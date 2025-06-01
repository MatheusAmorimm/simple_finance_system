from utils import (register_cat, register_transc, wallet)

#create categories
revenue = register_cat('Receitas')
bills = register_cat('Despesas')
courses = register_cat('Cursos')

#create transactions
register_transc(
    'Estagio',
    'Salario do estagio',
    revenue.name,
    2700
)

register_transc(
    'Curso Pyhton/C#/JAVA',
    'Curso completo de prog, com foco em algoritimos',
    courses.name,
    -1000

)

register_transc(
    'Aluguel',
    'Pagamento do alguel jul/25',
    bills.name,
    -1600
)

total = wallet()

print(f"Your balance: {total}")