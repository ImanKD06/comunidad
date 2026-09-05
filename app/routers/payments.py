from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.database.connection import SessionLocal

from app.models.payment import Payment
from app.schemas.payment import PaymentCreate, PaymentUpdate

router = APIRouter(prefix="/payment", tags=["Payments"])

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.get("")
def get_payments(db: Session = Depends(get_db)):
    return db.query(Payment).all()

@router.post("")
def create_payment(
    payment: PaymentCreate,
    db: Session = Depends(get_db)
):
    new_payment = Payment(
        neighbor_id=payment.neighbor_id,
        month=payment.month,
        year=payment.year,
        amount=payment.amount,
        paid=payment.paid
    )

    db.add(new_payment)
    db.commit()
    db.refresh(new_payment)

    return new_payment

@router.delete("/{payment_id}")
def delete_payment(
    payment_id: int,
    db: Session = Depends(get_db)
):
    payment = (
        db.query(Payment)
        .filter(Payment.id == payment_id)
        .first()
    )

    if not payment:
        raise HTTPException(
            status_code=404,
            detail="Payment not found"
        )

    db.delete(payment)
    db.commit()

    return {"message": "Deleted"}


@router.put("/{payment_id}/pay")
def mark_as_paid(
    payment_id: int,
    db: Session = Depends(get_db)
):
    payment = (
        db.query(Payment)
        .filter(Payment.id == payment_id)
        .first()
    )

    if not payment:
        raise HTTPException(
            status_code=404,
            detail="Payment not found"
        )

    payment.paid = True

    db.commit()
    db.refresh(payment)

    return payment

@router.put("/{payment_id}")
def update_payment(
    payment_id: int,
    data: PaymentUpdate,
    db: Session = Depends(get_db)
):
    payment = (
        db.query(Payment)
        .filter(Payment.id == payment_id)
        .first()
    )

    if not payment:
        raise HTTPException(
            status_code=404,
            detail="Payment not found"
        )

    payment.neighbor_id = data.neighbor_id
    payment.month = data.month
    payment.year = data.year
    payment.amount = data.amount
    payment.paid = data.paid

    db.commit()
    db.refresh(payment)

    return payment
    