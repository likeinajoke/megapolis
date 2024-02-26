from csv import *
from string import *

def promo_gen(product, Date):
    """Функция promo_gen генериует промокод по заданному в задании алгоритму на основе переданных в неё знгачений


            product - название продукта
            Date - дата постулпения продукта


    """
    Date = Date.split(".")
    return product[:2] + Date[0] + product[-2:][::-1] + Date[1][::-1]


with open('products.csv', encoding='utf-8-sig') as file:
    reader = list(DictReader(file, delimiter=';', quotechar="'"))

product_promo = []
for row in reader:
    row["promocode"] = promo_gen(row['product'], row['Date'])
    product_promo.append(row)



