"""6-9"""
daysA = {'월','화','수','목'}
daysB = (['수','목','금','토','일'])
weekends = set(('토','일'))

alldays = daysA.union(daysB) # alldays = daysA | daysB
print(alldays)

workdays = alldays - weekends
print(workdays)

print(daysA.intersection(daysB)) # daysA & daysB
print(daysA.symmetric_difference(daysB))
