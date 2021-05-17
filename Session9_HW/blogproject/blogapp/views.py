from django.shortcuts import render, redirect
from .models import Post, Comment
from django.contrib.auth.models import User
from django.contrib import auth
from django.contrib.auth.decorators import login_required

# Create your views here.
def home(request):
    posts = Post.objects.all().order_by('date')   #마감 기한 적게 남은 순서대로 정렬하기????

    return render(request, 'home.html', {'posts' : posts})

@login_required(login_url='registration/login')
def new(request):
    if request.method == 'POST':
        new_post = Post.objects.create(
            title = request.POST['title'], #method == post 안에서 name이 title인 것 in templates
            content = request.POST['content'],
            date = request.POST['date'],
            author = request.user
        )
        return redirect('detail', new_post.pk)

    return render(request, 'new.html')

def detail(request, post_pk):
    post = Post.objects.get(pk=post_pk)

    if request.method == 'POST':
        content = request.POST['content']
        Comment.objects.create(
            post=post,
            content=content,
            author = request.user
        )
        return redirect('detail', post_pk)

    return render(request, 'detail.html', {'post':post})

def edit(request, post_pk):
    post = Post.objects.get(pk=post_pk)

    if request.method == 'POST':
        Post.objects.filter(pk=post_pk).update(
            title = request.POST['title'],
            content = request.POST['content'],
            date = request.POST['date']
        )
        return redirect('detail', post_pk)

    return render(request, 'edit.html', {'post' : post})

def delete(request, post_pk):
    post = Post.objects.get(pk=post_pk)
    post.delete()

    return redirect('home')

def delete_comment(request, post_pk, comment_pk):
    comment = Comment.objects.get(pk=comment_pk)
    comment.delete()
    return redirect('detail', post_pk)

def signup(request):
    if (request.method == 'POST'):
        found_user = User.objects.filter(username=request.POST['username'])
        if (len(found_user)) > 0:
            error = '이미 존재하는 ID입니다.'
            return render (request, 'registration/signup.html', {'error':error})

        new_user = User.objects.create_user(  #create하면, 그대로 저장되어서 관리자들이 비번 다 알 수 있다.
            username = request.POST['username'],
            password = request.POST['password']
        )
        auth.login(request, new_user) #회원가입 정상적으로 진행한 뒤에, 자동으로 로그인!
        return redirect('home')
    
    return render(request, 'registration/signup.html')

def login(request):
    if request.method == 'POST':
        found_user = auth.authenticate(
            username = request.POST['username'],
            password = request.POST['password']
        )

        if found_user is None:
            error = '아이디 또는 비밀번호가 틀렸습니다'
            return render(request, 'registration/login.html', {'error':error})
            
        auth.login(request, found_user) #none이 아니면 login하고
        return redirect('home')  #home으로 redirect

    return render(request, 'registration/login.html')

def logout(request):
    auth.logout(request)

    return redirect('home')

def mypage(request):
    my_posts = Post.objects.filter(author=request.user)
    my_comments = Comment.objects.filter(author=request.user)

    return render(request, 'registration/mypage.html', {'my_posts':my_posts, 'my_comments':my_comments})