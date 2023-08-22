# Sequence Types
#Note: use print() to execute the examples. Comment out examples after they've been demoed.
def p(x):
    print(x)
# Creating Lists
#1. ✅ Create a list of 10 pet names
pet_names = ['Rose', 'Meow Meow Beans', 'Mr.Legumes', 'Luke', 'Lea', 'Princess Grace', 'Spot', 'Tom', 'Mini', 'Paul']

# Reading Information From Lists
#2. ✅ Return the first pet name
# print(pet_names[0])
# Rose


#3. ✅ Return all pet names beginning from the 3rd index
# print(pet_names[3:])
# ['Luke', 'Lea', 'Princess Grace', 'Spot', 'Tom', 'Mini', 'Paul']

#4. ✅ Return all pet names before the 3rd index
# print(pet_names[:3])
# ['Rose', 'Meow Meow Beans', 'Mr.Legumes']

#5. ✅  Return all pet names beginning from the 3rd index and up to the 7th
# start = 3
# end = 7
# print(pet_names[start:end])
# ['Luke', 'Lea', 'Princess Grace', 'Spot']

#6. ✅ Find the index of a given element
# luke_index = pet_names.index("Luke")
# -> 3
# p(pet_names[luke_index])
# -> "Luke"

#7. ✅ Reverse the original list'
# p(pet_names)
# ['Rose', 'Meow Meow Beans', 'Mr.Legumes', 'Luke', 'Lea', 'Princess Grace', 'Spot', 'Tom', 'Mini', 'Paul']
# p(pet_names.reverse())
# p(pet_names)
# ['Paul', 'Mini', 'Tom', 'Spot', 'Princess Grace', 'Lea', 'Luke', 'Mr.Legumes', 'Meow Meow Beans', 'Rose']

#8. ✅ Return the frequency of a given element 
# given_element = "Paul"
# count = 0
# for pet in pet_names:
#     if pet == given_element:
#         count = count + 1
# print(count)
# -> 1
# count = pet_names.count(given_element)
# print(count)
# -> 1


# Updating Lists
#9. ✅ Change the first element to all uppercase 
# pet_names[0] = pet_names[0].upper()
# p(pet_names[0])
# -> ROSE

#10. ✅ Append a new name to the list
# new_name = "Ashe"
# pet_names.append(new_name)
# p(pet_names)

#11. ✅ Add a new name at a specific index
# pet_names.insert(3,"Ashe")
# p(pet_names)
# -> ['Rose', 'Meow Meow Beans', 'Mr.Legumes', 'Ashe', 'Luke', 'Lea', 'Princess Grace', 'Spot', 'Tom', 'Mini', 'Paul']


#12. ✅ Add two lists together 
# extra_pets = ["Ashe", "Isha", "Liam"]
# p(extra_pets)
# added_list = pet_names + extra_pets
# p(added_list)
# -> ['Rose', 'Meow Meow Beans', 'Mr.Legumes', 'Luke', 'Lea', 'Princess Grace', 'Spot', 'Tom', 'Mini', 'Paul', 'Ashe', 'Isha', 'Liam']


#13. ✅ Remove the final element from the list
# pet_names.pop()
# p(pet_names)
# -> ['Rose', 'Meow Meow Beans', 'Mr.Legumes', 'Luke', 'Lea', 'Princess Grace', 'Spot', 'Tom', 'Mini']

#14. ✅ Remove element by specific index
# pet_names.pop(3)
# p(pet_names)
# -> ['Rose', 'Meow Meow Beans', 'Mr.Legumes', 'Lea', 'Princess Grace', 'Spot', 'Tom', 'Mini']

#15. ✅ Remove a specific element 
# p(pet_names)
# name_to_remove = 'Meow Meow Beans'
# try:
#     pet_names.remove(name_to_remove)
# except:
#     p(f"Could not find {name_to_remove}")
# p(pet_names)
# ->['Rose', 'Meow Meow Beans', 'Mr.Legumes', 'Luke', 'Lea', 'Princess Grace', 'Spot', 'Tom', 'Mini', 'Paul']
# ->['Rose', 'Mr.Legumes', 'Luke', 'Lea', 'Princess Grace', 'Spot', 'Tom', 'Mini', 'Paul']

