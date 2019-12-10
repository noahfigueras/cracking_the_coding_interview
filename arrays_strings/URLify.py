'''Write a method to replace all spaces in a string with '%20' 

---------
Attempt 1
---------'''

word = str(input('Enter sentence to urlify: '))

def URLify(word):
  newWord = ''
  for letter in word:
    if letter == ' ':
      letter = '%20'
    newWord += letter
  return newWord

print(URLify(word))
#Complexity of algorithm O(N)
