'''
How could you use a single array to implement three stacks?
'''
'''
I can use a single array with three other arrays each of one as a stack. In this case I would be able to remove the last element with pop() and insert on the end of eahc stack with append()
'''

arr = [[1,2,3,4],[2,3,4],[3,4]]

def pop(i):
  i -= 1
  arr[i].pop()

def push(list,insert):
  i = list -1
  arr[i].append(insert)
