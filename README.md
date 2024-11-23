# Hindu Baby Names

A static website that helps parents find meaningful Hindu names for their babies. The site provides detailed information about each name, including its meaning, gender, rashi (moon sign), and numerological significance.

## Features

- Browse names by letter
- View detailed information about each name
- Search functionality
- Responsive design
- Static site for fast loading

## Development

This site is built using:
- Python
- Flask
- Frozen-Flask (for static site generation)
- Bootstrap 5

## Local Development

1. Clone the repository
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Run the Flask development server:
   ```bash
   python app.py
   ```
4. Generate static site:
   ```bash
   python freeze.py
   ```

## Deployment

The site is deployed using GitHub Pages. The static files are generated using Frozen-Flask and served from the `docs` directory.
