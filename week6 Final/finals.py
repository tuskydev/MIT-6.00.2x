# import random, pylab


# xVals = []
# yVals = []
# wVals = []
# for i in range(1000):
#     xVals.append(random.random())
#     yVals.append(random.random())
#     wVals.append(random.random())
# xVals = pylab.array(xVals)
# yVals = pylab.array(yVals)
# wVals = pylab.array(wVals)
# twoTimesxVals = xVals + xVals
# zVals = twoTimesxVals + yVals
# tVals = twoTimesxVals + yVals + wVals

# pylab.plot(sorted(xVals), sorted(yVals))
# pylab.show()

#  ---

# import random


# class Lecture(object):
#   def __init__(self, listen, sleep, fb):
#     self.listen = listen
#     self.sleep = sleep
#     self.fb = fb
#   def get_listen_prob(self):
#     return self.listen
#   def get_sleep_prob(self):
#     return self.sleep
#   def get_fb_prob(self):
#     return self.fb

# def get_mean_and_std(X):
#   mean = sum(X)/float(len(X))
#   tot = 0.0
#   for x in X:
#     tot += (x - mean)**2
#   std = (tot/len(X))**0.5
#   return mean, std

# def lecture_activities(N, aLecture):
#   '''
#   N: integer, number of trials to run
#   aLecture: Lecture object

#   Runs a Monte Carlo simulation N times.
#   Returns: a tuple, (float, float)
#             Where the first float represents the mean number of lectures it takes
#             to have a lecture in which all 3 activities take place,
#             And the second float represents the total width of the 95% confidence
#             interval around that mean.
#   '''
#   success = []
#   tries = 1

#   for _ in range(N):

#     if random.random() < aLecture.get_listen_prob() \
#             and random.random() < aLecture.get_sleep_prob() \
#             and random.random() < aLecture.get_fb_prob():
#       success.append(tries)
#       tries = 1
#     else:
#       tries += 1

#   # Calculate the total width for 95% interval around the mean
#   mean, std = get_mean_and_std(success)
#   Z = 1.96
#   width = Z*std*2

#   return (mean, width)



# # sample test cases
# a = Lecture(1, 1, 1)
# print(lecture_activities(100, a))
# # the above test should print out (1.0, 0.0)

# b = Lecture(1, 1, 0.5)
# print(lecture_activities(100000, b))
# # the above test should print out something reasonably close to (2.0, 5.516)

#  ---

# import random, pylab


# # You are given this function
# def getMeanAndStd(X):
#   mean = sum(X)/float(len(X))
#   tot = 0.0
#   for x in X:
#     tot += (x - mean)**2
#   std = (tot/len(X))**0.5
#   return mean, std

# # You are given this class
# class Die(object):
#   def __init__(self, valList):
#     """ valList is not empty """
#     self.possibleVals = valList[:]
#   def roll(self):
#     return random.choice(self.possibleVals)

# # Implement this -- Coding Part 1 of 2
# def makeHistogram(values, numBins, xLabel, yLabel, title=None):
#   """
#   - values, a sequence of numbers
#   - numBins, a positive int
#   - xLabel, yLabel, title, are strings
#   - Produces a histogram of values with numBins bins and the indicated labels
#     for the x and y axis
#   - If title is provided by caller, puts that title on the figure and otherwise
#     does not title the figure
#   """
#   if title:
#     pylab.title(title)

#   pylab.hist(values, numBins)
#   pylab.xlabel(xLabel)
#   pylab.ylabel(yLabel)
#   pylab.show()

# # Personal test case
# # makeHistogram([1,2], 4, "Aaa", "Bbb")

# # Implement this -- Coding Part 2 of 2
# def getAverage(die, numRolls, numTrials):
#   """
#   - die, a Die
#   - numRolls, numTrials, are positive ints
#   - Calculates the expected mean value of the longest run of a number
#     over numTrials runs of numRolls rolls
#   - Calls makeHistogram to produce a histogram of the longest runs for all
#     the trials. There should be 10 bins in the histogram
#   - Choose appropriate labels for the x and y axes.
#   - Returns the mean calculated
#   """
#   results = []
#   for _ in range(numTrials):
#     currTrial = []
#     longestCurrStreak = []
#     highestStreak = 0

#     # Rolling dice for one trial
#     for _ in range(numRolls):
#       currTrial.append(die.roll())

