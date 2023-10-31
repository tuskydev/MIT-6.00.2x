## MIT 6.00.2x Code below:

# ---

# print("Hello world!")

#  ---

NUMBER = 3
def look_for_things(myList):
    """Looks at all elements"""
    for n in myList:
      if n == NUMBER:
        return True
    return False

# ---

# NUMBER = 3
# def look_for_other_things(myList):
#   """Looks at all pairs of elements"""
#   for n in myList:
#     for m in myList:
#       if n - m == NUMBER or m - n == NUMBER:
#         return True
#   return False

#  ---

# def get_all_subsets(some_list):
#   """Returns all subsets of size 0 - len(some_list) for some_list"""
#   if len(some_list) == 0:
#     # If the list is empty, return the empty list
#     return [[]]
#   subsets = []
#   first_elt = some_list[0]
#   rest_list = some_list[1:]
#   # Strategy: Get all the subsets of rest_list; for each
#   # of those subsets, a full subset list will contain both
#   # the original subset as well as a version of the subset
#   # that contains first_elt
#   for partial_subset in get_all_subsets(rest_list):
#     subsets.append(partial_subset)
#     next_subset = partial_subset[:] + [first_elt]
#     subsets.append(next_subset)
#   return subsets

# NUMBER = 3
# def look_for_all_the_things(myList):
#   """Looks at all subsets of this list"""
#   # Make subsets
#   all_subsets = get_all_subsets(myList)
#   for subset in all_subsets:
#     if sum(subset) == NUMBER:
#       return True
#   return False

# print(look_for_all_the_things([1,2,4]))

# ---

# print(1%2)

# ---

# generate all combinations of N items
def powerSet(items):
  N = len(items)
  # enumerate the 2**N possible combinations
  for i in range(2**N):
    combo = []
    for j in range(N):
      # test bit jth of integer i
      if (i >> j) % 2 == 1:
        # print("THIS IS IT: ", i, j)
        combo.append(items[j])
    yield combo

def yieldAllCombos(items):
  """
    Generates all combinations of N items into two bags, whereby each
    item is in one or zero bags.

    Yields a tuple, (bag1, bag2), where each bag is represented as
    a list of which item(s) are in each bag.
  """



for blunt in powerSet([1,2,3]):
  print("this is blunt,", blunt)
