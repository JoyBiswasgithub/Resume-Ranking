# Resume Ranking System

This project is a Flask web application that ranks resumes based on their similarity to a provided job description using a pre-trained BERT model. The application allows users to upload either a single resume or a folder containing multiple resumes, along with a job description, and then ranks the resumes based on their relevance to the job description.

## Features

- **Single Resume Mode**: Upload a single resume and a job description to get a similarity score.
- **Multiple Resumes Mode**: Upload a folder containing multiple resumes and a job description to rank all the resumes.
- **Shortlisting Option**: Choose the number of top resumes to display from the ranked list.

## Tech Stack

- **Backend**: Flask, Python, PyTorch, Transformers (BERT)
- **Frontend**: HTML, CSS, JavaScript
- **File Handling**: PyPDF2 for PDF text extraction

## Installation

### Prerequisites

- Python 3.7 or higher
- Virtualenv (optional but recommended)

### Steps

1. **Create a virtual environment** (optional but recommended):

    ```bash
    python3 -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

2. **Install the dependencies**:

    ```bash
    pip install -r requirements.txt
    ```

3. **Download the pre-trained BERT model and tokenizer**:

    Before running the application, download and save the pre-trained BERT model and tokenizer:

    ```python
    from transformers import BertTokenizer, BertModel

    tokenizer = BertTokenizer.from_pretrained('bert-base-uncased')
    model = BertModel.from_pretrained('bert-base-uncased')

    tokenizer.save_pretrained('model/bert_tokenizer')
    model.save_pretrained('model/bert_model')
    ```

4. **Run the Flask application**:

    ```bash
    python app.py
    ```

5. **Access the web application**:

    Open your web browser and go to `http://127.0.0.1:5000/`.

## Usage

1. **Single Resume Mode**:
   - Select "Single Resume and Job Description".
   - Upload a resume in PDF format.
   - Enter the job description in the text area.
   - Click "Submit" to see the similarity score.

2. **Multiple Resumes Mode**:
   - Select "Multiple Resumes and Job Description".
   - Upload a folder containing multiple resumes (ensure they are all in PDF format).
   - Enter the job description in the text area.
   - Optionally, specify the number of top resumes you want to shortlist.
   - Click "Submit" to see the ranked list of resumes.

## Project Structure

```plaintext
resume-ranking-system/
├── app.py                     # Flask application
├── static/
│   ├── css/
│   │   └── styles.css         # Stylesheets
│   └── js/
│       └── script.js          # JavaScript for toggling inputs
├── templates/
│   └── index.html             # HTML template for the web app
├── model/
│   ├── bert_model/            # Directory for the BERT model
│   └── bert_tokenizer/        # Directory for the BERT tokenizer
├── uploads/                   # Directory where uploaded files will be saved
├── requirements.txt           # Python dependencies
└── README.md                  # Project README file
