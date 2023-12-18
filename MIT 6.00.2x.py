# ## MIT 6.00.2x Code below:

# # ---

# # print("Hello world!")

# #  ---

# NUMBER = 3
# def look_for_things(myList):
#     """Looks at all elements"""
#     for n in myList:
#       if n == NUMBER:
#         return True
#     return False

# # ---

# # NUMBER = 3
# # def look_for_other_things(myList):
# #   """Looks at all pairs of elements"""
# #   for n in myList:
# #     for m in myList:
# #       if n - m == NUMBER or m - n == NUMBER:
# #         return True
# #   return False

# #  ---

# # def get_all_subsets(some_list):
# #   """Returns all subsets of size 0 - len(some_list) for some_list"""
# #   if len(some_list) == 0:
# #     # If the list is empty, return the empty list
# #     return [[]]
# #   subsets = []
# #   first_elt = some_list[0]
# #   rest_list = some_list[1:]
# #   # Strategy: Get all the subsets of rest_list; for each
# #   # of those subsets, a full subset list will contain both
# #   # the original subset as well as a version of the subset
# #   # that contains first_elt
# #   for partial_subset in get_all_subsets(rest_list):
# #     subsets.append(partial_subset)
# #     next_subset = partial_subset[:] + [first_elt]
# #     subsets.append(next_subset)
# #   return subsets

# # NUMBER = 3
# # def look_for_all_the_things(myList):
# #   """Looks at all subsets of this list"""
# #   # Make subsets
# #   all_subsets = get_all_subsets(myList)
# #   for subset in all_subsets:
# #     if sum(subset) == NUMBER:
# #       return True
# #   return False

# # print(look_for_all_the_things([1,2,4]))

# # ---

# # print(1%2)

# # ---

# # generate all combinations of N items
# def powerSet(items):
#   N = len(items)
#   # enumerate the 2**N possible combinations
#   for i in range(2**N):
#     combo = []
#     for j in range(N):
#       # print("this is i and j:", bin(i), j)
#       # test bit jth of integer i
#       if (i >> j) % 2 == 1:
#         combo.append(items[j])
#         print(i, j, "THIS ONE DID IT")
#       print(i, j)
#     yield combo

# def decimal_to_ternary(decimal, length):
#   ## THIS FUNCTION CONVERTS DECIMAL DIGITS INTO TERNARY DIGITS
#   result = ''

#   if decimal == 0:
#     while len(result) != length:
#       result = "0" + result

#   while decimal > 0:
#     remainder = decimal % 3
#     result = str(remainder) + result
#     decimal = decimal // 3

#   if length == len(result):
#     return result
#   else:
#     while len(result) != length:
#       result = "0" + result

#     return result

# def yieldAllCombos(items):
#   """
#     Generates all combinations of N items into two bags, whereby each
#     item is in one or zero bags.

#     Yields a tuple, (bag1, bag2), where each bag is represented as a list
#     of which item(s) are in each bag.
#   """
#   N = len(items)

#   for i in range(3**N):
#     i = decimal_to_ternary(i, N)
#     combo = ([], [])

#     for index, j in enumerate(i):
#       if int(j) == 1:
#         combo[0].append(items[index])
#       elif int(j) == 2:
#         combo[1].append(items[index])

#     yield combo

# items = ['a', 'b', 'c', 'd', 'e', 'f']

# for index, i in enumerate(yieldAllCombos(items)):
#   print(i)

# ---

## We will check the zero index or the second index

# nodeList = []
# for node in nodes:
#   for n in nodes:
#     if node.getName()[0] == n.getName()[0] \
#       or node.getName()[2] == n.getName()[2]:
#       nodeList.append([node, n])

# tempList = []
# finalList = []

# for n in nodeList:
#   tempList.append([n[1], n[0]])
#   if [n[0], n[1]] not in tempList:
#     finalList.append([n[0], n[1]])

# for n in finalList:
#   g.addEdge(Edge(n[0], n[1]))

# ---

## Starting work on problem 3.7; Answer below:

# class WeightedEdge(Edge):
#   def __init__(self, src, dest, weight):
#     self.weight = weight
#     self.src = src
#     self.dest = dest
#   def getWeight(self):
#     return self.weight
#   def __str__(self):
#     return self.src.getName() + '->' + self.dest.getName() \
#       + " (" + str(self.weight) + ")"

#  ---

# import random


# def genEven():
#     '''
#     Returns a random even number x, where 0 <= x < 100
#     '''
#     return random.choice([num for num in range(0, 100, 2)])

# print(genEven())

#  ---

# import random


# def deterministicNumber():
#     '''
#     Deterministically generates and returns an even number between 9 and 21
#     '''
#     return 16

# print(deterministicNumber())

#  ---

# import random


# def stochasticNumber():
#     '''
#     Deterministically generates and returns an even number between 9 and 21
#     '''
#     randInt = random.choice([num for num in range(9, 22)])

#     while randInt % 2 == 1:
#       return stochasticNumber()
#     return randInt

# print(stochasticNumber())

# ---

# import random


# mylist = []

# ## Code I believed to be deterministic but it's actually stochastic.

# for i in range(random.randint(1, 10)):
#     random.seed(0)
#     if random.randint(1, 10) > 3:
#         number = random.randint(1, 10)
#         mylist.append(number)
# print(mylist)

# ---

# Starting week 2 pSet in another folder.

# import random


# width = 3
# height = 2
# cleanDict = {}

# for w in range(width):
#   for h in range(height):
#     cleanDict[w, h] = False