#16. ✅ Remove all pet names from the list
# while len(pet_names) > 1:
#     pet_names.pop()
# pet_names.clear()
# p(pet_names)
# -> []
#Tuple 
# 📚 Review With Students:
    # Mutable, Immutable, Changeable, Unchangeable

#17. ✅ Create a Tuple of pet 10 ages 
pet_ages = (3, 3, 5, 1, 2, 4, 9, 2, 3, 1)
# p(pet_ages)

#18. ✅ Print the first pet age
# p(pet_ages[0])

# Testing Changeability 
#19. ✅ Attempt to remove an element with ".pop" (should error)
# pet_ages.pop()
# -> 'tuple' object has no attribute 'pop'

#20. ✅ Attempt to change the first element (should error)
# pet_ages[0] = 4
# -> 'tuple' object does not support item assignment

# Tuple Methods
#21. ✅ Return the frequency of a given element
# three_frequency = pet_ages.count(3)
# p(three_frequency)
# -> 3

#22. ✅ Return the index of a given element 
#twelve_index = pet_ages.index(12)
# -> ValueError: tuple.index(x): x not in tuple
# three_index = pet_ages.index(3)
# p(three_index)
# -> 0
# p(pet_ages[three_index])
# -> 3

#23. ✅ Create a Range 
#Note:  Ranges are primarily used in loops
# my_range = range(len(pet_ages))
# for num in my_range:
#     print(f"The count is {num}")
# The count is 1
# ...
# The count is 9


# Demo Sets (Stretch Goal)
#24. ✅ Create a set of 3 pet foods
# p(pet_ages)
# pet_ages_set = set(pet_ages)
# p(pet_ages_set)
# pet_ages_set = {1, 3, -1, -5, 3, 2, 3, -6}
# p(pet_ages_set)
# -> {1, 2, 3, -6, -5, -1}

# Demo Dictionaries 
# Creating 
#25. ✅  Create a dictionary of pet information with the keys "name", "age" and "breed"
pet_info_rose = {'name':'rose','age':11,'breed':'domestic long '}
# p(pet_info_rose)

#26. ✅  Use dict to create a dictionary of pet information with the keys "name", "age" and "breed"
pet_info_spot = dict(name='Spot', age=25, breed='boxer')
# p(pet_info_spot)

# Reading
#27. ✅ Print the pet attribute of "name" using bracket notation
# for attribute in pet_info_rose:
#     p(f"This attribute is {attribute}")
#     p(pet_info_rose[attribute])
#     p(pet_info_spot[attribute])
    # ->
# This attribute is name
# rose
# Spot
# This attribute is age
# 11
# 25
# This attribute is breed
# domestic long 
# boxer


#28. ✅ Print the pet attribute of "age" using ".get"
#Note: ".get" is preferred over bracket notation in most cases because it will return "None" instead of an error
# rose_age = pet_info_rose.get('age')
# p(rose_age)

# Updating 
#29. ✅ Update the pets age to 12
# p(pet_info_rose)
# pet_info_rose['age'] = 12
# p(pet_info_rose)

#30. ✅ Update the other pets age to 26
# p(pet_info_spot)
# pet_info_spot.update(age=26, color='brown')
# p(pet_info_spot)
# ->
# {'name': 'Spot', 'age': 25, 'breed': 'boxer'}
# {'name': 'Spot', 'age': 26, 'breed': 'boxer', 'color': 'brown'}

# Deleting
#30. ✅ Delete a pets age using the "del" keyword 
# del pet_info_spot['color']
# p(pet_info_spot)
# # ->
# {'name': 'Spot', 'age': 26, 'breed': 'boxer', 'color': 'brown'}
# {'name': 'Spot', 'age': 26, 'breed': 'boxer'}

#31. ✅ Delete the other pets age using ".pop"
# p(pet_info_rose.pop('age'))
# -> 11

#32. ✅ Delete the last item in the pet dictionary using "popitem()"
# p(pet_info_rose)
# p(pet_info_rose.popitem())
# p(pet_info_rose)
# -> 
# {'name': 'rose', 'age': 11, 'breed': 'domestic long '}
# ('breed', 'domestic long ')
# {'name': 'rose', 'age': 11}

