n=int(input("enter no. of terms"))
a=1
b=1
show=0
i=0
for i in range(n):
    if i==0 or i==1:
        print(i)
    show=a+b
    print(a)
    b=a
    a=show
    i=i+1
  
