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

L = [10, 9, 8, -1] ## 27
secondNumList=  [3, 4, -8, 15, -1, 2] ##16
thirdList = [3, 4, -1, 5, -4] ## 11
highestCount = 0

max_value = 0
value = 0
for i in range(len(thirdList)):
  print(i)
#   value = value + thirdList[i]
#   if value < 0:
#     value = 0
#   if max_value < value:
#     max_value = value
# print("MAX VLAUE", max_value)

for index, num in enumerate(thirdList):
  for n in range(len(thirdList), 0, -1):
    # print(index, n)
    if index == n:
      break

    currSum = sum(thirdList[index:n])
    if currSum > highestCount:
      highestCount = currSum

print("This is highestCount:", highestCount)

