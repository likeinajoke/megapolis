from csv import *

with open("products.csv", encoding="utf-8-sig") as file:
    reader = list(DictReader(file, delimiter=";", quotechar="'"))

products_new = []
for row in reader:
    row['total'] = float(row['Price per unit']) * float(row['Count'])
    products_new.append(row)

total_sum_zakuski = 0
for row in products_new:
    if row["Category"] == "Закуски":
        total_sum_zakuski += float(row['total'])
print(total_sum_zakuski)


with open("proucts_new.csv", "w", encoding="utf-8-sig") as file:
    file = DictWriter(delimiter=';', fieldnames=['Category', 'product', 'Date', 'Price per unit', 'Count', 'total'])
    file.writeheader('Category;product;Date;Price per unit;Count;total')
    file.writerows(products_new)