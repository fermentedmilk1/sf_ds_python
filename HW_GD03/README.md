# Homework GD3: analyze Quiz Freeze 

## Outline
[1. Project description](https://github.com/fermentedmilk1/sf_ds_python/blob/main/HW_GD3/README.md#project-description)

[2. What is the objective?](https://github.com/fermentedmilk1/sf_ds_python/blob/main/HW_GD3/README.md#objective)

[3. Info about data](https://github.com/fermentedmilk1/sf_ds_python/blob/main/HW_GD3/README.md#data)

[4. Work steps](https://github.com/fermentedmilk1/sf_ds_python/blob/main/HW_GD3/README.md#steps)

[5. Results](https://github.com/fermentedmilk1/sf_ds_python/blob/main/HW_GD3/README.md#results)

[6. Summary](https://github.com/fermentedmilk1/sf_ds_python/blob/main/HW_GD3/README.md#summary)

### Project description
game to guess a number given by computer using minimum amount of tries

[&#8593; go to outline](https://github.com/fermentedmilk1/sf_ds_python/blob/main/HW_GD3/README.md#outline)

### Цель
Исследовать поведение пользователей в обновлённом приложении.

**Задачи**
1. Понять, как пользователи взаимодействуют с продуктом, и соотнести идеальный путь пользователей с фактическим.
2. Выявить этапы, которые занимают больше всего времени, с тем чтобы поработать над их улучшением.
3. Проанализировать зависимость оплат от прохождения обучения.

**Формализованные задачи**

1. Определить самые распространённые пути прохождения (последовательности) этапов в приложении.
2. Посмотреть на среднее время между различными этапами и выделить самые большие временные промежутки.
3. Определить, существует ли различие в частоте и средней величине оплат между тремя группами пользователей:
    - пользователями, которые прошли обучение хотя бы раз;
    - пользователями, которые начали обучение, но не прошли его ни разу;
    - пользователями, которые не начинали обучение, а сразу же перешли к выбору уровня сложности.

**Дополнительная информация**

Поскольку вам предстоит анализировать пути прохождения пользователей по этапам игры, неплохо было бы знать, из каких именно этапов состоит Quiz Freeze:
1. регистрация
2. старт обучения
3. конец обучения
4. выбор уровня сложности
5. выбор пакетов вопросов
6. покупка платных вопросов

[&#8593; go to outline](https://github.com/fermentedmilk1/sf_ds_python/blob/main/Project_0/README.md#outline)

### Данные

**Таблица Event**

Хранит данные о событиях, которые совершают пользователи. По сути, каждое событие — это факт прохождения пользователем какого-либо этапа игры.
 - **id** идентификатор события
 - **user_id** уникальный идентификатор пользователя, совершившего событие в приложении
 - **start_time** дата и время события
 - **event_type** тип события (значения: registration — регистрация; tutorial_start — начало обучения; tutorial_finish — завершение обучения; level_choice — выбор уровня сложности; pack_choice — выбор пакетов вопросов)
 - **tutorial_id** идентификатор обучения (этот идентификатор есть только у событий обучения)
 - **selected_level** выбранный уровень сложности обучения

**Таблица purchase**

Хранит данные об оплатах, которые совершают пользователи.
Название поля 	Описание
 - **id** идентификатор события
 - **user_id** уникальный идентификатор пользователя, совершившего событие в приложении
 - **event_datetime** дата и время события/покупки
 - **amount** сумма оплаты

[&#8593; go to outline](https://github.com/fermentedmilk1/sf_ds_python/blob/main/Project_0/README.md#outline)

### Шаги

1. **Проверка данных на целостность**

[&#8593; go to outline](https://github.com/fermentedmilk1/sf_ds_python/blob/main/Project_0/README.md#outline)

### Results 

n/a

[&#8593; go to outline](https://github.com/fermentedmilk1/sf_ds_python/blob/main/Project_0/README.md#outline)

### Summary

n/a

[&#8593; go to outline](https://github.com/fermentedmilk1/sf_ds_python/blob/main/Project_0/README.md#outline)