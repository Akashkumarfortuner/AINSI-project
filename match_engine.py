import os
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import PyPDF2

def extract_text_from_pdf(pdf_path):
    text = ""
    with open(pdf_path, "rb") as f:
        reader = PyPDF2.PdfReader(f)
        for page in reader.pages:
            text += page.extract_text() or ""
    return text

def read_resume_text(file_path):
    ext = file_path.split('.')[-1].lower()
    if ext == 'pdf':
        return extract_text_from_pdf(file_path)
    elif ext == 'txt':
        with open(file_path, "r", encoding="utf-8") as f:
            return f.read()
    else:
        return ""

def match_resumes(job_description, resume_paths):
    documents = [job_description]
    filenames = []

    for path in resume_paths:
        text = read_resume_text(path)
        if text.strip():
            documents.append(text)
            filenames.append(os.path.basename(path))

    vectorizer = TfidfVectorizer(stop_words='english')
    tfidf_matrix = vectorizer.fit_transform(documents)

    # Compute cosine similarity between job description (index 0) and all resumes
    cosine_similarities = cosine_similarity(tfidf_matrix[0:1], tfidf_matrix[1:]).flatten()

    # Pair filename and similarity score, then sort descending
    results = list(zip(filenames, cosine_similarities))
    results.sort(key=lambda x: x[1], reverse=True)

    # Convert similarity scores to percentages (2 decimal places)
    results = [(filename, round(score * 100, 2)) for filename, score in results]

    return results
