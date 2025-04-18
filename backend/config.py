import os
from dotenv import load_dotenv

load_dotenv()

SERPAPI_API_KEY = os.getenv("SERP_API_KEY")
SECRET_KEY = os.getenv("SECRET_KEY")