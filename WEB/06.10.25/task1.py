from fastapi import FastAPI
import requests
import time
from concurrent.futures import ThreadPoolExecutor, as_completed

app = FastAPI()

def safe_get(url):
    try:
        r = requests.get(url, timeout=5)
        r.raise_for_status()
        return r.json()
    except:
        return None

@app.get("/user-dashboard/{user_id}")
def dashboard(user_id: int):
    start = time.time()

    urls = {
        "profile": f"https://jsonplaceholder.typicode.com/users/{user_id}",
        "posts": f"https://jsonplaceholder.typicode.com/users/{user_id}/posts",
        "albums": f"https://jsonplaceholder.typicode.com/users/{user_id}/albums",
        "photos": f"https://jsonplaceholder.typicode.com/photos?userId={user_id}&_limit=10"
    }

    result = {}

    with ThreadPoolExecutor(max_workers=4) as executor:
        future_to_key = {
            executor.submit(safe_get, url): key
            for key, url in urls.items()
        }

        for future in as_completed(future_to_key):
            key = future_to_key[future]
            result[key] = future.result()

    posts = result["posts"] or []
    albums = result["albums"] or []
    photos = result["photos"] or []

    response = {
        "profile": result["profile"],
        "posts_count": len(posts),
        "albums_count": len(albums),
        "photos_count": len(photos),
        "execution_time": round(time.time() - start, 3)
    }

    return response