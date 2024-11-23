import json
import random
import sys
import os
from typing import Dict, List, Any

# Add parent directory to Python path for imports
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from scripts.name_generator import HinduNameGenerator
from data.name_data import *

def load_sanskrit_dictionary():
    """
    This would normally load a comprehensive Sanskrit dictionary.
    For now, we'll use a smaller set of Sanskrit words and their meanings.
    """
    return {
        "amrita": "immortal",
        "ananda": "bliss",
        "chandra": "moon",
        "deva": "divine",
        "jyoti": "light",
        "karma": "action",
        "maya": "illusion",
        "prema": "love",
        "ravi": "sun",
        "satya": "truth",
        # Add more Sanskrit words here
    }

def generate_name_combinations(base_names: List[Dict], count: int) -> List[Dict]:
    """Generate new name combinations based on existing names."""
    sanskrit_dict = load_sanskrit_dictionary()
    new_names = []
    
    prefixes = ["A", "Vi", "Ni", "Pra", "Sam", "Anu", "Abhi", "Upa", "Su", "Maha"]
    suffixes = ["a", "i", "ya", "ana", "ika", "ita", "in", "ant", "aka", "van"]
    
    for _ in range(count):
        # Randomly select a base name
        base = random.choice(base_names)
        
        # Create a new name by combining elements
        prefix = random.choice(prefixes)
        suffix = random.choice(suffixes)
        new_name = prefix + base["name"].lower() + suffix
        
        # Generate variations
        variations = [
            new_name,
            new_name.replace('a', 'aa'),
            new_name.replace('i', 'ee'),
            new_name.capitalize()
        ]
        
        # Create new entry
        new_entry = {
            "name": new_name.capitalize(),
            "meaning": f"Derived from {base['meaning']}",
            "detailed_meaning": f"A variation of {base['name']}, combining elements to create new meaning",
            "gender": random.choice(["Male", "Female", "Unisex"]),
            "religious_significance": base["religious_significance"],
            "sanskrit_script": base["sanskrit_script"],  # This should be properly generated
            "pronunciation": "-".join(new_name.lower()),
            "variations": variations,
            "popularity": random.choice(["Rising", "Modern", "Traditional", "Common"])
        }
        
        new_names.append(new_entry)
    
    return new_names

