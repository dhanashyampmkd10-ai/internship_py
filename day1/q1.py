total=0
print("enter 5 marks:")
m1=int(input("mark 1: "))
m2=int(input("mark 2: "))
m3=int(input("mark 3: "))
m4=int(input("mark 4: "))
m5=int(input("mark 5: "))
total=m1+m2+m3+m4+m5
avg=total/5
if avg>=90:
    print("Grade A")
elif avg>=80:
    print("Grade B")
elif avg>=70:
    print("Grade C")
elif avg>=60:
    print("Grade D")
else:
    print("Grade F")

print ("average=",avg)



