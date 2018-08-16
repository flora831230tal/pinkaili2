'''Q4'''
raining = True
if True:
   print("watch TV")
else:
    print("take a walk")
'''Q5'''
print("Hip")
print("Hip")
print("Hurray")

for n in range(2):
    print("Hip")
    print("Hip")
    print("Hurray")

'''Q6'''
list = []
go_on = True
while go_on:
    a = input("what do you like to do?")
    if a == "stop":
        go_on = False
        break
    list.append(a)
print("Okay. My hobbies are", ','.join(list))

