from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

def get_flames_result(name1, name2):
    # Convert names to lowercase and remove spaces
    name1 = name1.lower().replace(" ", "")
    name2 = name2.lower().replace(" ", "")
    
    # Create a list of remaining letters after removing common letters
    remaining_letters = []
    for char in name1:
        if char not in name2:
            remaining_letters.append(char)
    for char in name2:
        if char not in name1:
            remaining_letters.append(char)
    
    # Calculate the number of remaining letters
    count = len(remaining_letters)
    
    # FLAMES dictionary
    flames = {
        1: "Friends",
        2: "Love",
        3: "Affection",
        4: "Marriage",
        5: "Enemy",
        0: "Siblings"
    }
    
    # Calculate the result
    while count > 6:
        count = count % 6
    
    return flames[count]

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/calculate', methods=['POST'])
def calculate():
    name1 = request.form.get('name1', '').strip()
    name2 = request.form.get('name2', '').strip()
    
    if not name1 or not name2:
        return jsonify({'error': 'Please enter both names'})
    
    result = get_flames_result(name1, name2)
    return jsonify({'result': result})

if __name__ == '__main__':
    app.run(debug=True) 