# Resume Ranking System

## Overview

This Flask application provides a solution for ranking resumes based on their similarity to a job description. It leverages BERT (Bidirectional Encoder Representations from Transformers) embeddings to compare and rank resumes. 

## Working Principle

1. **Text Extraction:**
   - **Resume:** Users upload a resume in PDF format. The application extracts the text content from the PDF using the PyPDF2 library.
   - **Job Description:** Users input a job description as plain text.

2. **Text Preprocessing:**
   - Both the resume text and the job description are preprocessed to lower case and stripped of extra whitespace.

3. **BERT Embeddings:**
   - The preprocessed text of the resume and job description is converted into embeddings using the pre-trained BERT model. BERT is a transformer-based model that captures contextual relationships between words in a text.

4. **Similarity Calculation:**
   - The embeddings for both the resume and the job description are compared using cosine similarity. Cosine similarity measures the angle between two vectors in the embedding space, providing a score that indicates how similar the two texts are.

5. **Ranking:**
   - The similarity score is calculated and displayed, representing how well the resume matches the job description. A higher score indicates a better match.

## Features

- **Single Resume and Job Description:** Users can upload a single PDF resume and provide a job description. The application calculates a similarity score and displays it along with the resume name.

## Use Cases

1. **Job Matching:**
   - **Scenario:** A recruiter receives a job description and a candidate's resume. The recruiter wants to quickly assess how well the resume matches the job description.
   - **Use:** Upload the resume and job description to get a similarity score that helps in evaluating the candidate's fit for the job.

2. **Automated Resume Screening:**
   - **Scenario:** A company receives multiple resumes for a job opening and needs to shortlist candidates based on how closely their resumes match the job description.
   - **Use:** Upload individual resumes and job descriptions to obtain similarity scores, helping in the initial screening process.

3. **Personal Career Development:**
   - **Scenario:** A job seeker wants to tailor their resume to better match a specific job description before submitting it.
   - **Use:** Upload the job description and their resume to see how well their current resume aligns with the job requirements and make improvements accordingly.

## Requirements

- Python 3.6+
- Flask
- Transformers
- Torch
- PyPDF2
- Scikit-learn

## Installation

1. **Install dependencies:**

    ```bash
    pip install flask transformers torch PyPDF2 scikit-learn
    ```

## Usage

1. **Single Resume and Job Description:**

    - On the main page, upload a single PDF resume.
    - Enter the job description text.
    - Submit the form to see the similarity rank of the resume.

## Example

For single resume processing:
- Upload a file named `resume.pdf`.
- Enter a job description like "Software Engineer with experience in Python and Machine Learning."
- After submission, you will see the similarity score displayed with the resume name.

## Notes

- Ensure that the resume file is in PDF format.
- The job description should be a plain text.


