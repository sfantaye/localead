# LocaLead

**Local Business Lead Generator** powered by FastAPI, Next.js, and SerpAPI

---

## 🧠 Project Overview
LocaLead is a modern web application designed to help users discover and export high-quality business leads from Google Maps based on search criteria like business type, location, and ratings. It combines the powerful scraping capabilities of SerpAPI with a beautiful frontend built in Next.js and a robust backend powered by FastAPI.

---

## 🚀 Features

- 🔍 Search and Filter Local Businesses
- 📍 Location-based Queries
- ⭐ Filter by Rating
- 📥 Export Leads as Excel (XLSX)
- 📬 Enrich Emails via External APIs (e.g., Hunter.io)
- 🔐 Auth System (via next-auth)
- 🧠 Save Searches
- 📊 Analytics Dashboard for Search Insights

---

## 🛠 Tech Stack

| Layer       | Tech            |
|-------------|-----------------|
| Frontend    | Next.js + Tailwind CSS |
| Backend     | FastAPI         |
| Scraping    | SerpAPI         |
| Auth        | next-auth / JWT |
| DB          | PostgreSQL / SQLite |
| Charts      | Recharts / Chart.js |

---

## 📁 Project Structure

```bash
LocaLead/
├── backend/                # FastAPI backend
│   ├── main.py
│   ├── routes/
│   ├── services/
│   ├── models/
│   └── utils/
├── frontend/               # Next.js frontend
│   ├── pages/
│   ├── components/
│   ├── styles/
│   └── utils/
├── .env
├── README.md
└── requirements.txt
```

---

## 🔧 Setup Instructions

### 1. Clone the repository
```bash
git clone https://github.com/sfantaye/localead.git
cd localead
```

### 2. Set up environment variables
Create a `.env` file in both `backend/` and `frontend/` with relevant API keys:

#### `.env` (Backend)
```
SERP_API_KEY=your_serpapi_key
HUNTER_API_KEY=your_hunter_key
SECRET_KEY=your_jwt_secret
DATABASE_URL=sqlite:///./test.db
```

#### `.env.local` (Frontend)
```
NEXTAUTH_URL=http://localhost:3000
NEXT_PUBLIC_API_BASE=http://localhost:8000
```

### 3. Install dependencies
```bash
# Backend
cd backend
pip install -r requirements.txt

# Frontend
cd ../frontend
npm install
```

### 4. Run the project
```bash
# Start backend
cd backend
uvicorn main:app --reload

# Start frontend
cd ../frontend
npm run dev
```

---

## 📌 API Endpoints (FastAPI)

| Method | Endpoint | Description |
|--------|----------|-------------|
| `GET`  | /api/leads | Fetch filtered leads |
| `POST` | /api/save-search | Save user searches |
| `GET`  | /api/analytics | Return dashboard metrics |

---

## ✨ Export & Enrichment
- Excel Export via `xlsx` on the frontend
- Email Enrichment via Hunter API (can be extended to Clearbit, etc.)

---

## 🔐 Authentication
Uses `next-auth` with providers (e.g., Google). On the backend, JWT is used to protect endpoints and associate user data.

---

## 📊 Analytics Features
- Top Searched Queries
- Frequent Locations
- Average Ratings
- Lead Export Count

---

## 🧪 Testing
- Backend: `pytest`
- Frontend: `jest` + `react-testing-library`

---

## 📦 Deployment
- Frontend: Vercel / Netlify
- Backend: Render / Heroku / Railway

---

## 📃 License
MIT License

---

## 👨‍💻 Author
Built by [Sintayehu Fantaye].

---

## 🙌 Contributions
PRs are welcome! Please open an issue first to discuss what you would like to change.

---

## 📎 Resources
- [SerpAPI Docs](https://serpapi.com)
- [FastAPI Docs](https://fastapi.tiangolo.com)
- [Next.js Docs](https://nextjs.org)
- [Hunter.io](https://hunter.io/)

---

## 📌 To-Do
- Add pagination
- UI theming
- Subscription plans
- Advanced filtering (price, hours, etc.)

