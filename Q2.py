import spacy

# Load spaCy English model
nlp = spacy.load("en_core_web_sm")

# Input text
text = "Chris met Alex at Apple headquarters in California. He told him about the new iPhone launch."

# Process the text
doc = nlp(text)

# 1. Named Entity Recognition (NER)
print("=== Named Entities ===")
for ent in doc.ents:
    print(f"{ent.text} --> {ent.label_}")

# 2. Pronoun ambiguity detection
pronouns = {"he", "she", "they", "him", "her", "them"}
if any(token.text.lower() in pronouns for token in doc):
    print("\nWarning: Possible pronoun ambiguity detected!")
