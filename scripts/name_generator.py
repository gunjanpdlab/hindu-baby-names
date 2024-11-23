import json
import random
from typing import Dict, List, Any

class HinduNameGenerator:
    def __init__(self):
        # Basic elements for name generation
        self.rashas = [
            "Mesh (Aries)", "Vrishabh (Taurus)", "Mithun (Gemini)", 
            "Kark (Cancer)", "Simha (Leo)", "Kanya (Virgo)",
            "Tula (Libra)", "Vrishchik (Scorpio)", "Dhanu (Sagittarius)",
            "Makar (Capricorn)", "Kumbh (Aquarius)", "Meen (Pisces)"
        ]
        
        self.lucky_colors = [
            "Red", "Blue", "Yellow", "Green", "Orange", "White", 
            "Purple", "Pink", "Brown", "Gold", "Silver"
        ]
        
        self.days = [
            "Sunday", "Monday", "Tuesday", "Wednesday", 
            "Thursday", "Friday", "Saturday"
        ]

    def generate_numerology(self) -> Dict[str, str]:
        number = str(random.randint(1, 9))
        meanings = {
            "1": "Natural leaders, independent, and ambitious",
            "2": "Diplomatic, cooperative, and sensitive",
            "3": "Creative, expressive, and optimistic",
            "4": "Practical, trustworthy, and organized",
            "5": "Versatile, adventurous, and freedom-loving",
            "6": "Responsible, caring, and harmonious",
            "7": "Spiritual, analytical, and wisdom-seeking",
            "8": "Powerful, successful, and material-oriented",
            "9": "Humanitarian, compassionate, and selfless"
        }
        return {
            "number": number,
            "meaning": meanings[number]
        }

    def generate_lucky_elements(self) -> Dict[str, str]:
        return {
            "color": f"{random.choice(self.lucky_colors)}, {random.choice(self.lucky_colors)}",
            "day": random.choice(self.days),
            "number": f"{random.randint(1, 9)}, {random.randint(1, 9)}"
        }

    def generate_name_entry(self, 
                          name: str,
                          meaning: str,
                          detailed_meaning: str,
                          gender: str,
                          religious_significance: str,
                          sanskrit_script: str,
                          pronunciation: str,
                          variations: List[str],
                          popularity: str) -> Dict[str, Any]:
        return {
            "meaning": meaning,
            "detailed_meaning": detailed_meaning,
            "gender": gender,
            "origin": "Sanskrit",
            "religious_significance": religious_significance,
            "rashi": random.choice(self.rashas),
            "numerology": self.generate_numerology(),
            "variations": variations,
            "lucky_elements": self.generate_lucky_elements(),
            "popularity": popularity,
            "sanskrit_script": sanskrit_script,
            "pronunciation": pronunciation
        }

    def load_existing_names(self, file_path: str) -> Dict[str, Any]:
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                return json.load(f)
        except FileNotFoundError:
            return {}

    def save_names(self, names: Dict[str, Any], file_path: str):
        with open(file_path, 'w', encoding='utf-8') as f:
            json.dump(names, f, ensure_ascii=False, indent=4)

    def add_names_batch(self, 
                       existing_names: Dict[str, Any], 
                       new_names_data: List[Dict[str, Any]]) -> Dict[str, Any]:
        for name_data in new_names_data:
            if name_data["name"] not in existing_names:
                entry = self.generate_name_entry(
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
        return existing_names

if __name__ == "__main__":
    generator = HinduNameGenerator()
    file_path = "../data/baby_names_extended.json"
    existing_names = generator.load_existing_names(file_path)
    
    # Example usage:
    new_names_data = [
        {
            "name": "Krishna",
            "meaning": "Dark, Divine",
            "detailed_meaning": "The name represents the divine incarnation of Lord Vishnu, who is known for his wisdom, love, and playfulness.",
            "gender": "Male",
            "religious_significance": "Lord Krishna is one of the most beloved deities in Hinduism, known for the Bhagavad Gita and his role in the Mahabharata.",
            "sanskrit_script": "कृष्ण",
            "pronunciation": "krish-na",
            "variations": ["Krishn", "Krushna", "Kishen"],
            "popularity": "Very Popular"
        }
    ]
    
    updated_names = generator.add_names_batch(existing_names, new_names_data)
    generator.save_names(updated_names, file_path)