# Demo Loops 
pet_info = [
    {
        'name':'rose',
        'age':11,
        'breed': 'domestic long-haired',
    }, 
    {
        'name':'spot',
        'age':1,
        'breed': 'boxer',
    },
    {
        'name':'Meow Meow Beans',
        'age':2,
        'breed': 'domestic long-haired',
    }
    ]

#33. ✅ Loop through a range of 10 and print every number within the range
# for i in range(10):
#     print(i)
#     # if i > 5:
#     #     break
# else:
#     print("I got to the end of the loop")

#34. ✅ Loop through a range between 50 and 60 that iterates by 2 and print every number
# for num in range(50,61,2):
#     p(num)

#35. ✅ Loop through the "pet_info" list and print every dictionary 
# for pet in pet_info:
#     print(pet)
# {'name': 'rose', 'age': 11, 'breed': 'domestic long-haired'}
# {'name': 'spot', 'age': 25, 'breed': 'boxer'}
# {'name': 'Meow Meow Beans', 'age': 2, 'breed': 'domestic long-haired'}


#36. ✅ Create a function that takes a list as an argument 
    # The function should use a "for" loop to loop through the list and print every item 
    # Invoke the function and pass it "pet_names" as an argument
def print_list(list):
    for item in list:
        print(item)

# print_list(pet_info)

#37. ✅ Create a function that takes a list as an argument. (simple example) 
    # The function should define a counter and set it to 0
    # Create a "while" loop 
        # The loop will continue as long as the counter is less than the length of the list
        # Every loop should increase the count by 1
    # Return the counter 
# def count_elements(list):
#     counter = 0
#     while counter < len(list):
#         counter = counter + 1
#         p(counter)
#     return counter

# p(count_elements(pet_names))

#38. ✅ Create a function that updates the age of a given pet
        # The function should take a list of "dict"s, "name" and "age" as parameters 
        # Create am index variable and set it to 0
        # Create a while loop 
            # The loop will continue so long as the list does not contain a name matching the "name" param 
            # &&&& and 
            # the index is less then the length of the list
            # Every list will increase the index by 1
        # If the dict containing a matching name is found, update the item's age with the new age 
            # Otherwise, return 'pet not found'

# change the age of pet with this name
# def update_age(list_of_pets, name, new_age):
#     index = 0
#     while index < len(list_of_pets) and list_of_pets[index].get('name') != name:
#         index += 1
#         p(index)
    
#     # if we did find one
#     if list_of_pets[index].get('name') == name:
#         list_of_pets[index]['age'] = new_age
#     else:
#         return 'pet not found'

# print_list(pet_info)
# update_age(pet_info, "spot", 72)
# print_list(pet_info)

# map like 
#39. ✅ Use list comprehension to return a list containing every pet name from "pet_info" changed to uppercase
# pet_names_upper = [pet.upper() for pet in pet_names]
# p(pet_names)
# p(pet_names_upper)
# ['Rose', 'Meow Meow Beans', 'Mr.Legumes', 'Luke', 'Lea', 'Princess Grace', 'Spot', 'Tom', 'Mini', 'Paul']
# ['ROSE', 'MEOW MEOW BEANS', 'MR.LEGUMES', 'LUKE', 'LEA', 'PRINCESS GRACE', 'SPOT', 'TOM', 'MINI', 'PAUL']

# find like
#40. ✅ Use list comprehension to find a pet named spot
# find_spot = [pet for pet in pet_info if pet.get('name') == 'spot']
# p(find_spot)
# [{'name': 'spot', 'age': 25, 'breed': 'boxer'}]

# filter like
#41. ✅ Use list comprehension to find all of the pets under 3 years old
# young_pets = [pet for pet in pet_info if pet.get('age') < 3]
# p(young_pets)

#43. ✅ Create a generator expression matching the filter above. Compare and contrast the generator to the list comprehension. 
# young_pets_generator = (pet for pet in pet_info if pet.get('age') < 3)
# p(young_pets_generator)


