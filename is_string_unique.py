'''Implement an algorithm to determine if a string has all unique characters. What if you cannot use additional data structures ?

-------------
First Attempt
-------------'''
  
word = 'pacolteriA'

def isUnique(m,word):
  for letter in word:
    if m == letter:
      return True

def isuniqueChar(word):
  boolean = False
  for m in range(len(word)):
    word2 = word[m+1:]
    if isUnique(word[m],word2):
      boolean = True
  return boolean

if isuniqueChar(word):
  print('Sorry, this word does not have all unique characters')
else:
  print('String with all unique characters')

  '''In my first attempt I solved the problem through bruteforce with a O(n2) algorithm
  
  --------------
  Second Attempt
  --------------'''
  
word = str(input())

def isUniqueChar2(word):
  if len(word) > 256:
    return False
  char_at = [False] * 256
  for letter in word:
    value = ord(letter)
    if char_at[value]:
      return False
    char_at[value] = True
    print(char_at)
  return True

print(isUniqueChar2(word))

''' After my first attempt I did a search on the boolean Data Structures and learn a new way to store strings'''
