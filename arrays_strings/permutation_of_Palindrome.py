'''Given a string, write a function to check if it is a permutation of a palindrome.

---------
Attempt 1
---------'''
word = str(input('Enter word: '))

def isPalindromePermutation(word):
  arrInt = {}
  i = 0
  for letter in word:
   if letter in arrInt:
     arrInt[letter] += 1
   else:
    arrInt[letter] = 1
  
  for key in arrInt:
    if ((arrInt[key] % 2) != 0) and key is not ' ':
      i += 1
  if i <= 1: 
    return True
  return False
print(isPalindromePermutation(word))
#Complexity of algorithm O(N)
