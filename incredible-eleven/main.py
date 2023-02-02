# from fastapi import FastAPI

# app = FastAPI()

# @app.get("/")
# def payemnts():
#     return {"payment-status": "this pyament is pending yet"}

# mounting multiple appications on a common app
# from fastapi import FastAPI
# from fastapi.responses import HTMLResponse
# from accounts.accounts import accounts_app
# from payments.payments import payemnts_app


# app = FastAPI()

# @app.get("/")
# async def root():
#     return {"message": "Hello from main app"}

# app.mount("/accounts", app=accounts_app)
# # app.mount("/payments", app=payemnts_app)

from fastapi import FastAPI
from accounts import accounts
from payments import payments

app = FastAPI()

@app.get("/")
def root():
    return {"Hello": "World"}


# app1 = create_app("/app1")
# app2 = create_app("/app2")

app.include_router(accounts.router)
app.include_router(payments.router)



