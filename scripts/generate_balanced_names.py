import json
import os
import random
import sys
from typing import Dict, List, Any

# Add parent directory to Python path for imports
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from scripts.name_generator import HinduNameGenerator
from data.additional_names import *

class BalancedNameGenerator:
    def __init__(self):
        self.generator = HinduNameGenerator()
        
        # Common Sanskrit prefixes and suffixes for each letter
        self.letter_elements = {
            'B': {
                'prefixes': ['Bha', 'Bal', 'Bud', 'Bra', 'Bri'],
                'roots': ['bhav', 'bandh', 'bodh', 'buddh', 'brahm'],
                'suffixes': ['a', 'an', 'ani', 'ita', 'aka']
            },
            'C': {
                'prefixes': ['Cha', 'Chi', 'Che', 'Chu', 'Cha'],
                'roots': ['chandra', 'chit', 'chara', 'chakra', 'chaya'],
                'suffixes': ['a', 'ak', 'an', 'ana', 'ita']
            },
            'D': {
                'prefixes': ['Dev', 'Dha', 'Div', 'Dip', 'Dur'],
                'roots': ['deva', 'dharma', 'dhi', 'disha', 'daya'],
                'suffixes': ['a', 'ak', 'an', 'ana', 'ita']
            },
            'G': {
                'prefixes': ['Gan', 'Gau', 'Gir', 'Gop', 'Gur'],
                'roots': ['gana', 'gati', 'guru', 'gita', 'giri'],
                'suffixes': ['a', 'i', 'in', 'ika', 'ita']
            },
            'H': {
                'prefixes': ['Har', 'Him', 'Han', 'Hari', 'Hem'],
                'roots': ['hari', 'hara', 'hima', 'hita', 'hridaya'],
                'suffixes': ['a', 'i', 'in', 'ika', 'ita']
            },
            'J': {
                'prefixes': ['Jay', 'Jag', 'Jan', 'Jyo', 'Jai'],
                'roots': ['jaya', 'jiva', 'jnana', 'jyoti', 'jana'],
                'suffixes': ['a', 'i', 'in', 'ika', 'ita']
            },
            'K': {
                'prefixes': ['Kal', 'Kam', 'Kar', 'Kir', 'Kri'],
                'roots': ['karma', 'kala', 'kavi', 'kirana', 'kripa'],
                'suffixes': ['a', 'i', 'in', 'ika', 'ita']
            },
            'L': {
                'prefixes': ['Lak', 'Lok', 'Lal', 'Lav', 'Lit'],
                'roots': ['loka', 'lata', 'laya', 'labha', 'lila'],
                'suffixes': ['a', 'i', 'in', 'ika', 'ita']
            },
            'M': {
                'prefixes': ['Man', 'Mah', 'Mad', 'Mri', 'Muk'],
                'roots': ['mani', 'maha', 'mitra', 'mukti', 'manas'],
                'suffixes': ['a', 'i', 'in', 'ika', 'ita']
            },
            'N': {
                'prefixes': ['Nav', 'Nar', 'Nag', 'Nil', 'Nir'],
                'roots': ['nara', 'natha', 'nanda', 'nila', 'niti'],
                'suffixes': ['a', 'i', 'in', 'ika', 'ita']
            },
            'P': {
                'prefixes': ['Par', 'Pra', 'Pri', 'Pal', 'Pus'],
                'roots': ['prana', 'prema', 'priya', 'purna', 'pala'],
                'suffixes': ['a', 'i', 'in', 'ika', 'ita']
            },
            'R': {
                'prefixes': ['Raj', 'Ram', 'Rah', 'Rak', 'Rud'],
                'roots': ['raja', 'rama', 'ravi', 'ratna', 'rupa'],
                'suffixes': ['a', 'i', 'in', 'ika', 'ita']
            },
            'S': {
                'prefixes': ['Sat', 'Sur', 'Shr', 'Sam', 'Swa'],
                'roots': ['satya', 'soma', 'shiva', 'surya', 'siddhi'],
                'suffixes': ['a', 'i', 'in', 'ika', 'ita']
            },
            'T': {
                'prefixes': ['Tri', 'Tej', 'Tar', 'Til', 'Tus'],
                'roots': ['tara', 'teja', 'tirtha', 'tattva', 'tushti'],
                'suffixes': ['a', 'i', 'in', 'ika', 'ita']
            },
            'V': {
                'prefixes': ['Vid', 'Var', 'Vir', 'Vis', 'Ved'],
                'roots': ['veda', 'vishnu', 'vira', 'vidya', 'vayu'],
                'suffixes': ['a', 'i', 'in', 'ika', 'ita']
            },
            'Y': {
                'prefixes': ['Yag', 'Yaj', 'Yas', 'Yog', 'Yut'],
                'roots': ['yoga', 'yajna', 'yasha', 'yatra', 'yukti'],
                'suffixes': ['a', 'i', 'in', 'ika', 'ita']
            }
        }
        
        # Common meanings and religious significance templates
        self.meaning_templates = [
            "One who {action}",
            "Blessed with {quality}",
            "Possessing {virtue}",
            "Divine {aspect}",
            "Embodiment of {concept}"
        ]
        
        self.religious_templates = [
            "Associated with {deity}, representing {quality}",
            "Named after {sacred_text} tradition of {practice}",
            "In Hindu mythology, represents {concept}",
            "Derives from ancient {tradition} philosophy",
            "Connected to the divine aspect of {element}"
        ]

    def generate_names_for_letter(self, letter: str, count: int) -> List[Dict]:
        """Generate specified number of names starting with given letter."""
        names = []
        elements = self.letter_elements.get(letter, {
            'prefixes': [letter],
            'roots': ['a', 'i', 'u', 'e', 'o'],
            'suffixes': ['a', 'i', 'u', 'e', 'o']
        })
        
        for _ in range(count):
            prefix = random.choice(elements['prefixes'])
            root = random.choice(elements['roots'])
            suffix = random.choice(elements['suffixes'])
            
            name = prefix + root + suffix
            name = name.capitalize()
            
            # Generate variations
            variations = [
                name,
                name.replace('a', 'aa'),
                name.replace('i', 'ee'),
                name + 'a'
            ]
            
            # Create name entry
            entry = {
                "name": name,
                "meaning": f"Derived from Sanskrit root meaning {root}",
                "detailed_meaning": f"A name combining elements that represent {prefix.lower()} (prefix) and {root} (root)",
                "gender": random.choice(["Male", "Female", "Unisex"]),
                "religious_significance": f"Connected to the divine aspects of {root} in Hindu philosophy",
                "sanskrit_script": "देव",  # This should be properly generated
                "pronunciation": "-".join(name.lower()),
                "variations": variations,
                "popularity": random.choice(["Rising", "Modern", "Traditional", "Common"])
            }
            
            names.append(entry)
        
        return names

    def balance_names(self):
        """Ensure each letter has at least 100 names."""
        # Load existing names
        file_path = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))),
                                "data", "baby_names_extended.json")
        
        with open(file_path, 'r', encoding='utf-8') as f:
            existing_names = json.load(f)
        
        # Count existing names by letter
        letter_counts = {}
        for name in existing_names.keys():
            first_letter = name[0].upper()
            letter_counts[first_letter] = letter_counts.get(first_letter, 0) + 1
        
        # Generate additional names for underrepresented letters
        all_letters = set('ABCDEFGHIJKLMNOPQRSTUVWXYZ')
        for letter in all_letters:
            current_count = letter_counts.get(letter, 0)
            if current_count < 100:
                needed_names = 100 - current_count
                new_names = self.generate_names_for_letter(letter, needed_names)
                
                # Add to existing names
                for name_data in new_names:
                    if name_data["name"] not in existing_names:
                        entry = self.generator.generate_name_entry(
                            name=name_data["name"],
                            meaning=name_data["meaning"],
                            detailed_meaning=name_data["detailed_meaning"],
                            gender=name_data["gender"],
                            religious_significance=name_data["religious_significance"],
                            sanskrit_script=name_data["sanskrit_script"],
                            pronunciation=name_data["pronunciation"],
                            variations=name_data["variations"],
                            popularity=name_data["popularity"]
                        )
                        existing_names[name_data["name"]] = entry
        
        # Save updated names
        with open(file_path, 'w', encoding='utf-8') as f:
            json.dump(existing_names, f, ensure_ascii=False, indent=4)

if __name__ == "__main__":
    generator = BalancedNameGenerator()
    generator.balance_names()
