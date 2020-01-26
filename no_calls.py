def add(a, b):
  return a + b
  

def add_ten(a):
  return add(a, 10)


def misc_fun():
  return add(add_ten(3), add_ten(9))

import sys

c = 0

import functools
def counted_calls(f):
    @functools.wraps(f)
    def count_wrapper(*args, **kwargs):
        count_wrapper.count += 1
        return f(*args, **kwargs)
    count_wrapper.count = 0
    return count_wrapper 
count = 0
class counter:
    #wraps a function, to keep a running count of how many
    #times it's been called
    def __init__(self, func):
        self.func = func
        self.count = count

    def __call__(self, *args, **kwargs):
        self.count += 1
        return self.func(*args, **kwargs)

def count_calls(func, *args, **kwargs):
  """Count calls in function func"""
  wrapped = counted_calls(func)
  sum_wrapped = counter(func)

#outputs 10
  
  rv = sum_wrapped(*args, **kwargs)
  print(sum_wrapped.count)
  calls = sum_wrapped.count
  return calls, rv

print(count_calls(misc_fun))