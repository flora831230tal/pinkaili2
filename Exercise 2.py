# ###1:
# def info(name, hometown, skill):
#     print("This is ", name, " of ", howetown, " undefeated in ", skill, "!")
#
# ###2:
# def p_suggest(p_old):
#     if p_old > 100:
#         p = p_old*1.05
#     else:
#         p = p_old*1.1
#     print("The total price is suggested to be", p, " when the price is ", p_old)
#
# p_suggest(20)

# ###3:
# import random
# list = ["rich", "smart", "lucky", "super strength"]
# print(random.choice(list))

###4:
# def count(n, m):
#     list = []
#     for i in range(n, m+1, 1):
#         list.append(i)
#     print(list)
#
# count(3, 10)

###5:
# def up_case():
#     string = str(input("what's the word?"))
#     print(string.upper())
# up_case()

# ###6:
def roversprak():
    string = str(input("what's the word?"))
    l = list(string)
    lnew = ""
    for i in l:
        print(i)
        if i not in ["a", "e", "i", "o", "u"]:
            lnew += i + "o" + i
        else:
            lnew += i
    print(lnew)

roversprak()








