



### while or for loop:
#24 reverse number
# num=int(input("enter a number: "))
# rev=0
# while(num>0):
#     digit=num%10 #123=123%10=3,
#     rev=rev*10+digit
#     num//=10

# print(rev)
    

#25 count of digits in num
num=int(input("enter the digit"))
count=0
while(num):
    digit=num%10
    count+1

print(count)