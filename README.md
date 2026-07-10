# 🤖 AI Resume Analyzer

An intelligent Resume Analyzer built with **Python** and **Streamlit** that compares a candidate's resume with a job description using **TF-IDF Vectorization** and **Cosine Similarity**. The application calculates a job match percentage and provides instant feedback based on the similarity score.

---

## 📌 Features

- 📄 Upload resume in PDF format
- 📝 Paste any job description
- 🧠 Extracts text from the uploaded resume
- 📊 Calculates resume-job compatibility score
- 📈 Displays match percentage
- 💬 Provides match feedback based on score
- ⚡ Simple and interactive Streamlit interface

---

## 🛠️ Technologies Used

- Python 3.x
- Streamlit
- PyPDF
- Scikit-learn

---

## 📚 Python Concepts Used

- Functions
- Conditional Statements
- Exception Handling
- File Handling
- Object Creation
- Modules and Packages
- String Manipulation

---

## 🤖 Machine Learning Concepts

- Natural Language Processing (NLP)
- TF-IDF (Term Frequency–Inverse Document Frequency)
- Cosine Similarity
- Text Vectorization
- Stop Words Removal

---

## 📁 Project Structure

```
AI-Resume-Analyzer/
│
├── app.py
├── requirements.txt
├── README.md
└── sample_resume.pdf (optional)
```

---

## 🚀 Installation

### 1. Clone the repository

```bash
git clone https://github.com/your-username/AI-Resume-Analyzer.git
```

### 2. Navigate to the project folder

```bash
cd AI-Resume-Analyzer
```

### 3. Create a virtual environment (Optional)

**Windows**

```bash
python -m venv venv
venv\Scripts\activate
```

**Linux / macOS**

```bash
python3 -m venv venv
source venv/bin/activate
```

### 4. Install dependencies

```bash
pip install -r requirements.txt
```

### 5. Run the application

```bash
streamlit run app.py
```

---

## 📦 Required Libraries

```text
streamlit
pypdf
scikit-learn
```

Or install manually:

```bash
pip install streamlit pypdf scikit-learn
```

---

## 💻 How It Works

1. Upload a resume in PDF format.
2. Paste the job description into the text area.
3. Click **Analyze Match Score**.
4. The application:
   - Extracts text from the PDF.
   - Converts resume and job description into TF-IDF vectors.
   - Computes cosine similarity.
   - Displays the job match percentage.
   - Provides feedback based on the score.

---

## 📊 Match Score Interpretation

| Score | Result |
|--------|--------|
| Above 70% | Excellent Match |
| 41% – 70% | Partial Match |
| 40% or below | Low Match |
📷 Application Preview
> Add screenshots of the application here.

Example:
screenshots/
├── home.png
├── result.png
## 🔮 Future Enhancements
- Support DOCX resumes
- AI-powered skill recommendations
- Missing skills analysis
- Resume keyword highlighting
- Resume ATS score
- Multiple resume comparison
- Export analysis report as PDF
- Gemini/OpenAI integration for detailed suggestions
## 🎯 Learning Outcomes

This project demonstrates practical knowledge of:
- Python Programming
- Streamlit Web Applications
- File Processing
- Natural Language Processing (NLP)
- Machine Learning Basics
- TF-IDF Vectorization
- Cosine Similarity
- Error Handling
- User Interface Development
## ⭐ If you found this project useful, consider giving it a Star!
