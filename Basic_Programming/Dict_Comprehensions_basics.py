# #Method 1: For-Loop
# import timeit
# # def square_for(arr):
# #     result = []
# #     for i in arr:
# #         result.append(i**2)
# #     return result
# # print ["List comprehension is" ]+ square_for(range(1,11))0
# # arr=range(1,11)
# def square_map(arr):
#     return map(lambda x: x**2, arr)
# print ["List comprehension is" ]+ square_map(range(1,11))
# 
# # square_map(range(1,11))


from collections import defaultdict
city_list = [('TX','Austin'), ('TX','Houston'), ('NY','Albany'), ('NY', 'Syracuse'), ('NY', 'Buffalo'), ('NY', 'Rochester'), ('TX', 'Dallas'), ('CA','Sacramento'), ('CA', 'Palo Alto'), ('GA', 'Atlanta')]

cities_by_state = defaultdict(list)
for state, city in city_list:
     cities_by_state[state].append(city)
     
print(cities_by_state)
for state, cities in cities_by_state.iteritems():
    print state, ', '.join(cities)