from flask import Flask, render_template, request
import random
import string
import itertools

app = Flask(__name__)

def generate_variations(keyword, count):
    variations = set()  # Using set to avoid duplicates
    base = keyword.lower().strip()
    
    # Basic variations
    variations.add(base)
    variations.add(base.capitalize())
    variations.add(base.upper())
    
    # Common number combinations
    numbers = ['123', '1234', '12345', '111', '000', '999', '888', '666']
    for num in numbers:
        variations.add(base + num)
        variations.add(num + base)
        variations.add(base.capitalize() + num)
        variations.add(num + base.capitalize())
    
    # Common years
    years = ['2023', '2022', '2021', '2020', '2019', '2018', '2017', '2016']
    for year in years:
        variations.add(base + year)
        variations.add(year + base)
        variations.add(base.capitalize() + year)
        variations.add(year + base.capitalize())
    
    # Special characters
    special_chars = ['@', '#', '$', '%', '&', '*', '!', '?']
    for char in special_chars:
        variations.add(base + char)
        variations.add(char + base)
        variations.add(base.capitalize() + char)
        variations.add(char + base.capitalize())
    
    # Leetspeak variations
    leetspeak = {
        'a': '@', 'e': '3', 'i': '1', 'o': '0', 's': '$', 'b': '8'
    }
    leet_word = base
    for char, replacement in leetspeak.items():
        leet_word = leet_word.replace(char, replacement)
    variations.add(leet_word)
    variations.add(leet_word.capitalize())
    
    # Reversed variations
    variations.add(base[::-1])
    variations.add(base[::-1].capitalize())
    
    # Common prefixes and suffixes
    prefixes = ['admin', 'user', 'test', 'demo', 'super']
    suffixes = ['123', 'admin', 'user', 'test', 'demo']
    
    for prefix in prefixes:
        variations.add(prefix + base)
        variations.add(prefix + base.capitalize())
    
    for suffix in suffixes:
        variations.add(base + suffix)
        variations.add(base.capitalize() + suffix)
    
    # Add some random variations
    while len(variations) < count:
        # Random capitalization
        random_cap = ''.join(c.upper() if random.random() > 0.5 else c.lower() for c in base)
        variations.add(random_cap)
        
        # Random numbers
        variations.add(base + str(random.randint(100, 999)))
        variations.add(str(random.randint(100, 999)) + base)
        
        # Random special characters
        variations.add(base + random.choice(special_chars))
        variations.add(random.choice(special_chars) + base)
    
    # Convert to list and limit to requested count
    variations_list = list(variations)
    random.shuffle(variations_list)
    return variations_list[:count]

@app.route('/', methods=['GET', 'POST'])
def index():
    generated_keywords = []
    if request.method == 'POST':
        keywords = [k.strip() for k in request.form['keywords'].split(',') if k.strip()]
        variations_count = int(request.form.get('variations', 20))
        
        for keyword in keywords:
            variations = generate_variations(keyword, variations_count)
            generated_keywords.extend(variations)
        
        # Shuffle the final list
        random.shuffle(generated_keywords)
    
    return render_template('index.html', generated_keywords=generated_keywords)

if __name__ == '__main__':
    app.run(debug=True)
