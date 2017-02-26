
import random
 
items = ['here', 'are', 'some', 'strings', 'of',
         'which', 'we', 'will', 'select', 'one']
 
# rand_item = items[random.randrange(len(items))]
# rand_item = random.choice(items)
rand_item = random.sample(items, 5)
print(rand_item)