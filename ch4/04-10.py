"""4-10"""
MAXNUM = 4
MAXHEIGHT = 130

more = True
cnt = 0
while more:
    height = float(input('키는?'))
    if height < MAXHEIGHT:
        cnt += 1
        print("들어가세여", '%d명' % cnt)
    else:
            print("커서 못 들어가요.")
    if cnt == MAXNUM:
         more = False
    else:
        print("%d 명이 모두 찼습니다. 다음번에 이용하세요." % cnt)
