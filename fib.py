n=8
a=0
b=1
c=0
if n==0:
    print('not valid')
elif n==1:
    print(n)
    print(a)
else:
    print('fibonaci starts : ')
    while n>c:
        print(a, end=' \n')
        nth =a+b
        a=b
        b=nth
        c+=1

#new_list
# new_list = []
# for j in range(3):
#     new_list.append([1,2,3])
# print(new_list)


# n='''
# in884120250401051228
# in206420250401061319
# in746820250401064406
# in332220250401130822
# in651920250401132947
# in274820250402092347
# in342920250402095059
# in122820250402095134
# '''
# n=n.split('\n')
# print(n)
n=[1,2,3,4,5]

for i in n:
    if i %2==0:
        print(f'even --{i}')
    else:
        print(f'odd --{i}')