# Matthew Aaron Marchetti

# write a program that:
# 1. greets the user in English
# 2. asks the user to choose from 1 of 3 spoken languages (pick your favorite languages!) 
# 3. displays the greeting in the chosen language
# 4. exits

# make sure that your code contains comments explaining your logic!

print('Hello, person!')
print('')
print('If you would like, I could greet you in another language!')
print('')
print('       1. Japanese')
print('       2. Spanish')
print('       3. Polish')
print('')
print('Just enter the number corresponding to the language you would like me to')
print('greet you in!')   # All the above greets the user and asks the language they would like to be introduced in.
lang=input() # Waits for the user's input.
if lang == '1': # Checks if the user chose 1, and responds accordingly.
 print('Hola, persona')
elif lang == '2': # Checks if the user chose 2, and responds accordingly.
 print('Konnichiha, jin')
elif lang == '3': # Checks if the user chose 3, and responds accordingly.
 print('Witam, osoby')
elif lang > '3': Checks if the user chose any number above 3, and responds.
 print('That is not one of the numbers I asked you to input...')
elif lang < '1': # Checks if the user chose a 0 or below, and reponds.
 print('ERROR')
 print('CANNOT REGISTER 0s OR NEGATIVE NUMBERS')
 print('ENDING PROGRAM')