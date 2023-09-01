def first_repeated_value(list):
  # create a Set to keep track of values we've seen
  number_set = set()
  # iterate over each element from the list
  for i in range(0, len(list)):

    # if we've already seen a value, we've found the duplicate!
    if list[i] in number_set:
        return list[i]
    else:
        print("what")

print(first_repeated_value([3,3,4,5,6,6,7,7]))

