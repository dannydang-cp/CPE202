def max_list_iter(int_list):
   """finds the max of a list of numbers and returns the value (not the index)
   If int_list is empty, returns None. If list is None, raises ValueError"""
   if int_list is None:
      raise ValueError
   else:
      max = int_list[0]
      for x in int_list:
         if x > max:
            max = x
      return max


def reverse_rec(int_list):   # must use recursion
   """recursively reverses a list of numbers and returns the reversed list
   If list is None, raises ValueError"""
   if int_list is None:
      raise ValueError
   elif len(int_list) == 0:
      return []
   else:
      return [int_list[-1]] + reverse_rec(int_list[:-1])


def bin_search(target, low, high, int_list):  # must use recursion
   """searches for target in int_list[low..high] and returns index if found"""
   """If target is not found returns None. If list is None, raises ValueError"""
   if int_list is None:
      raise ValueError

   elif high < low:
      raise ValueError

   else:
      mid = (high + low) // 2

      if int_list[mid] == target:
         return mid
      elif int_list[mid] > target:
         return bin_search(target, low, mid - 1, int_list)
      else:
         return bin_search(target, mid + 1, high, int_list)

