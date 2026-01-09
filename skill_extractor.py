import spacy

nlp = spacy.load("en_core_web_sm")

SKILLS = [
    "python","machine learning","sql","nlp","data analysis",
    "deep learning","pandas","numpy","scikit-learn",
    "communication","problem solving"
]

def extract_skills(text):
    text = text.lower()
    return list(set(skill for skill in SKILLS if skill in text))
