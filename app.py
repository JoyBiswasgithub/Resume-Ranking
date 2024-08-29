from flask import Flask, render_template, request, redirect, url_for, session
import os
from werkzeug.utils import secure_filename
from transformers import BertTokenizer, BertModel
import torch
from sklearn.metrics.pairwise import cosine_similarity
import PyPDF2
import json

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'uploads/'
app.secret_key = 'supersecretkey'  # Needed for session management

# Load pre-trained BERT model and tokenizer
tokenizer = BertTokenizer.from_pretrained('bert-base-uncased')
model = BertModel.from_pretrained('bert-base-uncased')

def extract_text_from_pdf(pdf_path):
    with open(pdf_path, 'rb') as file:
        reader = PyPDF2.PdfReader(file)
        text = ''
        for page in range(len(reader.pages)):
            text += reader.pages[page].extract_text()
    return text

def get_bert_embedding(text):
    inputs = tokenizer(text, return_tensors='pt', max_length=512, truncation=True, padding=True)
    with torch.no_grad():
        outputs = model(**inputs)
    return outputs.last_hidden_state.mean(dim=1).squeeze()

def preprocess_text(text):
    return text.lower().strip()

def calculate_similarity(job_description, resume):
    job_embedding = get_bert_embedding(preprocess_text(job_description))
    resume_embedding = get_bert_embedding(preprocess_text(resume))
    similarity = cosine_similarity([job_embedding.numpy()], [resume_embedding.numpy()])[0][0]
    return float(similarity)  # Convert to Python native float

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        job_description = request.form['job_description']
        resume_file = request.files['resume']
        
        if resume_file and resume_file.filename.endswith('.pdf'):
            resume_path = os.path.join(app.config['UPLOAD_FOLDER'], secure_filename(resume_file.filename))
            resume_file.save(resume_path)
            
            resume_text = extract_text_from_pdf(resume_path)
            rank = calculate_similarity(job_description, resume_text)
            
            session['single_rank'] = rank
            session['resume_name'] = os.path.basename(resume_path)
            
            return redirect(url_for('result'))
        else:
            return render_template('index.html', error="Invalid file type. Please upload a PDF.")
    
    return render_template('index.html')

@app.route('/result')
def result():
    single_rank = session.get('single_rank')
    resume_name = session.get('resume_name')

    return render_template('result.html', single_rank=single_rank, resume_name=resume_name)

if __name__ == '__main__':
    if not os.path.exists(app.config['UPLOAD_FOLDER']):
        os.makedirs(app.config['UPLOAD_FOLDER'])
    app.run(debug=True)
