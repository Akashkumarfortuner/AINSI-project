import os
from flask import Flask, render_template, request, redirect, url_for
from werkzeug.utils import secure_filename
from match_engine import match_resumes

UPLOAD_FOLDER = 'static/uploads'
ALLOWED_EXTENSIONS = {'pdf', 'txt'}

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload_files():
    job_desc = request.form.get('job_description')
    if not job_desc:
        return "Job description is required.", 400

    files = request.files.getlist('resumes')
    if not files or len(files) == 0:
        return "Please upload at least one resume.", 400

    saved_files = []
    for file in files:
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
            file.save(filepath)
            saved_files.append(filepath)
        else:
            return f"File type not allowed: {file.filename}", 400

    results = match_resumes(job_desc, saved_files)  # Returns list of (filename, score)

    return render_template('results.html', results=results)

if __name__ == '__main__':
    app.run(debug=True)
