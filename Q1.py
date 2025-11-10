import spacy
from spacy.lang.en.stop_words import STOP_WORDS

# Load the English language model
nlp = spacy.load("en_core_web_sm")

# Input text
text = "John enjoys playing football while Mary loves reading books in the library."

# Step 1: Segment into tokens (tokenization)
doc = nlp(text)

# Step 2, 3, 4: Remove stopwords, apply lemmatization, and keep only verbs and nouns
filtered_tokens = []
for token in doc:
    if token.is_alpha and token.text.lower() not in STOP_WORDS:   # remove stopwords & punctuation
        if token.pos_ in ['NOUN', 'VERB']:                        # keep only nouns and verbs
            filtered_tokens.append(token.lemma_)                   # use lemma (base form)

print("Filtered Tokens (Nouns & Verbs only):")
print(filtered_tokens)
