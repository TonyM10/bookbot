# This function counts the number of words in a text file
def word_count(text_file):
    return len(text_file.split())

# Counts each character in a text file and creates a dictionary
# of each character and their count.
def character_count(text_file):
    character_counts = {}
    for char in text_file.lower():
        if char in character_counts:
            character_counts[char] += 1
        else:
            character_counts[char] = 1
    return character_counts

# Sorts a dictionary of characters and their counts from
# greatest to least and prints alphabetical characters.
def sort_character_count(character_dict):
    items = list(character_dict.items())
    sort_items = sorted(items, key=lambda item: item[1], reverse=True)
    sorted_list_dict = [{'character': char, 'count': count} for char, count in sort_items]
    return sorted_list_dict