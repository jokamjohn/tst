from fastapi import FastAPI, Body, Depends, Response
from fastapi.middleware.cors import CORSMiddleware

from models.user import UserSchema
from auth.auth_handler import users, verify_user, sign_jwt
from auth.auth_bearer import JWTBearer

from transactions.generator import generate_transactions_for_api

app = FastAPI()

origins = ['*']

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_methods=["*"],
    allow_headers=["*"],
)


def get_sample_transactions(limit: int):
    """
    Please do not focus on the implementation of this heuristic.
    For the purpose of the exercise, we will assume that the heuristic is already
    implemented with the code below.
    """
    transactions = generate_transactions_for_api(limit)
    return transactions


@app.get("/transactions", dependencies=[Depends(JWTBearer())])
async def get_transactions(limit: int = 10):
    return get_sample_transactions(limit)


@app.post("/signup", status_code=201)
async def signup(user: UserSchema = Body(...)):
    # validation, hash password
    users.append(user)
    return sign_jwt(user.email)


@app.post("/login", status_code=200)
async def login(response: Response, user: UserSchema = Body(...)):
    if verify_user(user):
        return sign_jwt(user.email)
    response.status_code = 400
    return {
        "error": "wrong email or password"
    }


@app.post("/logout")
async def logout():
    pass