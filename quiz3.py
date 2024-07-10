#사용자로부터 임의의 값을 받아서
#해당 수가 5와 10 사이에 있으면 'ok'를 출력하고
#그렇지 않은 경우 'no'를 출력하게 코드를 작성하시오.
#elif 사용
num = int(input("값을 입력하세요."))

if 5 < num < 10:
    print('ok')
elif num<=5:
    print('no')
elif num>= 10:
    print('no')
#else 사용
num=int(input("값을 입력하세요."))

if 5<num<10 :
    print('ok')
else :
    print('no')

