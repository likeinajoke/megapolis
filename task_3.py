from csv import *

with open("products.csv", encoding="utf-8-sig") as file:
    reader = list(DictReader(file, delimiter=";", quotechar="'"))

category = input("Введите название категории\n")
min_count = 10 ** 9

while category != "молоко":
    for row in reader:
        if row["Category"] == category:
            min_count = min(min_count, float(row['Count']))
    if min_count == 10 ** 9:
        print('Такой категории не существует в нашей БД')
    else:
        for row in reader:
            if row["Category"] == category and float(row['Count']) == min_count:
                print(f'В категории: {category} товар: {row["product"]} был куплен {int(min_count)} раз')
    category = input("Введите название категории\n")