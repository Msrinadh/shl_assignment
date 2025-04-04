# SHL Assessment Recommendation Engine

A smart AI-powered engine that recommends the most relevant SHL assessments for a given job description (JD). Built using sentence embeddings, FastAPI, Streamlit, and BeautifulSoup-based JD scraping.

---

## 🚀 Features

- 🔍 **JD URL Scraper** using BeautifulSoup
- 🧠 **Sentence Embedding Matching** with SHL product catalog
- 🧪 **Evaluation**: Precision@K, MAP@K, F1-Score
- 🖥️ **Streamlit UI**: Skill filters, autocomplete, and simple UX
- ⚙️ **FastAPI Wrapper** for backend recommendations

---

## 📁 Project Structure

```bash
shl_recommender_updated/
├── app.py                  # Streamlit frontend
├── api.py                  # FastAPI backend API
├── extract.py              # JD scraper using BeautifulSoup
├── recommend_core.py       # Embedding and recommendation logic
├── evaluation.py           # Precision@K, F1, MAP@K evaluation script
├── shl_catalog.csv         # Sample SHL product catalog
├── requirements.txt        # All Python dependencies
└── README.md               # Project documentation



🧰 Installation
# Clone the repo
git clone https://github.com/YOUR_USERNAME/shl-recommender.git
cd shl-recommender

# Install dependencies
pip install -r requirements.txt
 Run the App
Streamlit (Frontend)
streamlit run app.py
FastAPI (Backend)
uvicorn api:app --reload
