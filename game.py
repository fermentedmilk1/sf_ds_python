"""Game guess the number"""

import numpy as np

number = np.random.randint(1,101) # giving the number

# count tries
count = 0

while True:
    count += 1
    predict_number = int(input('guess the number from 1 to 100: '))
    
    if predict_number > number:
        print('number is smaller!')
        
    elif predict_number < number:
        print('number is bigger!')
        
    else:
        print(f'you guessed the number {number} using {count} tries')
        break