#입력받은 문자열의 역순을 출력하는 함수를 작성하세요.
#ex) python -> nohtyp
str = input("문자열을 입력하세요: ")

def reverse_str(str):
    for i in range(len(str)-1, -1, -1):
        print(str[i], end="")

reverse_str(str)
