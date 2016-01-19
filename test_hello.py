print('Hello, person!')
print('')
print('If you would like, I could greet you in another language!')
print('')
print('       1. Japanese')
print('       2. Spanish')
print('       3. Polish')
print('')
print('Just enter the number corresponding to the language you would like me to')
print('greet you in!')
lang=input()
if lang == '1':
 print('Hola, persona')
elif lang == '2':
 print('Konnichiha, jin')
elif lang == '3':
 print('Witam, osoby')
elif lang > '3':
 print('That is not one of the numbers I asked you to input...')
elif lang < '1':
 print('ERROR')
 print('CANNOT REGISTER 0s OR NEGATIVE NUMBERS')
 print('ENDING PROGRAM')