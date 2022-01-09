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
        random_predict ([type]): guessing function

    Returns:
        int: mean of try counts
    """
    count_ls = [] # список для сохранения количества попыток
    np.random.seed(1) # фиксируем сид для воcпроизводимости
    random_array = np.random.randint(1, 101, size=(1000)) # загадали список чисел

    for number in random_array:
        count_ls.append(random_predict(number))

    score = int(np.mean(count_ls)) # находим среднее количество попыток

    print(f'Ваш алгоритм угадывает число в среднем за: {score} попыток')
    return(score)

# RUN
score_game(random_predict)