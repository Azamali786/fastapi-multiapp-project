from fastapi import APIRouter
from .models import PaymentBody

router = APIRouter()

@router.get("/payments")
def payemnts():
    return {"payment-status": "this pyament is pending yet"}

@router.post("/payments")
def payments(payment: PaymentBody):
    return {"payments-data":payment}