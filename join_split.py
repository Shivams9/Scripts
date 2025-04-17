#split method- string ko list me convert karta hai, jahan space hoga se break karega
#split method 'shivam,50' hai toh esko todne ke leye .split(',') value denge jahan comma hai wahan se todega
#convert string to list
user_info = 'harshit,24'.split(',')
# print(user_info)
# name,age=input('Enter name and Age : ').split()
# print(name)
# print(age)

#join method - string k andar jo caractr likhna chahte hai vo add karenge aur list ko string me change karte hai
#convert List to String : 
user = ['Samrat', '24']
# print(','.join(user))

n=7
for i in range(2,n):
    if (n%i==0):
        print('not prime')
        break
else:
    print('prime')