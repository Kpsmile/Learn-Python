# Writing a File

# fo = open("foo.txt", "wb")
# fo.write( "Python is a great language.\nYeah its great!!\n");
# 
# # Close opend file
# fo.close()


# you can write to stdout for debugging purposes, e.g.
# print "this is a debug message"
from datetime import datetime

def solution(E, L):
    # write your code in Python 2.7
    s1 = E
    s2 = L # for example
    FMT = '%H:%M'
    time_delta = datetime.strptime(s2, FMT) - datetime.strptime(s1, FMT)
    print (time_delta)
    
    
    parking_fee=2
    
    
    if time_diff>1:
        partial_hr=time_diff-1
        costs=2+3+4*partial_hr
        return costs
    else:
        partial_hr=time_diff-1
        costs=2+3
        return costs
        
solution('09:42','11:42')
    