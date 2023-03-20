# | Задание 44 |
# | --- |
# | В ячейке ниже представлен код генерирующий DataFrame, которая состоит всего из 1 столбца. Ваша задача перевести его в one hot вид. Сможете ли вы это сделать без get_dummies?

# import random
# lst = ['robot'] * 10
# lst += ['human'] * 10
# random.shuffle(lst)
# data = pd.DataFrame({'whoAmI'lst})
# data.head() |


import pandas as pd
import random
lst = ['robot'] * 10
lst += ['human'] * 10
random.shuffle(lst)
data = pd.DataFrame({'whoAmI':lst})
# создаём пустой словарь
new_data = {}
# из колонки whoAmI выбираем уникальные значения и проходимся по всем строкам в поиске совпадений
for who in set(data['whoAmI']):
    new_data[who] = [1 if x == who else 0 for x in data['whoAmI']]
# создаем новый датасет
dummies = pd.DataFrame(new_data)
print(dummies)