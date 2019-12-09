'''Given two strings, write a method to decide if one is a permutation of the other

---------
Attempt 1
---------'''

word1 = str(input('Enter first word: '))
word2 = str(input('Enter second word: '))

def hasPermutation(word1,word2):
  if len(word1) == len(word2):
    for letter in word1:
      word2 = word2.replace(letter,'')
    if len(word2) <= 0:
      return True
  return False

print(hasPermutation(word1,word2))

#Complexity of algorithm O(N)
