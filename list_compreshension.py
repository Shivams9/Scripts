#input =[True, False,[1,2,3],1,1.0,3]
#output = ['1','2','3']

l1 = [1,2,4]
l2 = [1,3,4]  
c=[]  
# for i in l1,l2:
#     if i==i:
#         c.append(i)
#     print(i)
# print(c)
#reverse string
# s='shivam'  
# rv =""
# for c in s:
#     rv = c+rv
# print(rv)

#reverse list
# l=[1,2,3,4,5]
# rv = []
# for i in l:
#     rv.insert(0,i)
# print(rv)

n=5 
for i in range(1,11,1):
    print(i*n,end = "")

# str = "DoctorPhenomenal"
# for i in range(0,str,2):
#     # print(str[i],end=' ')
#     print(i,end=' ')
def num_to_string(l):
    return [str(i) for i in l if (type(i)== int or type(i) == float)]

print(num_to_string([True,False,[1,2,3],1,2.0,3]))


