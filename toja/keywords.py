import os
import spacy
import subprocess
from PyPDF2 import PdfReader
from collections import Counter

import constants as constant


class JobDescription:
    def __init__(self):
        self.num_of_jobs = 0
        self.keywords = []


class Resume:
    def __init__(self):
        self.score = 0
        self.keywords = []
        self.resume_path = None


class KeywordExtractor:
    def __init__(self):
        self.text = ''

    def extract_keywords(self, text, num_keywords=50) -> list:
        nlp = spacy.load(constant.SPACY_NLP_MODEL)
        doc = nlp(text)
        results = [token.text for token in doc if token.pos_ in constant.PART_OF_SPEECH]

        # Count the keywords
        keyword_counts = Counter(results)
        sorted_keyword_counts = sorted(keyword_counts.items(), key=lambda x: x[1], reverse=True)

        return sorted_keyword_counts[:num_keywords]

    def extract_pdf_text(self, file_path: str):
        reader = PdfReader(file_path)
        page = reader.pages[0]
        self.text = page.extract_text()
        return self.text.lower()


def resume_score(resume_keywords: list[tuple[str, int]], jd_keywords: list[tuple[str, int]], num_of_jd: int) -> float:
    score = 0
    for resume_words in resume_keywords:
        for jd_words in jd_keywords:
            if resume_words[0] == jd_words[0]:
                score += resume_words[1]
                score += (jd_words[1] / num_of_jd)
    return round(score, 2)
