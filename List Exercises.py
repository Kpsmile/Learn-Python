"""1. Which of the following commands will create a list(multiple answers allowed) ?
a) list1 = list()
b) list1 = [] c) list1 = list([1, 2, 3])
d) list1 = [1, 2, 3]"""

# list1 = list()
# list1 = [] 
list1 = list([1, 2, 3])
# d) list1 = [1, 2, 3]
print(list1)



# def dic(words):
#     data = {}
#     for i in words:
#         
# #       import pdb;pdb.set_trace()
#          try:
#              data[i] += 1
#              
# #          except KeyError: ## the famous pythonic way:
# #                 data[i] = 1 
# #       import pdb;pdb.set_trace()
#         return data
#   
# a='1,3,1,1,2,4,5,3,2,1,4,3,2'.split(',')
# a
# print(dic(a))
import collections
# 
from collections import defaultdict
# 
words = "apple banana apple strawberry banana lemon"
words = words.split()
result = collections.defaultdict(int)
for word in words:
     result[word] += 1
print result

n= [1,21,53,84,50,66,7,38,9]
odd=[]
even=[]
for i in n:
    if i%2==0:
        even.append(i)
    else:
         odd.append(i)
print even
print odd


even_1 = [i for i in n if i%2==0]
odd_1 = [i for i in n if i%2==1]
print even_1
print odd_1

asd =[1,21,53,84,50,66,7,38,9]
for index, data in enumerate(asd):
    print "{0} -> {1}".format(index, data)
    
n = [1,2,5,10,3,100,9,24]
 
for e in n:
  if e<5:
      
#     import pdb;pdb.set_trace()
    print e
#     n.remove(e)

def func(x,*y,**z):
    print x,y,z
 
func(1,2,3)
# print n

n = 1
n+=1
print n

a = [1,2,5,10,3,100,9,24]
b = [10,3,100,9,24]
def SwapLists(a, b):
     a[:] = b[:]
     print a

# x = input('Enter value of x: ')
# y = input('Enter value of y: ')
# 
# # create a temporary variable and swap the values
# # temp = x
# # x = y
# # y = temp
# # x,y=y,x
# x = x + y;  
# y = x - y;  
# x = x - y;
# 
# print('The value of x after swapping: {}'.format(x))
# print('The value of y after swapping: {}'.format(y))

# import time
# import thread
#  
# def myfunction(string, sleeptime, max_count, *args):
#  
#     counter = 0
#     ## To manage I/O
#     time.sleep(0.2)
#     while counter < max_count:
#         print "{}. {}".format(counter, string)
#         counter += 1
#         time.sleep(sleeptime)
#         #sleep for a specified amount of time.
#  
# if __name__=="__main__":
#  
#     print "thread Started : {}".format(thread.start_new_thread(myfunction,("Thread No:1", 2, 10)))