from pydantic import BaseModel
from typing import Union

class PaymentBody(BaseModel):

    product_name: str
    product_price: float
    description: str
    deliver_date: str
