from pathlib import Path
from .models import Expense
from typing import List
from decimal import Decimal
import json
from datetime import date
import logging

logger=logging.getLogger(__name__)
class JSONStorage:
    def __init__(self,filepath:Path):
        self.filepath=filepath

    def save(self,expenses:List[Expense]) -> None:
        try:
            data=[]
            for exp in expenses:
                expense={'id':exp.id,
                    'amount':str(Decimal(exp.amount)),
                    'category':exp.category,
                    'description':exp.description,
                    'date':exp.date.isoformat()}
                data.append(expense)
            with open(self.filepath,'w',encoding='utf-8') as f:
                json.dump(data,f,indent=2)
                logger.info(f"Expenses {len(expenses)} are saved to {self.filepath}successfully!")
        except OSError as e:
            logger.error(f"Failed to save to this file {self.filepath}")

    def load(self)->List[Expense]:
        if not self.filepath.exists():
            logger.info(f"Failed to load the file {self.filepath} starting refresh with empty list ")
            return []
        expenses=[]
        try:
            with open (self.filepath,'r') as f:
                data=json.load(f)
                for item in data:
                    required={"id","amount","category","description","date"}
                    if not required.issubset(item.keys()):
                        raise ValueError(f"Missing keys in {item}")
                    expense=Expense(
                        id=item['id'],
                        amount=Decimal(item['amount']),
                        category=item['category'],
                        description=item['description'],
                        date=date.fromisoformat(item['date'])
                    )
                    expenses.append(expense)
                    logger.info(f"Loaded expenses from {self.filepath} is successful!")
                    return expenses
        except (json.JSONDecodeError,ValueError,KeyError) as e :
            logger.error(f"Failed to fetch the details issue {e}")
            return []


