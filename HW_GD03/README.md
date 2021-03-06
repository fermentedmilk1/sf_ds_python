# Homework GD3: analyze Quiz Freeze 

## Outline
[1. Project description](https://github.com/fermentedmilk1/sf_ds_python/blob/main/HW_GD03/README.md#project-description)

[2. What is the objective?](https://github.com/fermentedmilk1/sf_ds_python/blob/main/HW_GD03/README.md#objective)

[3. Info about data](https://github.com/fermentedmilk1/sf_ds_python/blob/main/HW_GD03/README.md#data)

[4. Work steps](https://github.com/fermentedmilk1/sf_ds_python/blob/main/HW_GD03/README.md#steps)

[5. Results](https://github.com/fermentedmilk1/sf_ds_python/blob/main/HW_GD03/README.md#results)

[6. Summary](https://github.com/fermentedmilk1/sf_ds_python/blob/main/HW_GD03/README.md#summary)

### Project description
Это исследование позволит понять, как пользователи пользуются приложением, и сравнить фактический путь пользователей с тем, который был задуман при разработке приложения.

Когда мы поймём, какие этапы занимают больше всего времени, мы выясним, что требует оптимизации.

[&#8593; go to outline](https://github.com/fermentedmilk1/sf_ds_python/blob/main/HW_GD03/README.md#outline)

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

[&#8593; go to outline](https://github.com/fermentedmilk1/sf_ds_python/blob/main/HW_GD03/README.md#outline)

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

[&#8593; go to outline](https://github.com/fermentedmilk1/sf_ds_python/blob/main/HW_GD03/README.md#outline)

### Шаги

**1. Отфильтровать данные пользователей зарегистрировавшихся в 2018 году**

фильтрацию проводим в два этапа: 
 - выделим пользователей, зарегистрированных в 2018 г.
 - оставим в датафрейме только этих пользователей и все их действия уже без привязки к году

**2. Проверка данных на целостность**

 - исследуем пропуски:

Наличие пропущенных строк обусловлено тем, что не все из параметров selected_level и tutorial_id присутствуют в каждом из событий. Эти параметры заполнятся в зависимости от event_type. К примеру, посмотрим на events_df, оставив в нём только такие строки, где event_type = level_choice. Этот срез датафрейма не содержит пропущенных значений в столбце selected_level, но зато содержит пропуски в tutorial_id. Это связано с тем, что для событий типа level_choice не предусмотрена запись параметра tutorial_id.

Теперь проверим аналогичные данные, но при условии, что срез будет содержать данные о событиях tutorial_start и tutorial_finish. Столбец selected_level в таком срезе не содержит ни одного значения.  Причина этого в том, что для событий, связанных с обучением, отсутствуют параметры выбора уровня сложности selected_level. А вот остальные столбцы заполнены полностью.

 - исследуем значения

 количество событий регистрация, выбор уровня, выбор бесплатных вопросов и покупка - по одному на каждого пользователя

 количество событий старта и завершения обучения - может быть больше 1 на пользователя

**3. Анализ данных**

*3.1. Анализ пользовательских событий*

Для того чтобы понимать, как пользователи переходят из этапа в этап и на каких из них возникают сложности, мы должны определить конверсию на каждом из этапов воронки. То есть нам нужно понять, какой процент пользователей переходит с предыдущего этапа на следующий. 

1. Registration: как мы видим, все пользователи совершают событие registration. Это обусловлено тем, что данный этап является обязательным для выполнения и без него пользователь не сможет перейти дальше.

2. Tutorial_start: процент пользователей, начавших обучение (от общего числа зарегистрировавшихся): 59.51%

3. Tutorial_finish: процент пользователей, завершивших обучение: 86.44%. В нашем приложении достаточно хороший процент прохождения обучения. Но есть куда стремиться для его увеличения.

4. Level_choice: процент пользователей, выбравших уровень сложности тренировок (от общего числа зарегистрировавшихся): 41.86%. Меньше половины пользователей (41.76 %) доходят до этапа выбора уровня сложности вопросов. А ведь этот этап напрямую влияет на то, что пользователь будет пользоваться приложением через бесплатные возможности, которые в дальнейшем могут привести к оплате. Таким образом, для успешной монетизации приложения крайне важно оптимизировать прохождение до этапа выбора сложности.

5. Pack_choice: процент пользователей, выбравших набор бесплатных вопросов (от числа пользователей, которые выбрали уровень сложности): 68.77%

6. Purchase: процент пользователей, которые оплатили вопросы (от числа зарегистрировавшихся пользователей): 8.03%. Процент пользователей, которые оплатили вопросы (от числа пользователей, которые выбрали тренировки): 27.89%.

*3.2. Анализ уникальных пользовательских путей*

Наша воронка достаточно предсказуемая: почти все этапы идут последовательно друг за другом. Однако нужно иметь в виду один нюанс: есть пользователи, которые не начинают обучение, есть такие, кто его не заканчивает, а есть те, кто проходят его по несколько раз.

    Отследив уникальные пользовательские пути, мы можем визуально оценить, какие успешные пути существуют, 
    а также заметить девиации (например, если у нас будет много путей с очень частым началом обучения).

Чтобы понимать, какие есть различные последовательности прохождения пользователей по воронке и насколько часто они встречаются, можно воспользоваться таким подходом:

     - отсортировать все события по возрастанию во времени;
     - объединить для каждого пользователя все его события в один список;
     - подсчитать частоту различных списков.

Сначала нужно сформировать выборку, в которой объединены события и покупки. Потом каждого пользователя создать список, который будет содержать во временной последовательности все события, совершаемые данным пользователем. Затет выявить наиболее популярные пути.

Среди 10 самых популярных последовательностей только одна содержит этап оплаты. Это последовательность  (1083 пользователей из 1600 совершивших покупки): 

    registration > tutorial_start > tutorial_finish > level_choice > pack_choice > purchase  

Большинство последовательностей, которые содержат в себе оплату, также содержат старт обучения. Это наводит нас на **гипотезу**, что вероятность оплаты зависит от того, проходил ли пользователь обучение.

Проверим это в рамках следующей гипотезы.

*3.3. Анализ временных промежутков*

Этот шаг очень полезен при анализе поведения пользователей. Время между этапами может сообщить нам о вовлечённости пользователей в приложение, а также о роли отдельных этапов на развитие этой вовлечённости. Если окажется, что у пользователей, которые проходят обучение, время до выбора вопросов меньше, чем у тех, кто его не проходит, то разработчикам нужно будет придумывать способы, как вовлекать пользователя в прохождение данного этапа.

    В целом, чем меньше срок до целевого действия (оплаты) в среднем, тем более управляемо наше приложение,
    и, скорее всего, на пути пользователя будет меньше отвлекающих факторов, которые ему помешают совершить
    оплату.

1. Определяем время между registration и tutorial_start

    - четверть пользователей тратит более 1 часа 21 минут на переход от регистрации к началу обучения;
    - половина всех пользователей тратит между регистрацией и началом обучения более 3 часов 22 минут.

2. Определяем время между registration и level_choice

    - четверть пользователей тратит более 3 часа 53 минут на переход от регистрации к выбору уровня;
    - половина всех пользователей тратит между регистрацией и выбором уровня более 6 часов 02 минут.

3. Определяем время между level_choice и Pack_choice

    - четверть пользователей тратит более 3 минут на переход от выбора уровня к бесплатным вопросам;
    - половина всех пользователей тратит между выбором уровня и переходом к бесплатным вопросам более 4 минут;
    - в среднем для всех пользователей проходит более 5 минут между событием выбора уровня сложности до события выбора набора бесплатных вопросов.

4. Определяем время между Pack_choice и purchase

    - четверть пользователей тратит менее 2 дней на переход от бесплатных вопросов к покупке платных;
    - половина всех пользователей тратит более 3,5 дней после перехода к бесплатным вопросам чтобы совершить покупку;
    - в среднем для всех пользователей проходит более 3 дней 17 часов между событием выбора набора бесплатных вопросов и покупкой платных вопросов.

Эта информация может быть полезна в том случае, когда мы сравниваем между собой различные группы пользователей и ищем способы сократить время между этапами.  

**4. Проверка аналитической гипотезы**

На что и каким образом влияет прохождение обучения?

Cуществует ли различие в частоте и средней величине оплат между тремя группами пользователей:

    - пользователи, которые прошли обучение хотя бы раз (10250);
    - пользователи, которые начали обучение, но не прошли его ни разу (1608);
    - пользователи, которые не начинали обучение, а сразу же перешли к выбору уровня сложности (8068).

Процент пользователей, которые оплатили вопросы (от числа пользователей, завершивших обучение): 14.12%
средний размер платежа у пользователей, которые завершили обучение, составляет 110 рублей 99 копейки.

Процент пользователей, которые оплатили вопросы (от числа пользователей, начавших обучение, но не завершивших): 8.15%. средний размер платежа у пользователей, которые начали но не завершили обучение, составляет 104 рублей 96 копейки.

Процент пользователей, которые оплатили вопросы (от числа пользователей, не начавших обучение): 0.27%, средний размер платежа у пользователей, которые не начинали обучение, составляет 128 рублей 41 копейки.

    Как мы видим, процент пользователей, которые завершили обучение и совершили оплату, выше, чем процент
    пользователей, которые не начали обучение или не закончили его.

    Это говорит о том, что факт прохождения обучения влияет на дальнейшую мотивацию использовать
    приложение. Существенной разницы в среднем чеке при этом не наблюдается, то есть обучение увеличивает
    вовлечённость, но выбор количества платных пакетов зависит индивидуально от пользователя.

**5. Исследование поведения пользователей**

в рамках этого исследования нужно ответить на два вопроса:

1. Зависит ли вероятность оплаты от выбранного пользователем уровня сложности? (есть ли зависимость между выбранным уровнем сложности и вероятностью оплаты)
2. Существует ли разница во времени между событиями регистрации и оплаты для разных групп пользователей с разным уровнем сложности? (различается ли временной промежуток между регистрацией и оплатой у групп пользователей с разным уровнем сложности)

- наибольшее количество пользователей (4645 человек) выбрало средний уровень сложности, но им в среднем понадобилось больше всего времени (почти 4 дня) чтобы совершить на покупку.

- наименьшее количество пользователей (1249 человек) выбрало высокий уровень сложности, однако им в среднем понадобилось меньше всего времени (3 дня и 7,35 часа) чтобы совершить покупку.

- те, кто выбрал низкий уровень сложности (примерно треть от всех, кто выбрал уровень сложности) редко совершали покупку: только 7,72 %.

*Вывод: чем выше уровень трудности выбрал пользователь, тем вероятнее что он совершит покупку.*

Существует ли разница во времени между событиями регистрации и оплаты?
- опять же, быстрее всех совершают покупку пользователи, выбравшие высокий уровень сложности (за 3 дня и 15 часов).
- медленнее всех совершают покупку пользователи, выбравшие средний уровень сложности (за 4 дня и 6,2 часов).
- те, кто выбрал низкий уровень сложности совершают покупку в среднем через 3 дня и 22,2 часов после регистрации.

похоже что время между регистрацией и выбором уровня для разных групп различается мало, и в среднем составляет 7 часов и 15 минут

[&#8593; go to outline](https://github.com/fermentedmilk1/sf_ds_python/blob/main/HW_GD03/README.md#outline)

### Results 

n/a

[&#8593; go to outline](https://github.com/fermentedmilk1/sf_ds_python/blob/main/HW_GD03/README.md#outline)

### Summary

n/a

[&#8593; go to outline](https://github.com/fermentedmilk1/sf_ds_python/blob/main/HW_GD03/README.md#outline)