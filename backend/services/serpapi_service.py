import os
import requests
from backend.config import SERPAPI_API_KEY




def fetch_leads(query: str, min_rating: float = 0.0):
    params = {
        "engine": "google_maps",
        "q": query,
        "type": "search",
        "api_key": SERPAPI_API_KEY
    }
    response = requests.get("https://serpapi.com/search", params=params)
    data = response.json()
    print("🔍 Raw SerpAPI response:", data)
    results = []
    for item in data.get("local_results", []):
        rating = item.get("rating", 0.0)
        if rating >= min_rating:
            results.append({
                "title": item.get("title"),
                "phone": item.get("phone"),
                "rating": rating,
                "reviews": item.get("reviews"),
                "address": item.get("address"),
                "website": item.get("website"),
            })

    return results
