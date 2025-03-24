# Importing the regexp module
import re

# Initial text
a = """homEwork:
      tHis iz your homeWork, copy these Text to variable.

      You NEED TO normalize it fROM letter CASEs point oF View. also, create one MORE senTENCE witH LAST WoRDS of each existING SENtence and add it to the END OF this Paragraph.

      it iZ misspeLLing here. fix“iZ” with correct “is”, but ONLY when it Iz a mistAKE.

      last iz TO calculate nuMber OF Whitespace characteRS in this Tex. caREFULL, not only Spaces, but ALL whitespaces. I got 87.
    """


# Text normalization
def normalize_text(text):
    # Splitting the text into paragraphs
    paragraphs = re.split(r'\n\n|\n', text)
    # List of paragraphs initialisation
    normalized_paragraphs = []
    for paragraph in paragraphs:
        # Paragraph splitting into sentences
        sentences = re.split(r'([.!?]\s+)', paragraph)
        # List of sentences initialisation
        corrected_sentences = []
        # Sentences normalization
        for i in range(0, len(sentences), 2):
            # Spaces at the beginning of the sentence removing
            sentence = sentences[i].strip().lower()
            if sentence:
                # Incorrect "iz" fixing and capitalization
                sentence = re.sub(r'(?<!\S)iz(?!\S)', 'is', sentence).capitalize()
            corrected_sentences.append(sentence)
            # Sentences ending punctuating appending
            if i + 1 < len(sentences):
                corrected_sentences.append(sentences[i + 1])
        # List of paragraphs population
        normalized_paragraphs.append("".join(corrected_sentences))
    return "\n".join(normalized_paragraphs)


# Creating the additional sentence
def create_additional_sentence(normalized_text):
    # Split text into sentences
    sentences = re.split(r'(?<=[.!?])\s+', normalized_text)
    # Extract last words
    last_words = [re.search(r'(\w+)[.!?]', s) for s in sentences if s]
    # Normalize capitalization
    last_sentence = " ".join(m.group(1) for m in last_words if m) + ".".capitalize()
    # Fix incorrect "iz"
    last_sentence = re.sub(r'(?<!\S)iz(?!\S)', 'is', last_sentence)
    return last_sentence


# Additional sentence appending
def append_additional_sentence(normalized_text, last_sentence):
    # Find the paragraph to modify and insert the additional sentence
    paragraphs = normalized_text.split("\n")
    # Append to second paragraph
    paragraphs[1] += " " + last_sentence
    return "\n".join(paragraphs)


# Count whitespace characters in text
def count_whitespaces(text):
    whitespace_count = 0
    for char in text:
        if char.isspace():
            whitespace_count += 1
    return whitespace_count


def main():
    normalized_text = normalize_text(a)
    last_sentence = create_additional_sentence(normalized_text)
    final_text = append_additional_sentence(normalized_text, last_sentence)
    original_whitespace_count = count_whitespaces(a)
    normalized_whitespace_count = count_whitespaces(final_text)
    # Print results
    print(f"\nNormalized text:\n\n{final_text}")
    print(f"\nTotal whitespace in the initial text: {original_whitespace_count}")
    print(f"\nTotal whitespace in the normalized text: {normalized_whitespace_count}")


if __name__ == "__main__":
    main()
