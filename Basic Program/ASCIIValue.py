# Program to print ASCII Value of a character

print('ASCII for input')
word = input('Enter the word : ')
print('-'*60)
print('You entered ', word)

for (index, char) in enumerate(word):
    print(f'{index}.  {char} : {ord(char)} ')
