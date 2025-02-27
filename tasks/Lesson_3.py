# Importing the regexp module
import re

a = """homEwork:
  tHis iz your homeWork, copy these Text to variable.

  You NEED TO normalize it fROM letter CASEs point oF View. also, create one MORE senTENCE witH LAST WoRDS of each existING SENtence and add it to the END OF this Paragraph.

  it iZ misspeLLing here. fix“iZ” with correct “is”, but ONLY when it Iz a mistAKE.

  last iz TO calculate nuMber OF Whitespace characteRS in this Tex. caREFULL, not only Spaces, but ALL whitespaces. I got 87.
"""

# Normalize text
# Splitting the text into paragraphs
paragraphs = a.split("\n\n")
# List of paragraphs initialisation
normalized_paragraphs = []

# Text normalization
for paragraph in paragraphs:
    # Paragraph splitting into sentences
    sentences = re.split(r'([.!?]\s+)', paragraph)
    # List of sentences initialisation
    corrected_sentences = []
    # Sentences normalization
    for i in range(0, len(sentences), 2):
        # Spaces at the beginning of the sentence removing
        sentence = sentences[i].strip()
        if sentence:
            # Incorrect "iz" fixing and capitalization
            sentence = re.sub(r'(?<!\S)iz(?!\S)', 'is', sentence).capitalize()
        corrected_sentences.append(sentence)
        # Sentences ending punctuating appending
        if i + 1 < len(sentences):
            corrected_sentences.append(sentences[i + 1])
    # List of paragraphs population
    normalized_paragraphs.append("".join(corrected_sentences))

normalized_text = "\n\n".join(normalized_paragraphs)

print(f"\nTotal whitespace in the normalized text: {normalized_text}")





