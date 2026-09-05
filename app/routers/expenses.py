from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database.connection import SessionLocal
from app.models.expense import Expense
from app.schemas.expense import ExpenseCreate, ExpenseUpdate

router = APIRouter(prefix="/expenses", tags=["Expenses"])


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.get("")
def get_expenses(db: Session = Depends(get_db)):
    return db.query(Expense).all()



@router.post("")
def create_expense(expense: ExpenseCreate, db: Session = Depends(get_db)):
    new_expense = Expense(
      
        description=expense.description,
        amount=expense.amount,
        date=expense.date,
        community_id=expense.community_id
)
    

    db.add(new_expense)
    db.commit()
    db.refresh(new_expense)

    return new_expense


@router.delete("/{expense_id}")
def delete_community(expense_id: int, db: Session = Depends(get_db)):
    expense = db.query(Expense).filter(Expense.id == expense_id).first()

    if not expense:
        raise HTTPException(status_code=404, detail="Expense not found")

    db.delete(expense)
    db.commit()

    return {"message": "Deleted"}



@router.put("/{expense_id}")
def update_expense(
    expense_id: int,
    data: ExpenseUpdate,
    db: Session = Depends(get_db)
):
    expense = db.query(Expense).filter(Expense.id == expense_id).first()

    if not expense:
        raise HTTPException(status_code=404, detail="Expense not found")

    expense.description = data.description
    expense.amount = data.amount
    expense.date = data.date
    expense.community_id = data.community_id
    db.commit()
    db.refresh(expense)

    return expense