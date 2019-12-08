'''Implement an algorithm to determine if a string has all unique characters. What if you cannot use additional data structures ?'''
import string

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
