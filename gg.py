# ### Day 2 ###
# ###
# for i in range(10, 21, 2):
#     print(i)
#
# cat_names = ["Kiki", "Jack", "Tom", "Dog"]
#
# ###
# print("If I have a cat, I will call it", ','.join(cat_names),".")
# print("If I have a cat, I will call it {}.".format(','.join(cat_names)))
#
# ###
# counter = 5
# while counter > 0:
#     print(counter)
#     counter = counter - 1
#
# counter = 5
# while counter > 0:
#     print(counter)
#     counter -= 1
#
# ###
# counter = 30
# while counter > 0:
#     if counter % 4 == 0:
#         print(counter)
#     counter -= 1

# ###
# b = float(input("How many deciliters?"))
# cup = b/2.37
# print(b, "deciliters is equivalent to", cup, "cups.")

###
# index = [4, 7, 4, 3, 9]
# num = float(input("Guess a number in the list!"))
# if num in index:
#     col = [4, 7, 4, 3, 9].index(num)
#     print("output is", col)
# else:
#     print("Output is none.")

###
# list = [2, 6, 3, 0, 4, 3]
# mylist = []
# while len(list) != 0:
#     low = min(list)
#     list.remove(low)
#     mylist.append(low)
# print(list)
# print(mylist)
###
# list = [2, 6, 3, 0, 4, 3]
# mylist = []
# for i in range(len(list)):
#     low = min(list)
#     list.remove(low)
#     mylist.append(low)
#print(mylist)

###
# def test_recipe(food_1, food_2):
#     recipe = food_1 + food_2
#     print(recipe)
#     return "The ingredients are " + food_1 + " and " + food_2 +"."
# food_1 = "egg"
# food_2 = "milk"
# print(test_recipe(food_1, food_2))

###
# def F(n):
#     if n == 0:
#         return 0
#     elif n == 1:
#         return 1
#     else:
#         return F(n-1)+F(n-2)
# n = 10
# print(F(n))


###
import dog
dog.bark(3)

