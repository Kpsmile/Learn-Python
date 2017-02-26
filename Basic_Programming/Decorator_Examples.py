def smart_divide(func):
    def inner_func(a,b):
        print("Going to divide A by B")
        if b==0:
            print("OOPs b is -ve")
            return
        return func(a,b)
    return inner_func

@smart_divide
def divide(a,b):
    return a/b
#     print(result)

divide=(2,5)




            
        