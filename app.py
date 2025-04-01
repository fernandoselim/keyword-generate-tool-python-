from flask import Flask, render_template, request
import random
import string
import itertools

app = Flask(__name__)

def generate_password_variations(keywords, num_variations=5):
    new_passwords = []
    common_special_chars = ['@', '#', '$', '%', '&', '*', '!', '?', '_', '-']
    common_numbers = ['123', '456', '789', '111', '222', '333', '444', '555', '666', '777', '888', '999']
    common_years = ['2020', '2021', '2022', '2023', '2024', '1990', '1991', '1992', '1993', '1994', '1995']
    
    for keyword in keywords:
        keyword = keyword.strip()
        # Basic variations
        for _ in range(num_variations):
            # Capitalize first letter
            variation = keyword.capitalize()
            
            # Add random numbers
            if random.choice([True, False]):
                variation += random.choice(common_numbers)
            
            # Add random special characters
            if random.choice([True, False]):
                variation += random.choice(common_special_chars)
            
            # Add random year
            if random.choice([True, False]):
                variation += random.choice(common_years)
            
            # Add random uppercase letters
            if random.choice([True, False]):
                variation += random.choice(string.ascii_uppercase)
            
            new_passwords.append(variation)
            
            # Create more complex variations
            if random.choice([True, False]):
                # Add common words
                common_words = ['admin', 'user', 'pass', '1234', 'qwerty', 'password']
                variation = keyword + random.choice(common_words)
                new_passwords.append(variation)
            
            # Add leetspeak variations
            if random.choice([True, False]):
                leetspeak = keyword.replace('a', '@').replace('e', '3').replace('i', '1').replace('o', '0').replace('s', '$')
                new_passwords.append(leetspeak)
            
            # Add reverse variations
            if random.choice([True, False]):
                reverse = keyword[::-1]
                new_passwords.append(reverse)
            
            # Add common prefixes/suffixes
            prefixes = ['admin', 'user', 'test', 'demo', 'temp']
            suffixes = ['123', '456', '789', 'admin', 'user']
            
            if random.choice([True, False]):
                new_passwords.append(random.choice(prefixes) + keyword)
            if random.choice([True, False]):
                new_passwords.append(keyword + random.choice(suffixes))

    # Remove duplicates while preserving order
    return list(dict.fromkeys(new_passwords))

@app.route("/", methods=["GET", "POST"])
def index():
    generated_passwords = []
    if request.method == "POST":
        try:
            input_keywords = [k.strip() for k in request.form["keywords"].split(',') if k.strip()]
            num_variations = min(max(int(request.form["variations"]), 1), 20)  # Ensure between 1 and 20
            generated_passwords = generate_password_variations(input_keywords, num_variations)
        except Exception as e:
            print(f"Error: {str(e)}")
            generated_passwords = []
    return render_template("index.html", generated_keywords=generated_passwords)

if __name__ == "__main__":
    app.run(host='localhost')
