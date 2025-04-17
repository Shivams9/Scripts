#map_function - ittrable( we can run only on map object) 
#We can change map into list and then we can run multiple time loop
#OutPut

numbers = [1,2,3,4]
# def square(a):
#     return a**2

# l=[square(1),square(2),square(3)]
# print(l)
# squares =list(map(square,numbers))
# print(squares)

#using lambda function
squares =list(map(lambda a:a**2,numbers))
print(squares)

#With list compreshension
square_new = [ i**2 for i in numbers]
print(square_new)

#Normal with python
l=[1,2,3,4]

def square(a):
    return a**2

new_list =[]
for i in l:
    new_list.append(square(i))

# print(new_list)

#map function another example :
#find lenght of list of string
name =['don','police', 'hero']
new =map(len,name)
for i in new:
    print(i)
# print(new)
