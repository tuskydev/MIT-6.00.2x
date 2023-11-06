kvlist = [['Betsy', 9], ['Henrietta', 9], ['Herman', 7], ['Oreo', 6], ['Millie', 5], ['Maggie', 3], ['Moo Moo', 3], ['Milkshake', 2], ['Lola', 2], ['Florence', 2]]

kvlist = sorted(kvlist, key=lambda x: -x[1])

indexToRemove = kvlist[0].index("Betsy")

print(indexToRemove)
