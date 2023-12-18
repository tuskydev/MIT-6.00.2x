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

import random


class Lecture(object):
  def __init__(self, listen, sleep, fb):
    self.listen = listen
    self.sleep = sleep
    self.fb = fb
  def get_listen_prob(self):
    return self.listen
  def get_sleep_prob(self):
    return self.sleep
  def get_fb_prob(self):
    return self.fb

def get_mean_and_std(X):
  mean = sum(X)/float(len(X))
  tot = 0.0
  for x in X:
    tot += (x - mean)**2
  std = (tot/len(X))**0.5
  return mean, std

def lecture_activities(N, aLecture):
  '''
  N: integer, number of trials to run
  aLecture: Lecture object

  Runs a Monte Carlo simulation N times.
  Returns: a tuple, (float, float)
            Where the first float represents the mean number of lectures it takes 
            to have a lecture in which all 3 activities take place,
            And the second float represents the total width of the 95% confidence 
            interval around that mean.
  '''
  # IMPLEMENT THIS FUNCTION


# sample test cases
a = Lecture(1, 1, 1)
print(lecture_activities(100, a))
# the above test should print out (1.0, 0.0)

b = Lecture(1, 1, 0.5)
print(lecture_activities(100000, b))
# the above test should print out something reasonably close to (2.0, 5.516)