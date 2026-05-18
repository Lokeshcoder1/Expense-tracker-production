from src.expense_tracker.models import Expense
import pytest
from datetime import date,timedelta
from decimal import Decimal

def test_expense_creating_successfully():
    expense=Expense(amount=Decimal("190.0"),
                    category="food",
                    description="BreakFast",
                    date=date.today(),
                    id=1
                    )
    assert expense.amount==Decimal("190.0")
    assert expense.id==1

def test_negative_amount_raise_value_error():
    with pytest.raises(ValueError,match="Amount must be positive"):
        Expense(amount=Decimal("-5"),
                category="food",
                description="Lunch",
                date=date.today())

def test_empty_category_raises_error():
    with pytest.raises(ValueError,match="Category cant be empty"):
        Expense(amount=Decimal("100"),
                category=" ",
                description="play",
                date=date.today())

def test_long_description_raises_error():
    with pytest.raises(ValueError,match="Description is too long"):
        long_word="lokesh"*40
        Expense(amount=Decimal("400"),
                category="study",
                description=long_word,
                date=date.today())

def test_future_date_raises_error():
    today=date.today()+timedelta(days=1)
    with pytest.raises(ValueError,match="Date cant be future"):
        Expense(amount=Decimal("100"),
                category="date",
                description="future date",
                date=today)

