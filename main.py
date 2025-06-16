import os
import fitz  # PyMuPDF
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

def extract_text_from_pdf(pdf_path):
    text = ""
    with fitz.open(pdf_path) as doc:
        for page in doc:
            text += page.get_text()
    return text

def preprocess(text):
    return text.lower()

# Load job description
with open("job_description.txt", "r", encoding="utf-8") as f:
    job_description = preprocess(f.read())

# Load and extract text from resumes
resumes_dir = "resumes"
resume_texts = []
resume_files = []

for filename in os.listdir(resumes_dir):
    if filename.endswith(".pdf"):
        path = os.path.join(resumes_dir, filename)
        resume_files.append(filename)
        resume_texts.append(preprocess(extract_text_from_pdf(path)))

# Combine for vectorization
texts = [job_description] + resume_texts
vectorizer = TfidfVectorizer()
tfidf_matrix = vectorizer.fit_transform(texts)

# Compute similarities
scores = cosine_similarity(tfidf_matrix[0:1], tfidf_matrix[1:]).flatten()
ranked = sorted(zip(resume_files, scores), key=lambda x: x[1], reverse=True)

# Display results
print("\n📄 Resume Rankings:")
for idx, (file, score) in enumerate(ranked, 1):
    print(f"{idx}. {file} — Score: {score:.2f}")
