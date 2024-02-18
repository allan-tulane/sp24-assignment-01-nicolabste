"""
CMPS 2200  Assignment 1.
See assignment-01.pdf for details.
"""
# no imports needed.

def foo(x):
    if x <= 1:
      return x
    else:
      ra = foo(x - 1)
      rb = foo(x - 2)
      return ra + rb
      
def longest_run(mylist, key):
    current_count = 0

    for num in mylist:
        if num == key:
            current_count += 1
            max_count = max(max_count, current_count)
        else:
            current_count = 0

    return max_count

class Result:
    """ done """
    def __init__(self, left_size, right_size, longest_size, is_entire_range):
        self.left_size = left_size               # run on left side of input
        self.right_size = right_size             # run on right side of input
        self.longest_size = longest_size         # longest run in input
        self.is_entire_range = is_entire_range   # True if the entire input matches the key
        
    def __repr__(self):
        return('longest_size=%d left_size=%d right_size=%d is_entire_range=%s' %
              (self.longest_size, self.left_size, self.right_size, self.is_entire_range))
    

def to_value(v):
    """
    if it is a Result object, return longest_size.
    else return v
    """
    if type(v) == Result:
        return v.longest_size
    else:
        return int(v)
        
def longest_run_recursive(mylist, key):
    def helper(start, end):
        if start == end:
            return Result(0, 0, 0, mylist[start] == key)

        mid = (start + end) // 2
        left_result = helper(start, mid)
        right_result = helper(mid + 1, end)

        left_size = left_result.left_size
        right_size = right_result.right_size

        if mylist[mid] == key:
            left_size += left_result.right_size
            right_size += right_result.left_size

        longest_size = max(left_result.longest_size, right_result.longest_size, left_size, right_size)
        is_entire_range = left_result.is_entire_range and right_result.is_entire_range and \
                          left_result.right_size + right_result.left_size >= longest_size

        return Result(left_size, right_size, longest_size, is_entire_range)

    return helper(0, len(mylist) - 1).longest_size



