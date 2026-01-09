🤖 FitScoreAI

AI-powered tool to analyze resume ↔ job description fit using NLP & ML.
Built for practical hiring intelligence — not buzzwords.

🚀 What it does
Upload resume (PDF)
Paste job description
Calculates fit score
Extracts skills
Highlights missing skills
Suggests improvements

🧠 How it works
TF-IDF + cosine similarity
NLP-based skill extraction
Lightweight, fast, explainable ML

🛠 Tech Stack
Python 3.11
spaCy
scikit-learn
Streamlit

```▶️ Run locally
git clone https://github.com/your-username/FitScoreAI.git
cd FitScoreAI

python -m venv .venv
.\.venv\Scripts\Activate.ps1

pip install -r requirements.txt
python -m spacy download en_core_web_sm

streamlit run app.py
```
🧪 Example JD
Looking for a Python developer with ML, NLP, SQL,
and strong problem-solving skills.

🎯 Why this project

Real-world HR + AI use case
Interview-friendly ML logic
Easy to extend with embeddings / LLMs

