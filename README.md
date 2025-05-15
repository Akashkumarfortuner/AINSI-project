# AINSI-project

AI-Powered Resume Matching System using NLP and Machine Learning

Project Overview:
This project implements an AI-driven resume matching system that uses Natural Language Processing (NLP) and Machine Learning techniques to compare resumes against job descriptions. It helps recruiters quickly identify the best-fit candidates by calculating similarity scores based on text analysis.

Features:
•	Extracts text from PDF and TXT resume files
•	Uses TF-IDF vectorization and cosine similarity for matching
•	Supports bulk resume evaluation against a single job description
•	Generates similarity scores to rank resumes by relevance
•	Easily extensible to incorporate advanced NLP models (e.g., BERT)
Technologies Used
•	Python 3.x
•	scikit-learn
•	PyPDF2
•	NumPy
•	Pandas (optional for data handling)
Installation:
1.	Clone the repository:
    git clone https://github.com/Akashkumarfortuner/AINSI-project.git
    cd resume-matching-system
  	
3.	Create a virtual environment (optional but recommended):
    python -m venv venv
    source venv/bin/activate  # On Windows: venv\Scripts\activate
  	
5.	Install dependencies:
    pip install -r requirements.txt
Usage
1. Place your job description text in a `.txt` file or directly input as a string in the code.
2. Place all resume files (PDF or TXT) in a designated folder.
3. Run the main script to compute similarity scores:

    python match_resumes.py --job_desc path/to/job_description.txt --resumes_folder path/to/resumes/

4. The output will list resumes ranked by match percentage.
Sample Output
Resume_JohnDoe.pdf - 87.5%
Resume_JaneSmith.pdf - 79.3%
Resume_AliceBrown.txt - 65.4%

Future Improvements:
•	Integrate BERT or other transformer models for semantic matching
•	Develop a web interface for easier interaction
•	Add support for more resume formats (DOCX, HTML)
•	Implement batch processing with database storage
