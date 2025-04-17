name ='naman'
# if (name ==name[::-1]):
#     print('this is a palindrome')
# else:
    # print('not palindrome')

#---2--
# string ='Shivam'
# is_palindrome = True
# for i in range(0, int(len(string)/2)):
#     if string[i]!=string[len(string)-i-1]:
#         is_palindrome= False
#         break 
# if is_palindrome:
#     print('palindrome')
# else:
#     print('Not palindrome')

# ---------3-----------
# n=int[1,2,3,4,5]
# n=n[::-1]
# print(n)

for i in range(1,20):
    c=0
    for j in range(1,i+1):
        if (i%j ==0):
            # print(i,'Not prime', end= ', \n')
            c+=1
            
    if(c==2):
        print(i,'prime', end=', ')
