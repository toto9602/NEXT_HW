from django.shortcuts import render

# Create your views here.
def count(request):
    return render(request, 'count.html')

def result(request):
    text = request.POST['text']
    total_len = len(text)
    total_text = text
    texts = len(text.replace(' ', ''))
    count_word = len(text.split())

    return render(request, 'result.html', {'total_len': total_len, 'total_text':total_text, 'texts':texts, 'count_word':count_word,})
