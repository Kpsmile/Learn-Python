def gcf(num1, num2):
    if num1>num2:
        num1,num2=num2,num1
        
#     print(num1,num2)
        
    for x in range(num1, 1,-1):
#          print(x)
         if num1%x==0 and num2%x==0:
            print("GCF")
            return x
num1=54
num2=24
print(str(gcf(num1, num2)))