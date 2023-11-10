import random

def lotto():
    result = []
    while len(result) < 6:
        number = random.randint(1, 45)
        if number not in result:
            result.append(number)
            print(f"{number}을(를) 없습니다.")
        else:
            print(f"{number}은(는) 이미 있습니다..")

    print("로또 번호:", result)

# 함수 호출하여 로또 번호 생성
lotto()

