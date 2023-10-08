import os
import spacy
import subprocess
from PyPDF2 import PdfReader
from collections import Counter

import constants


class JobDescription:
    def __init__(self):
        self.num_of_jobs = 0
        self.keyword = []


class Resume:
    def __init__(self):
        self.score = 0
        self.keywords = []
        self.resume_path = None


class KeywordExtractor:
    def __init__(self):
        self.text = ''

    def download_model(self):
        try:
            spacy.load("en_core_web_sm")
        except OSError:
            print("Downloading 'en_core_web_sm' model...")
            subprocess.run(["python", "-m", "spacy", "download", "en_core_web_sm"])

    def extract_keywords(self, text) -> list:
        self.download_model()
        nlp = spacy.load("en_core_web_sm")
        doc = nlp(text)
        results = [token.text for token in doc if token.pos_ in ["NOUN", "PROPN"]]

        # Count the keywords
        keyword_counts = Counter(results)
        sorted_keyword_counts = sorted(keyword_counts.items(), key=lambda x: x[1], reverse=True)

        return sorted_keyword_counts[1:50]

    def extract_pdf_text(self, file_path: str):
        reader = PdfReader(file_path)
        page = reader.pages[0]
        self.text = page.extract_text()
        return self.text.lower()
