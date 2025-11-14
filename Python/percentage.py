#write a program to input marks scored by a student in 3 subject and compute the percentage obtained
sub1=int(input("enter the first sub marks: "))
sub2=int(input("enter the sec sub marks: "))
sub3=int(input("enter the third sub marks: "))
obtainedmarks=sub1+sub2+sub3
percentage=(obtainedmarks/300)*100
print("the score is: ",percentage)