#     # Indexing longest streak
#     for index, roll in enumerate(currTrial):
#       if len(longestCurrStreak) == 0:
#         longestCurrStreak.append(roll)
#         longestCurrStreak.append(1)
#         highestStreak = longestCurrStreak[1]
#         continue
#       # Same roll in a row
#       if longestCurrStreak[0] == roll:
#         longestCurrStreak[1] += 1
#       # New roll, and check if the longestCurrStreak is higher than highestStreak
#       else:
#         if highestStreak < longestCurrStreak[1]:
#           highestStreak = longestCurrStreak[1]
#         longestCurrStreak[0] = roll
#         longestCurrStreak[1] = 1
#       # Edge case where we're still on a streak but loop ends
#       if index+1 == len(currTrial):
#         if highestStreak < longestCurrStreak[1]:
#           highestStreak = longestCurrStreak[1]

#     results.append(highestStreak)

#   makeHistogram(results, 10, "Length of Longest Run", "Frequency", "Highest streak for dice roll experimentation")

#   return sum(results)/float(len(results))


# # One test case
# # print(getAverage(Die([1,2,3,4,5,6,6,6,7]), 500, 10000))
# print(getAverage(Die([1,2,3,4,5,6,6,6,7]), 1, 1000))

#  ---

# import numpy as np

# def find_combination(choices, total):
#   """
#   choices: a non-empty list of ints
#   total: a positive int

#   Returns result, a numpy.array of length len(choices)
#   such that
#     * each element of result is 0 or 1
#     * sum(result*choices) == total
#     * sum(result) is as small as possible
#   In case of ties, returns any result that works.
#   If there is no result that gives the exact total,
#   pick the one that gives sum(result*choices) closest
#   to total without going over.
#   """
#   num_choices = len(choices)

#   # Generate all possible binary combinations
#   binary_combinations = [np.array(list(bin(i)[2:].zfill(num_choices)), dtype=int) for i in range(2**num_choices)]

#   # Filter combinations that satisfy the sum condition
#   valid_combinations = [comb for comb in binary_combinations if np.sum(comb * choices) == total]

#   if not valid_combinations:
#     # If there is no exact match, find the closest sum without going over
#     closest_sum = 0
#     closest_combination = None

#     for comb in binary_combinations:
#       current_sum = np.sum(comb * choices)
#       if current_sum <= total and current_sum >= closest_sum:
#         closest_sum = current_sum
#         closest_combination = comb

#     return closest_combination

#   # Sort valid combinations based on the sum of 1s (smallest sum first)
#   valid_combinations.sort(key=lambda x: np.sum(x))

#   # Return the one with the smallest sum
#   return valid_combinations[0]

# # Test cases
# print(find_combination([1,2,2,3], 4))  # [1 0 0 1] or [0 1 1 0]
# print(find_combination([1,1,3,5,3], 5))  # [0 0 0 1 0]
# print(find_combination([1,1,1,9], 4))  # [1 1 1 0]

# ---

import random
import pylab


# Global Variables
MAXRABBITPOP = 1000
CURRENTRABBITPOP = 500
CURRENTFOXPOP = 30

def rabbitGrowth():
  """
  rabbitGrowth is called once at the beginning of each time step.

  It makes use of the global variables: CURRENTRABBITPOP and MAXRABBITPOP.

  The global variable CURRENTRABBITPOP is modified by this procedure.

  For each rabbit, based on the probabilities in the problem set write-up,
  a new rabbit may be born.
  Nothing is returned.
  """
  # you need this line for modifying global variables
  global CURRENTRABBITPOP

  # TO DO
  pass

def foxGrowth():
  """
  foxGrowth is called once at the end of each time step.

  It makes use of the global variables: CURRENTFOXPOP and CURRENTRABBITPOP,
    and both may be modified by this procedure.

  Each fox, based on the probabilities in the problem statement, may eat
  one rabbit (but only if there are more than 10 rabbits).

  If it eats a rabbit, then with a 1/3 prob it gives birth to a new fox.

  If it does not eat a rabbit, then with a 1/10 prob it dies.

  Nothing is returned.
  """
  # you need these lines for modifying global variables
  global CURRENTRABBITPOP
  global CURRENTFOXPOP

  # TO DO
  pass

def runSimulation(numSteps):
  """
  Runs the simulation for `numSteps` time steps.

  Returns a tuple of two lists: (rabbit_populations, fox_populations)
  where rabbit_populations is a record of the rabbit population at the
  END of each time step, and fox_populations is a record of the fox population
  at the END of each time step.

  Both lists should be `numSteps` items long.
  """

  # TO DO
  pass

