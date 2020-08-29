#Problem1
x = input("Type a number")
y = input("type a number")
if x == y:
    print("they are equal")
else:
    print("they are not equal")

#Problem2
a = input("type a number")
b = input("type a number")
if a + b == 10:
    print("it is equal to 10")
else:
    print("it is greater than or less than 10")


#Problem3
import random
prob = random.random()
print(prob)
number = range(1,5)
print(number)
if number == range(1,5):
    print("The number 5 is here")
else:
    print("The number 5 is not here")

#Problem4
year = input("enter a year")
if year % 4 == 0:
    print("it is a leap year")
elif year % 100 == 0:
    print("it is not a leap year")
elif year % 400  == 0:
    print("it is a leap year")
else:
    ("it is not a leap year")

#Problem5
list1 = [pan, paper, idea, rope, groceries]
debuffs = [slow]
if list1 == [rope, coat, firstaidkit] and debuffs != [slow]: 
    print("you can traverse the mountains")
else:
    print("finish gathering your items and cure any debuffs!")
if list1 == [pan, paper, idea, rope, groceries] and debuffs != [small]:
    print("You can cook a meal")
else:
    print("finish gathering your items and cure any debuffs!")
if list1 == [pan, pen, paper, idea, rope, groceries] and debuffs != [confusuon]:
    print("you can write a book")
else:
    print("finish gathering your items and cure any debuffs!")
