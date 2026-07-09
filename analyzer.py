import streamlit as st
from pypdf import PdfReader
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

def extract_text_from_pdf(pdf_file):
    """Reads an uploaded PDF file object and extracts text."""
    reader = PdfReader(pdf_file)
    text = ""
    for page in reader.pages:
        text += page.extract_text() or ""
    return text

def calculate_match_score(resume_text, job_description):
    """Calculates the matching percentage using TF-IDF and Cosine Similarity."""
    text_content = [resume_text, job_description]
    vectorizer = TfidfVectorizer(stop_words='english')
    tfidf_matrix = vectorizer.fit_transform(text_content)
    similarity_matrix = cosine_similarity(tfidf_matrix[0:1], tfidf_matrix[1:2])
    return round(similarity_matrix[0][0] * 100, 2)

# --- Streamlit Web Interface Configuration ---
st.set_page_config(page_title="AI Resume Analyzer", page_icon="🤖", layout="centered")

st.title("🤖 AI Resume Analyzer & Matcher")
st.write("Upload any candidate's resume PDF and paste a job description to calculate their compatibility score.")

# Text input for the Job Description
job_desc = st.text_area("1. Paste the Job Description Here:", height=200, placeholder="Looking for a developer with skills in Python, Java, JavaScript...")

# File uploader for the Resume PDF
uploaded_file = st.file_uploader("2. Upload Resume (PDF format only)", type=["pdf"])

# Action button to trigger the analysis
if st.button("Analyze Match Score", use_container_width=True):
    if uploaded_file is not None and job_desc.strip() != "":
        with st.spinner("Analyzing text and calculating vector similarity..."):
            try:
                # Process the PDF and run the match
                resume_text = extract_text_from_pdf(uploaded_file)
                score = calculate_match_score(resume_text, job_desc)
                
                # Display Results
                st.success("Analysis Complete!")
                st.metric(label="Job Match Percentage", value=f"{score}%")
                
                # Feedback based on score thresholds
                if score > 70:
                    st.balloons()
                    st.write("✨ **Excellent Match!** This resume aligns strongly with the job profile keywords.")
                elif score > 40:
                    st.write("⚠️ **Partial Match.** The candidate shares some core technical skills but misses key requirements.")
                else:
                    st.write("❌ **Low Match.** The resume terminology doesn't match this job description well.")
            
            except Exception as e:
                st.error(f"An error occurred while processing the PDF: {e}")
    else:
        st.error("Please fill in both fields: paste a job description AND upload a resume PDF file.")