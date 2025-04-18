from fastapi import APIRouter, Query
from fastapi.responses import FileResponse, JSONResponse
from backend.services.serpapi_service import fetch_leads
from backend.utils.export import export_leads_to_excel
import uuid
import os

router = APIRouter()

# 🟢 Route 1: Search leads (with rating filter + optional export)
@router.get("/")
def get_leads(
    query: str = Query(..., example="Plumbers in NYC"),
    min_rating: float = Query(0.0, ge=0.0, le=5.0),
    export: bool = Query(False)
):
    leads = fetch_leads(query=query, min_rating=min_rating)

    if export:
        file_path = export_leads_to_excel(leads)
        return FileResponse(
            file_path,
            media_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet',
            filename=os.path.basename(file_path)
        )

    return {"results": leads}


# 🟢 Route 2: Save a search (auth + DB later)
@router.post("/save-search/")
def save_search(query: str):
    # Placeholder (to be replaced with DB + user info)
    return {"message": f"Search '{query}' saved successfully!"}


# 🟢 Route 3: Get user’s saved searches (auth later)
@router.get("/saved-searches/")
def get_saved_searches():
    # Placeholder
    return {"searches": ["Restaurants in LA", "Electricians in Chicago"]}


# 🟢 Route 4: Leads analytics
@router.get("/analytics/")
def get_analytics(
    query: str = Query(..., example="Plumbers in NYC")
):
    leads = fetch_leads(query=query)
    total = len(leads)
    average_rating = sum([l.get("rating", 0) for l in leads]) / total if total else 0
    top_rated = sorted(leads, key=lambda l: l.get("rating", 0), reverse=True)[:5]

    return {
        "total_results": total,
        "average_rating": round(average_rating, 2),
        "top_rated": top_rated
    }
