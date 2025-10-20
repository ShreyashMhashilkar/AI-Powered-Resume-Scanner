import spacy
from sentence_transformers import SentenceTransformer
from transformers import AutoTokenizer, AutoModelForTokenClassification, pipeline
import torch

# Sentence Transformer for resume ranking
_rank_model = None
def get_rank_model():
    global _rank_model
    if _rank_model is None:
        _rank_model = SentenceTransformer("all-MiniLM-L6-v2")  # lightweight and fast
    return _rank_model

# BERT-based NER for skills
_ner_pipeline = None
def get_ner_pipeline():
    global _ner_pipeline
    if _ner_pipeline is None:
        tokenizer = AutoTokenizer.from_pretrained("dslim/bert-base-NER")
        model = AutoModelForTokenClassification.from_pretrained("dslim/bert-base-NER")
        _ner_pipeline = pipeline("ner", model=model, tokenizer=tokenizer, aggregation_strategy="simple")
    return _ner_pipeline

# Optional: spaCy for fallback skill extraction
_nlp = None
def get_spacy_nlp():
    global _nlp
    if _nlp is None:
        _nlp = spacy.load("en_core_web_sm")
    return _nlp
