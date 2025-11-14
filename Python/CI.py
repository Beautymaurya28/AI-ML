# 1.Total amount
#total amount=1+r(100)*t;

# 2.ci=totalamount-principal

p=1000 
r=10/100
n=1
t=3
A=p*(1+r/n)**(n*t)
ci=A-p
print("compound interest is:",ci)
print("total amount is :",A)

