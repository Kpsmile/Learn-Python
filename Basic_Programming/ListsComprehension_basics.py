sentence='My Name is Kp Singh'
def eg_lc(sentence):
     vowel='a,e,i,o,u'
     return''.join(l for l in sentence if l not in vowel)
     
print"List comprehension is" + eg_lc(sentence)
 
"""square of only even numbers in the list    
def square_map(arr):
    return map(lambda x: x**2, arr)
print ["List comprehension is" ]+ square_map(range(1,11))"""

"""square of only even numbers in the list"""
def even_fil(arr):
    return str(filter(lambda x:x is not None ,map(lambda x:x**2 if x%2==0 else None, arr)))
print "square of only even numbers in the list is :" + even_fil(range(1,11))

#Method 3: List comprehension:
def square_even_lc(arr):
    return str([i**2 for i in arr if i%2==0])
print "square of only even numbers in the list is :"+square_even_lc(range(1,11))
    
"""
Counting the occurrences of one item in a list
"""
l=['q','a','q', 1,3,1,2,3]
res=[[x,l.count(x)] for x in set(l)]
res_1=[[x,l.count(x)] for x in (l)]
print res
print res_1