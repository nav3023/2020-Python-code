"""6-6"""
color = dict(검은색 ='black',흰색='white',녹색='greeb',파란색='blue')
print(color)

#항목조회
print(color.get('녹색'))
print(color.get('노란색'))
print()
#항목추가
color['노란색'] = 'yellow'
print(color)
print()
#항목 삭제
c = '흰색'
print('삭제: %s %s' % (c, color.pop('흰색')))
print(color)
c = '빨간색'
print('삭제: %s %s' % (c, color.pop(c,'없어요')))

print('임의 삭제: {}'.format(color.popitem()))
print('임의 삭제 후: {}'.format(color))

c = '검은색'
del color[c]
print('{} 삭제 후: {}'.format(c, color))
#모든항목삭제
color.clear()
print(color)
