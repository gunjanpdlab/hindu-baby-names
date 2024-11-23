import json
import os
from collections import defaultdict

def analyze_name_distribution():
    # Load the names file
    file_path = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))),
                            "data", "baby_names_extended.json")
    
    with open(file_path, 'r', encoding='utf-8') as f:
        names_data = json.load(f)
    
    # Count names by first letter
    letter_counts = defaultdict(int)
    letter_names = defaultdict(list)
    
    for name in names_data.keys():
        first_letter = name[0].upper()
        letter_counts[first_letter] += 1
        letter_names[first_letter].append(name)
    
    # Print distribution
    print("\nName distribution by alphabet:")
    print("=" * 40)
    for letter in sorted(letter_counts.keys()):
        print(f"{letter}: {letter_counts[letter]} names")
    
    # Find missing or underrepresented letters
    all_letters = set('ABCDEFGHIJKLMNOPQRSTUVWXYZ')
    missing_letters = all_letters - set(letter_counts.keys())
    underrepresented = {l: c for l, c in letter_counts.items() if c < 100}
    
    print("\nMissing letters:")
    print("=" * 40)
    for letter in sorted(missing_letters):
        print(letter)
    
    print("\nLetters with fewer than 100 names:")
    print("=" * 40)
    for letter, count in sorted(underrepresented.items()):
        print(f"{letter}: {count} names")

if __name__ == "__main__":
    analyze_name_distribution()
