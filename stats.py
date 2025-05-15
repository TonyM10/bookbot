def word_count(text_file):
    return len(text_file.split())

def character_count(text_file):
    character_counts = {}
    for char in text_file.lower():
        if char in character_counts:
            character_counts[char] += 1
        else:
            character_counts[char] = 1
    return character_counts

def new_funct():
    return