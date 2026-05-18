from .storage import JSONStorage
from typing import List
from decimal import Decimal
from .models import Expense
from datetime import date
import logging

logger=logging.getLogger(__name__)

class ExpenseTracker:
    def __init__(self,storage:JSONStorage):
        self._storage=storage
        self._expenses:List[Expense]=[]
        self._next_id:int=1
        self._load()

    def _load(self):
        self._expenses=self._storage.load()
        if self._expenses:
            self._next_id=max(e.id for e in self._expenses)+1
            logger.debug(f"Next id is {self._next_id}")
        else:
            logger.info("No expenses found in exists")

    def add_expense(self,
                    amount:Decimal,
                    category:str,
                    description:str,
                    expense_date:date)->Expense:
        expense=Expense(
            id=self._next_id,
            amount=amount,
            category=category,
            description=description,
            date=expense_date
        )
        self._expenses.append(expense)
        self._next_id+=1
        logger.info(f"New expense is added with id {self._next_id}")
        self._storage.save(self._expenses)
        return expense

    def get_all(self):
        return self._expenses.copy()

    def remove_expense(self,expense_id:int):
        original_len=len(self._expenses)
        self._expenses=[e for e in self._expenses if e.id!=expense_id]
        if original_len>len(self._expenses):
            logger.info(f"Expense {expense_id} is removed is successful")
            self._storage.save(self._expenses)
            return True
        logger.warning(f"Expense id {expense_id} not found")
        return False


