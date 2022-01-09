"""Game guess the number
copmuter is giving and guessing it by himself"""

import numpy as np

def random_predict(number: int = 1) -> int:
    """randomly guessing the number

    Args:
        number (int, optional): given number. Defaults to 1.

    Returns:
        int: amount of tries
    """
    count = 0
    
    while True:
        count += 1
        predict_number = np.random.randint(1,101) # guessed number
        if number == predict_number:
            break # exit cycle when guessed
    return count

def score_game(random_predict) -> int:
    """using how many attempts will computer guess the number

    Args:
        random_predict ([type]): [description]

    Returns:
        int: [description]
    """