# print("i am Aniedi Ndem")
# print('o----')
# print(' IIII')
#
# print('*' * 10)
# name = "Aniedi Abasi"
#
# age = 58
#
# print(f" I'm {name}, {age} years old. I'm here now for python and django")
import time

#
# age = int(input("How old are you?:"))
#
# if age == 100:
#     print("You are a centurion")
# elif age >= 18 and age < 100:
#     print("You are an adult")
# elif age < 18:
#     print("You are a newbie")


# name = ""
# while len(name) == 0:
#     name = input("Enter your name>: ")
# print("Hello "+name)


# name = None
# while not name:
#     name = input("Enter your name>: ")
# print("Hello "+name)

# while True:
#     name = input("Enter your name: ")
#     if name != "":
#         break
# print("Hello "+name)

# import time
#
# for seconds in range(10, 0, -1):
#     print(seconds)
#     time.sleep(1)
# print("Happy New Year!!!!")

# rows = int(input("Enter rows:> "))
# columns = int(input("Enter columns:> "))
# symbol = input("Enter symbol:> ")
#
# for i in range(rows):
#     for j in range(columns):
#         print(symbol, end="")
#     print("")


# capitals = {'USA': 'WASHINGTON DC',
#             'NIGERIA': 'ABUJA',
#             'GHANA': 'ACCRA',
#             'RUSSIA': 'MOSCOW'
# }

# print(capitals['USA'])
# print(capitals['KENYA'])
# print(capitals.get('KENYA'))
# print(capitals.get('USA'))

# for key, value in capitals.items():
#     print(key + " : " + value)
#


# def add(*args):
#     sum = 0
#     stuff = list(args)
#     stuff[0] = 5
#     for i in stuff:
#         sum += i
#     return sum
#
#
# print(add(1, 2, 3, 4, 5, 6))

# WALRUS OPERATOR :=

# foods = list()
# while True:
#     food = input("What food do you like?: ")
#     if food == "quit":
#         break
#     foods.append(food)

# -------------------------------------

# foods = tuple()
# while food := input("What food do you like?: ") != "quit":
#     foods.append(food)

# Lambda Function

# double = lambda x: x * 2
# print(double(5))
# multiply = lambda x, y: x * y
# print(multiply(4, 7))


# names = ['John', 'Daisy', 'Bob', 'Lilly', 'Bob', 'Daisy']
# # will lose order of names
# # unique_names = list(set(names))
# unique_names = []
# for name in names:
#     if name not in unique_names:
#         unique_names.append(name)
#
# print(unique_names)

# will maintain order of names
# unique_names = list({name: name for name in names}.values())
# Or even simpler
# unique_names = list(dict.fromkeys(names))
# print(unique_names)



# numbers = [2, 2, 4, 6, 3, 4, 6, 1]
# uniques = []
# for number in numbers:
#     if number not in uniques:
#         uniques.append(number)
#
# print(uniques)



# x = 7, 8, 9
# sorted(x) == x
# # sorted_x = sorted(x)
# sorted_x = list(x)
# print(sorted_x)
#


# a = [4, 2, 1, 3]
# sorted_a = sorted(a)
# a = a.sort()
# b = None
# print(sorted_a)


# x = 5
# y = 10
# result = True if x < y else False
# print(result)

# my_list = ["I", "like", "Python", "a", "lot"]

# # print(sorted(my_list, key=len)[-1])
#
# print(max(my_list, key=len))
# l_word = sorted(my_list, key=lambda s: -len(s))[0]
# l_word = sorted(my_list, key=lambda s: len(s))[-1]
# print(l_word)

# print(sorted(my_list, key=lambda s: -len(s))[0])


# x = 2
# y = 10
#
# x x * y * x + 1
#
# print(x)
# nums = (20, 1, 53, 5, 9)
#
# def find_max(nums):
#     max_num = float("-inf")
#     for num in nums:
#         # print(num)
#         if num > max_num:
#             max_num = num
#             # num = max_num
#
#     return max_num
# # print(max_num)
#
# result = find_max(nums)
# print(result)


# nums = (20, 1, 53, 5, 9)
#
# max_num = nums[0]
# for num in nums:
#     if num > max_num:
#         max_num = num
#
#
# print(max_num)


# def adder(numbers=[]):
#     numbers.append(2)
#     return numbers
#
#
# result = adder()
# print(result)

# from collections import Counter
#
# counter = Counter(["blue",
#                    "red",
#                    "blue",
#                    "green",
#                    "red",
#                    "blue",
#                    "blue"])
#
# print(counter.most_common()[1])


 