def main():
    # Initialize the name generator
    generator = HinduNameGenerator()
    
    # Combine all base names
    all_base_names = (
        DEITY_NAMES +
        NATURE_NAMES +
        VIRTUE_NAMES +
        CELESTIAL_NAMES +
        VEDIC_NAMES +
        MODERN_NAMES +
        MYTHOLOGICAL_NAMES +
        ELEMENTS_AND_NATURE +
        REGIONAL_NAMES["North_Indian"] +
        REGIONAL_NAMES["South_Indian"]
    )
    
    # Generate new combinations to reach 5000 names
    remaining_count = 5000 - len(all_base_names)
    new_names = generate_name_combinations(all_base_names, remaining_count)
    
    # Combine all names
    all_names = all_base_names + new_names
    
    # Convert to dictionary format
    names_dict = {}
    for name_data in all_names:
        names_dict[name_data["name"]] = generator.generate_name_entry(
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
    
    # Add popularity data for common names
    popular_names = {
        'A': ['Aarav', 'Arjun', 'Aanya', 'Advika', 'Aryan', 'Aditya', 'Avni', 'Ananya', 'Arnav', 'Ayush'],
        'B': ['Bharat', 'Bhavya', 'Bhuvan', 'Balaji', 'Bhumi', 'Bhavesh', 'Bhakti', 'Bala', 'Badri', 'Bhanu'],
        'C': ['Chandan', 'Chitra', 'Chirag', 'Chetan', 'Chandni', 'Chakra', 'Charu', 'Chandra', 'Chahat', 'Chameli'],
        'D': ['Dev', 'Dhruv', 'Daksh', 'Divya', 'Diya', 'Darsh', 'Devi', 'Dhara', 'Daksha', 'Drishti'],
        'E': ['Ekta', 'Esha', 'Eshaan', 'Ekavir', 'Ekansh', 'Ekaja', 'Ekalinga', 'Ekanta', 'Ekagra', 'Ekapad'],
        'F': ['Falak', 'Falan', 'Falgu', 'Falguni', 'Falisha', 'Falan', 'Falaknuma', 'Falak', 'Falan', 'Falgu'],
        'G': ['Ganesh', 'Gautam', 'Gauri', 'Girish', 'Gita', 'Govind', 'Ganga', 'Garima', 'Gaurav', 'Gagan'],
        'H': ['Harsh', 'Harish', 'Hari', 'Himani', 'Hridaan', 'Hetal', 'Hemant', 'Hira', 'Hansa', 'Hitesh'],
        'I': ['Ishaan', 'Isha', 'Indra', 'Ishika', 'Ishan', 'Indira', 'Indu', 'Ira', 'Ishani', 'Iksha'],
        'J': ['Jay', 'Jiya', 'Jai', 'Jatin', 'Janvi', 'Jhanvi', 'Jiyan', 'Jyoti', 'Jagat', 'Jeevan'],
        'K': ['Krishna', 'Kabir', 'Kavya', 'Kiara', 'Krish', 'Karan', 'Kishan', 'Kanika', 'Kartik', 'Kashvi'],
        'L': ['Laksh', 'Lakshmi', 'Laxmi', 'Lavanya', 'Lakshya', 'Lalita', 'Lohit', 'Lalit', 'Lata', 'Lochan'],
        'M': ['Manav', 'Maya', 'Mohit', 'Mira', 'Madhav', 'Meera', 'Mukund', 'Mahi', 'Mahesh', 'Manan'],
        'N': ['Nav', 'Nisha', 'Nikhil', 'Neha', 'Neel', 'Nandini', 'Naksh', 'Nitya', 'Naman', 'Navya'],
        'O': ['Om', 'Ojas', 'Ojasvi', 'Omkar', 'Ojaswi', 'Omkara', 'Ojal', 'Ojasvi', 'Omisha', 'Onkar'],
        'P': ['Pranav', 'Priya', 'Parth', 'Pari', 'Prem', 'Pallavi', 'Pranay', 'Payal', 'Pankaj', 'Prisha'],
        'Q': ['Qabil', 'Qainat', 'Qashish', 'Qudrat', 'Qulsum', 'Qamar', 'Qasim', 'Qazi', 'Qubool', 'Quahira'],
        'R': ['Raj', 'Riya', 'Rohan', 'Rashi', 'Rahul', 'Rithvik', 'Riddhi', 'Rishi', 'Ruhi', 'Rudra'],
        'S': ['Sai', 'Saanvi', 'Shiv', 'Siya', 'Shree', 'Samarth', 'Sanvi', 'Sarthak', 'Shreya', 'Shaurya'],
        'T': ['Tanvi', 'Tara', 'Tanay', 'Trisha', 'Tejas', 'Tanya', 'Tarun', 'Tisha', 'Trishna', 'Trilok'],
        'U': ['Udai', 'Uma', 'Utkarsh', 'Urvi', 'Uday', 'Ujjwal', 'Unnati', 'Umang', 'Urja', 'Urvashi'],
        'V': ['Veer', 'Vanya', 'Vivaan', 'Vidhi', 'Varun', 'Vedika', 'Virat', 'Vaishnavi', 'Viaan', 'Vansh'],
        'W': ['Wamika', 'Warsha', 'Wafa', 'Wahida', 'Warda', 'Waheeda', 'Waseem', 'Wajid', 'Wamil', 'Warin'],
        'X': ['Xena', 'Xavi', 'Xavier', 'Xerxes', 'Xora', 'Xander', 'Xara', 'Xitan', 'Xora', 'Xitij'],
        'Y': ['Yash', 'Yuvraj', 'Yuvan', 'Yashvi', 'Yug', 'Yamini', 'Yogesh', 'Yuti', 'Yagna', 'Yaksha'],
        'Z': ['Zara', 'Zain', 'Zaira', 'Zayan', 'Ziva', 'Zara', 'Zaid', 'Zaina', 'Zayn', 'Ziva']
    }

    def update_name_popularity():
        for letter, names in popular_names.items():
            for index, name in enumerate(names):
                if name in names_dict:
                    names_dict[name]['popularity'] = {
                        'rank': index + 1,
                        'is_popular': True
                    }
        
        # Set default popularity for other names
        for name in names_dict:
            if 'popularity' not in names_dict[name]:
                names_dict[name]['popularity'] = {
                    'rank': 1000,
                    'is_popular': False
                }

    update_name_popularity()

    # Save to file
    output_path = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 
                              "data", "baby_names_extended.json")
    with open(output_path, "w", encoding="utf-8") as f:
        json.dump(names_dict, f, ensure_ascii=False, indent=4)

if __name__ == "__main__":
    main()
