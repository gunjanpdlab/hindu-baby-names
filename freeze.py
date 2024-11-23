from flask_frozen import Freezer
from app import app, baby_names

freezer = Freezer(app)

@freezer.register_generator
def names_by_letter():
    letters = set(name[0].upper() for name in baby_names.keys())
    for letter in letters:
        yield {'letter': letter}

@freezer.register_generator
def name_details():
    for name in baby_names.keys():
        yield {'letter': name[0].upper(), 'name': name}

@freezer.register_generator
def index():
    yield {}

if __name__ == '__main__':
    freezer.freeze()
