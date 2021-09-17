# Take Home Exercise: Fullstack Engineering

## 🎯 Goal

This take home exercise is meant as an opportunity for you to showcase your software engineering
skills. We think about software engineering in its broadest sense - ie not just design and 
code but also all the best practices around the software.


## 💪 Exercise
We've provided you with an implementation of a `get_transactions` endpoint that is currently 
exposed and unprotected. Your first task is to implement an authentication endpoint that protects
the `get_transactions` endpoint. 

Your next task would be to provide a web UI through which we can view the transactions data.
We have made the `get_transactions` endpoint intentionally slow to encourage you to think about
optimization techniques on the frontend and backend.


## 🧭 Constraints

Languages: Pave's backend code base is 100% Python, and our frontend is React so we would love 
to see you working with Python and React. If you're not comfortable with React, you can use 
any modern javascript framework you're comfortable with.


Runnable: we would really like to be able to run your solution - please make it easy!
Tools that can help here include Docker and/or Docker Compose.


## ❌ What is out of scope

We value your time, so we don't expect you to spend time on:
* CI/CD: this is a critical component of the software engineering process, but it can be
very heavy to setup, so we don't expect anything on this front.
* The transactions implementation itself: the exercise is not about generating the data. 
We provide a mock implementation for the transactions.
* A pretty UI: We don't expect a polished UI, we mostly just want to see how you approach the problem


## ▶️ How to run

We provide a starter API endpoint leveraging Python, Docker and FastAPI. Please use this
as a starting point - but feel free to go and modify the code and the API to accomodate
your solution.

The steps below show how to build and run the minimal API:

### Step 1: build image

```bash
docker build -t pave-api .
```

### Step 2: run

```bash
docker run --rm -p 9898:9898 pave-api
```

### Step 2: run

```bash
curl localhost:9898/transactions
```
