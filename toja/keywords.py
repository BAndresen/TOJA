import os
import spacy
import subprocess
from collections import Counter

import constants


class JobDescription:
    def __init__(self):
        self.num_of_jobs = 0
        self.keyword = {}


class Resume:
    def __init__(self):
        self.score = 0
        self.keywords = {}


class KeywordExtractor:
    def __init__(self):
        self.text = ''

    def download_model(self):
        try:
            spacy.load("en_core_web_sm")
        except OSError:
            print("Downloading 'en_core_web_sm' model...")
            subprocess.run(["python", "-m", "spacy", "download", "en_core_web_sm"])

    def extract_keywords(self, text):
        self.download_model()
        nlp = spacy.load("en_core_web_sm")
        doc = nlp(text)
        keywords = [token.text for token in doc if token.pos_ in ["NOUN", "ADJ"]]
        return keywords





