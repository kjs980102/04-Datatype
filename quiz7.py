#점수 구간에 해당하는 학점이 아래와 같이 정의되어 있다.
#사용자로부터 score를 입력 받아 학점으로 환산하여 출력하라.

score=int(input("점수를 입력하세요.: "))

if 100>=score>=81 :
    print("학점은 A입니다.")
elif 80>=score>=61 :
    print("학점은 B입니다.")
elif 60>=score>=41:
    print("학점은 C입니다.")
elif 40>=score>=21 :
    print("학점은 D입니다.")
elif 20>=score>=0 :
    print("학점은 E입니다.")
