from typing import TypedDict


class TypeInvestment(TypedDict):
    uuid: str
    loan: int
    amount: float
    status: int
    investor: str
