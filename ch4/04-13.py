"""4-13"""
number = 11,17,28,30,33,35
print('모의 로또 당첨 번호'.center(28,'='))
print(number)
print()
print('내 번호 확인'.center(30,'-'))
cnt = 0
import random
for i in range(6):
    n = random.randint(1,45)
    if n in number:
        print(n,'O', end=' ')
        cnt += 1
    else:
        print(n,'X', end=' ')

    print()
    print(cnt,'개맞음')
