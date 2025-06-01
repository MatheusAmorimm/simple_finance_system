from category import Category
from transaction import Transaction

cat_list = list()
transc_list = list()

def register_cat(name):
    new_category = Category(name)
    cat_list.append(new_category)
    return new_category

def register_transc(root, desc, cat, value):
    new_transaction = Transaction(root, desc, cat, value)
    transc_list.append(new_transaction)
    return new_transaction

def wallet():
    total = 0

    for transaction in transc_list:
        total += transaction.valor

    return total