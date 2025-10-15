import spacy
from sentence_transformers import SentenceTransformer

_nlp = None
_embedding_model = None

def get_nlp():
    global _nlp
    if _nlp is None:
        _nlp = spacy.load("en_core_web_sm")
    return _nlp

def get_embedding_model():
    global _embedding_model
    if _embedding_model is None:
        # Use a smaller model for lower memory
        _embedding_model = SentenceTransformer("all-MiniLM-L6-v2")
    return _embedding_model