from dataclasses import dataclass
from category import Category

@dataclass
class Transaction:
    root : str
    description : str
    category : Category
    value : float

    def show(self):
        print(f"Descrição: {self.description} | Valor: {self.value} | Categoria: {self.category.name}")