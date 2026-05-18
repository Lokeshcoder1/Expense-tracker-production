from dataclasses import dataclass
from datetime import date
from decimal import Decimal
from typing import Optional

@dataclass
class Expense:

    amount:Decimal
    category:str
    description:str
    date:date
    id:Optional[int]=None

    def __post_init__(self):
        self.validate()

    def validate(self):
        if self.amount<=0:
            raise ValueError("Amount must be positive")
        if self.amount>1_000_000:
            raise ValueError("Amount must be below 1_000_000")
        if not self.category or not self.category.strip():
            raise ValueError("Category cant be empty")
        if len(self.category)>=50:
            raise ValueError("category is too long ")
        if not self.description or not self.description.strip():
            raise ValueError("Description cant be empty")
        if len(self.description)>=200:
            raise ValueError("Description is too long")
        if self.date>date.today():
            raise ValueError("Date cant be future")





