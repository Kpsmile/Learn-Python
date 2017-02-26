a = [3, 6, 8, 2, 78, 1, 23, 45, 9]
print(sorted(a))

"""
Sorting a List of Lists or Tuples
This is a little more complicated, but still pretty easy, so don't fret! 
Both the sorted function and the sort function take in a keyword argument called key.

What key does is it provides a way to specify a function that returns what you would like your items 
sorted by. The function gets an "invisible" argument passed to it that represents an item in the list,
 and returns
 a value that you would like to be the item's "key" for sorting.
So, taking a new list, let's test it out by sorting by the first item in each sub-list
"""
def getkey(item):
    return item[1]

l=[[1,30],[4,21],[3,7]]

res=sorted(l, key=getkey)
print(res)

"""
Sorting a List (or Tuple) of Custom Python Objects
"""
class Custom(object):
    def __init__(self, name, number):
        self.name=name
        self.number=number
        
    def __repr__(self):
        """
        the __repr__ function tells Python how we want the object to be represented as.
        it tells the interpreter how to display the object when it is printed to the screen.
        """
        return'{}: {} {}'.format(self.__class__.__name__,
                                 self.name,
                                 self.number)
        
Customlist=[Custom('abc',10),Custom('xyz',10),Custom('jklm',10),Custom('qrs',10)]
def getkey(item):
    return item.name
results=sorted(Customlist, key=getkey)
result_rev=sorted(Customlist, key=getkey,reverse=True)
print(results)
print(result_rev)
    
        
    
        
        
    