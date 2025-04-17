#Even Numbers _
def is_even(a):
    return a%2 ==0

numbers=[2,1,4,5,6,7,8,9]    #ye main list hai jo sare function me call ho rahi hai

# evens =tuple(filter(is_even,numbers))
# print(evens)

evenNumber =tuple(filter(lambda a:a%2==0, numbers))
print(f'Using_lambda_function -->{evenNumber}') 


#using normaly
evenNumber =filter(lambda a:a%2==0, numbers)
for i in evenNumber:
    print(i)

#using list_comprehension
new_even =[i for i in numbers if i%2==0]
print(f'List_comp_Even -->{new_even}')