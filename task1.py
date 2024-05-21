# Set
my_set = {1,2,3,4,5}
my_set.add(6)
my_set.remove(3)
my_set.discard(2)
my_set.add(10)
print("Updated set:", my_set)
 
# List
my_list = [1,2,3,4,5]
my_list.append(7)
my_list.remove(2)
my_list[0] = 10
print("Updated list:", my_list)
 
# Dictionary
my_dict = {'name':'Newt', 'age':'24', 'city':'Bangalore'}
my_dict['gender'] = 'Male'
del my_dict ['age']
my_dict['city'] = 'Mumbai'
print("Updated dict:", my_dict)