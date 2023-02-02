from fastapi import APIRouter

router = APIRouter()

@router.get("/accounts")
def accounts():
    return {"accounts-status": "accounts has been created"}

@router.post("/accounts/{name}")
def accounts(name):
    return {"accounts-name": name}