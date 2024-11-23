from flask import Flask, render_template, jsonify, request, send_file, redirect, url_for, make_response, abort
import json
import os
from io import BytesIO
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont

app = Flask(__name__)

# Load baby names data
def load_baby_names():
    with open('data/baby_names_extended.json', 'r', encoding='utf-8') as f:
        return json.load(f)

baby_names = load_baby_names()

@app.route('/index.html')
@app.route('/')
def index():
    """Display the home page."""
    rashis = sorted(list(set(details['rashi'] for details in baby_names.values())))
    return render_template('index.html', rashis=rashis)

@app.route('/api/search')
def api_search():
    query = request.args.get('q', '').lower()
    gender = request.args.get('gender')
    rashi = request.args.get('rashi')
    sort_by = request.args.get('sort')
    
    results = []
    
    for name, details in baby_names.items():
        # Basic name search
        if query and query not in name.lower() and query not in details['meaning'].lower():
            continue
            
        # Gender filter
        if gender and details['gender'].lower() != gender.lower():
            continue
            
        # Rashi filter
        if rashi and details['rashi'] != rashi:
            continue
            
        results.append({
            'name': name,
            'meaning': details['meaning'],
            'gender': details['gender'],
            'rashi': details['rashi'],
            'popularity': details.get('popularity', ''),
            'sanskrit_script': details.get('sanskrit_script', ''),
            'url': f"/{name[0].lower()}/{name.lower()}.html"
        })
    
    # Sort results
    if sort_by == 'popularity':
        results.sort(key=lambda x: x['popularity'].get('rank', float('inf')), reverse=True)
    elif sort_by == 'name':
        results.sort(key=lambda x: x['name'])
    
    return jsonify(results)

@app.route('/search')
def search_page():
    query = request.args.get('q', '').strip()
    gender = request.args.get('gender', 'all').lower()
    
    if not query:
        return redirect(url_for('index'))
    
    # Search logic
    results = {}
    
    for name, details in baby_names.items():
        # Search match
        if (query.lower() in name.lower() or 
            query.lower() in details['meaning'].lower()) and \
           (gender == 'all' or details['gender'].lower() == gender):
            
            # Ensure popularity data is in correct format
            if 'popularity' not in details:
                details['popularity'] = {
                    'is_popular': False,
                    'rank': float('inf')  # For sorting purposes
                }
            elif isinstance(details['popularity'], str):
                popularity_str = details['popularity']
                details['popularity'] = {
                    'is_popular': bool(popularity_str),
                    'rank': float('inf')
                }
            
            results[name] = details
    
    # Sort results by popularity rank and then alphabetically
    sorted_results = dict(sorted(results.items(), 
                               key=lambda x: (x[1]['popularity'].get('rank', float('inf')), x[0])))
    
    return render_template('search_results.html', 
                         results=sorted_results, 
                         query=query)

@app.route('/<letter>/index.html')
def names_by_letter(letter):
    """Display names starting with the given letter."""
    letter = letter.upper()
    matching_names = {name: details for name, details in baby_names.items() if name[0].upper() == letter}
    if not matching_names:
        return render_template('404.html'), 404
    return render_template('index.html', letter=letter, names=matching_names)

@app.route('/<letter>/<name>.html')
def name_details(letter, name):
    """Display details for a specific name."""
    name_info = get_name_info(letter, name)
    if name_info:
        return render_template('name_details.html', name_info=name_info)
    return render_template('404.html'), 404

def get_name_info(letter, name):
    """Get information about a specific name."""
    for n, details in baby_names.items():
        if n.lower() == name.lower():
            return {'name': n, 'gender': details['gender'], 'meaning': details['meaning'], 'numerology': details['numerology'], 'rashi': details['rashi']}
    return None

if __name__ == '__main__':
    app.run(debug=True)
