import streamlit as st
from resume_parser import extract_text_from_pdf
from skill_extractor import extract_skills
from similarity import calculate_similarity

st.set_page_config(page_title="Resume Job Fit Analyzer")

st.title("🧠 AI Resume & Job Fit Analyzer")

resume_file = st.file_uploader("Upload Resume (PDF)", type=["pdf"])
jd_text = st.text_area("Paste Job Description")

if st.button("Analyze"):
    if resume_file and jd_text:
        resume_text = extract_text_from_pdf(resume_file)

        score = calculate_similarity(resume_text, jd_text)
        resume_skills = extract_skills(resume_text)
        jd_skills = extract_skills(jd_text)

        missing_skills = list(set(jd_skills) - set(resume_skills))

        st.subheader("📊 Fit Score")
        st.progress(int(score * 100))
        st.write(f"**{round(score*100,2)}% Match**")

        st.subheader("✅ Resume Skills")
        st.write(resume_skills)

        st.subheader("❌ Missing Skills")
        st.write(missing_skills if missing_skills else "None 🎉")

        st.subheader("📝 Suggestions")
        if missing_skills:
            st.write("Consider adding projects or experience related to:")
            for skill in missing_skills:
                st.write(f"- {skill}")
        else:
            st.write("Your resume is well aligned!")
    else:
        st.warning("Please upload resume and paste JD")
