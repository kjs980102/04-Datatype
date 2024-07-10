# 사용자로부터 입력 받은 단어가 아래 fruit 리스트에 포함되어 있는지를 확인하라.
# 포함되었다면 "정답입니다"를 아닐 경우 "오답입니다"를 출력하라.

# 과일=input("좋아하는 과일")
# fruit=["사과","포도","홍시"]
#
# if 과일 in fruit :
#     print("정답입니다")
# else :
#     print("오답입니다")

data=input("좋아하는 계절: ")
fruit={"봄":"딸기","여름":"토마토","가을":"사과"}

if data in fruit :
    print("정답입니다")
    print(fruit[data]+"가 제철입니다.")
else :
    print("오답입니다")