# cleanDict[2,1] = True

# for x,y in cleanDict.keys():
#   print(x,y)
# print(random.choice(list(cleanDict.keys())))

# ---

## Unit 3.7 Inferential Statistics

# def stdDevOfLengths(L):
#   """
#   L: a list of strings

#   returns: float, the standard deviation of the lengths of the strings,
#   or NaN if L is empty.
#   """
#   if len(L) == False:
#     return float("NaN")

#   total = 0 ## Calculates the mean
#   for number in L:
#     total += number
#   mean = total / len(L)

#   total = 0 ## Calculates the standard deviation
#   for number in L:
#     total += (number - mean)**2
#   standard = (total / len(L))**0.5

#   return standard / mean


# L = [1, 2, 3]
# print(stdDevOfLengths(L))
# L = [11, 12, 13]
# print(stdDevOfLengths(L))
# L = [.1, .1, .1]
# print(stdDevOfLengths(L))

#  ---

# import numpy


# def loadFile():
#   inFile = open('./julytemps.txt')
#   high = []
#   low = []
#   for line in inFile:
#     fields = line.split()
#     if len(fields) < 3 or not fields[0].isdigit():
#       continue
#     else:
#       high.append(int(fields[1]))
#       low.append(int(fields[2]))
#   diffTemps = list(numpy.array(high) - numpy.array(low))
#   return (diffTemps)

# print(loadFile())

#  ---

# L = [10, 9, 8, -1] ## 27
# secondNumList=  [3, 4, -8, 15, -1, 2] ##16
# thirdList = [3, 4, -1, 5, -4] ## 11
# highestCount = 0

# for index, num in enumerate(thirdList):
#   for n in range(len(thirdList), 0, -1):
#     # print(index, n)
#     if index == n:
#       break

#     currSum = sum(thirdList[index:n])
#     if currSum > highestCount:
#       highestCount = currSum

# print("This is highestCount:", highestCount)

#  ---

# import random

# def F(): ## DETERMINISTIC
#   mylist = []
#   r = 1

#   if random.random() > 0.99: ## IT WILL PASS THIS
#     r = random.randint(1, 10)
#   for i in range(r):
#     random.seed(0)
#     if random.randint(1, 10) > 3:
#       number = random.randint(1, 10)
#       if number not in mylist:
#         mylist.append(number)
#   print(mylist)

# def G():
#   random.seed(0)
#   mylist = []
#   r = 1

#   if random.random() > 0.99: ## IT WILL PASS THIS
#     r = random.randint(1, 10)
#   for i in range(r):
#     if random.randint(1, 10) > 3:
#       number = random.randint(1, 10)
#       mylist.append(number)
#       print(mylist)

# print(G())

#  ---

# one = []
# two = [1]
# three = [2]
# four = [10, 5 ,1]

# def greedySum(L, s):
#   """ input: s, positive integer, what the sum should add up to
#       L, list of unique positive integers sorted in descending order
#       Use the greedy approach where you find the largest multiplier for
#       the largest value in L then for the second largest, and so on to
#       solve the equation s = L[0]*m_0 + L[1]*m_1 + ... + L[n-1]*m_(n-1)
#       return: the sum of the multipliers or "no solution" if greedy approach does
#       not yield a set of multipliers such that the equation sums to 's'
#   """
#   multList = [0 for _ in range(len(L))]
#   tempS = s

#   for index, num in enumerate(L):
#     multiplier = multList[index]

#     while (num * (multiplier + 1)) <= tempS:
#       multiplier += 1
#     multList[index] = multiplier
#     tempS -= num * multiplier

#   if tempS == 0:
#     return sum(multList)
#   else:
#     return "no solution"

# print(greedySum([16, 12, 5, 3, 1], 15))

# ---

# def solve(s):
#   """
#   s: positive integer, what the sum should add up to

#   Solves the following optimization problem:
#     x1 + x2 + x3 + x4 is minimized
#     subject to the constraint x1*25 + x2*10 + x3*5 + x4 = s
#     and that x1, x2, x3, x4 are non-negative integers.
#   Returns a list of the coefficients x1, x2, x3, x4 in that order
#   """
#   tempS = s
#   counter = [0, 0, 0, 0]

#   if tempS // 25:
#     multiplier = tempS // 25
#     counter[0] += multiplier
#     tempS -= 25 * multiplier

#   if tempS // 10:
#     multiplier = tempS // 10
#     counter[1] += multiplier
#     tempS -= 10 * multiplier

#   if tempS // 5:
#     multiplier = tempS // 5
#     counter[2] += multiplier
#     tempS -= 5 * multiplier

#   if tempS // 1:
#     multiplier = tempS // 1
#     counter[3] += multiplier
#     tempS -= 1 * multiplier

#   return counter

# print(solve(22))

#  ---

# def solveit(test):
#     source_lines = []
#     try:
#         # Try to open the source file and read the lines
#         with open(test.__code__.co_filename, 'r') as source_file:
#             source_lines = source_file.readlines()
#     except Exception as e:
#         print(f"Error reading source file: {e}")

#     # Print the source code
#     print(f"The source code of {test.__name__} is:")
#     for line in source_lines:
#         print(line.strip())



# #### This test case prints 49 ####
# def f(x):
#   return (x+15)**0.5 + x**0.5 == 15
# print(solveit(f))

# #### This test case prints 0 ####
# def f(x):
#   return x == 0
# print(solveit(f))

#  ---

# newL = [1, 2, 3]

# for n in newL:
#   for i in newL:
#     print(n,i)

#  ---

