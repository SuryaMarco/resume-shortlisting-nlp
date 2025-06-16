# 🧠 Resume Shortlisting using NLP

This project uses Natural Language Processing (NLP) to automate the shortlisting of resumes by matching their content to a given job description.

## 📌 Features
- Extracts text from PDF resumes
- Cleans and vectorizes text using TF-IDF
- Ranks resumes by cosine similarity to job description

## 🚀 How to Run

1. Clone the repo  
   `git clone https://github.com/SuryaMarco/resume-shortlisting-nlp.git`

2. Install dependencies  
   `pip install -r requirements.txt`

3. Add:
   - Your job description to `job_description.txt`
   - Your PDF resumes inside the `resumes/` folder

4. Run the main script  
   `python main.py`

## 🧰 Technologies
- Python
- scikit-learn
- PyMuPDF
- TF-IDF
- Cosine Similarity

## 👤 Author
Surya Madha

## 📄 License
MIT
