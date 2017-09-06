import calendar

#Q1.

leap_year=[]

for i in range(1950,2018,1):
    for j in range(2,3):
        if calendar.monthrange(i,j)[1] == 29:
            leap_year.append(i)

#print(leap_year)

def day(a):
    if a == 0 : return '월요일'
    elif a == 1 : return '화요일'
    elif a == 2 : return '수요일'
    elif a == 3 : return '목요일'
    elif a == 4 : return '금요일'
    elif a == 5 : return '토요일'
    elif a == 6 : return '일요일'
    else : return


days=[]


for i in leap_year:
    for j in range(1,2):
        days.append(day(calendar.weekday(i,j,j)))

for i in range(len(days)):
    print(leap_year[i],days[i])

print("="*70)

#Q2.

sum = 0
for i in range(1950,2018,1):
    for j in range(1,13,1):
        sum += calendar.monthrange(i,j)[1]
print('The sum of days 1950~2017 is : %d'%(sum))

print("="*70)

#Q3.

fr13_sum =0
for i in range(1950,2018,1):
    for j in range(1,13,1):
        if calendar.weekday(i,j,13) == 4 :
            fr13_sum += 1
print('The sum of 13th Friday is : %d'%(fr13_sum))