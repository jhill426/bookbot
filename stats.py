def get_book_text(file_path):
    with open(file_path, "r") as f:
        return f.read()
    
def get_word_count(text):
    return len(text.split())

def get_letter_counts(text):
    letter_counts = {}
    for letter in text.lower():
        if letter.isalpha():
            letter_counts[letter] = letter_counts.get(letter, 0) + 1
    letter_counts = sorted(letter_counts.items(), key=lambda x: x[1], reverse=True)
    return letter_counts