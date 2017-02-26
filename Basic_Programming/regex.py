import re

addressToVerify ='_infokp123@emailhippo.com'
# match = re.match('^[_a-z0-9-]+(\.[_a-z0-9-]+)*@[a-z0-9-]+(\.[a-z0-9-]+)*(\.[a-z]{2,4})$', addressToVerify)
match = re.match('^([a-z0-9_\.-]+)@([\da-z]+)\.([a-z]{2,6})$', addressToVerify)

if match == None:
    print('Bad Syntax')
    raise ValueError('Bad Syntax')
else:
    print(match)