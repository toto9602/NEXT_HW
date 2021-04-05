money = 200

if money > 5000:
    print("택시 타세요")
elif money > 1300:
    print("지하철 타세요")
elif money > 500:
    print("뛰어 가세요")
else:
    print("걸어 가세요")



likelion = ("단비", "연우", "동현", "지현")

if "해주" in likelion:
    print("멋사입니다")
elif "해주" not in likelion:
    print("멋사가 아닙니다")

count = 1

while count < 5:
    print("%d번째 반복 중" % count)
    # count = count + 1
    count += 1

for i in range(1, 5, 2):
    print(i)

while count < 5:
    if count == 3:
        continue

    print("%번째 반복 중" % count)
    count = count + 1

for i in range(1, 5, 1):
    if i % 2 == 0:

    print("%번째 반복 중" % i)

count = 5
print("{}번째 반복 중".format(count))
print(f'{count}번째 반복 중')



 #함수

def add(a, b):
    return a + b

print(add(1,2))

def add(a,b):
    print(a+b)

def get_number():
    return 4

print(get_number())

def say_hello():
    print("hello")

say_hello()