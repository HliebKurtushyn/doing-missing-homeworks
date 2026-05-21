from fastapi import FastAPI
from pydantic import BaseModel
from concurrent.futures import ProcessPoolExecutor
import math
import time
import numpy as np

app = FastAPI()
pool = ProcessPoolExecutor()

MAX_N = 1000
MAX_M = 200

class Req(BaseModel):
    op: str
    n: int | None = None
    array: list[float] | None = None

def factorial(n):
    return math.factorial(n)

def primes(n):
    sieve = [True] * (n + 1)
    sieve[0:2] = [False, False]
    for i in range(2, int(n**0.5) + 1):
        if sieve[i]:
            for j in range(i*i, n+1, i):
                sieve[j] = False
    return [i for i, v in enumerate(sieve) if v]

def matrix(n):
    a = np.random.randint(0, 10, (n, n))
    b = np.random.randint(0, 10, (n, n))
    return (a @ b).tolist()

def stats(arr):
    arr = np.array(arr)
    return {
        "mean": float(arr.mean()),
        "median": float(np.median(arr)),
        "std": float(arr.std())
    }

@app.post("/calculate")
def calc(r: Req):
    t = time.time()

    if r.op == "factorial":
        if r.n > MAX_N: return {"error": "too big"}
        res = pool.submit(factorial, r.n).result()

    elif r.op == "primes":
        res = pool.submit(primes, r.n).result()

    elif r.op == "matrix":
        if r.n > MAX_M: return {"error": "too big"}
        res = pool.submit(matrix, r.n).result()

    elif r.op == "stats":
        res = pool.submit(stats, r.array).result()

    else:
        return {"error": "unknown op"}

    return {
        "result": res,
        "time": time.time() - t
    }