from flask import Flask, render_template, request, jsonify
import random

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')  # The HTML file we created

@app.route('/play', methods=['POST'])
def play():
    user_choice = request.json['user']  # Get user's choice from frontend
    choices = ['Rock', 'Paper', 'Scissors']
    computer_choice = random.choice(choices)  # Computer randomly chooses

    # Decide winner
    if user_choice == computer_choice:
        result = "Tie"
    elif (user_choice == 'Rock' and computer_choice == 'Scissors') or \
         (user_choice == 'Paper' and computer_choice == 'Rock') or \
         (user_choice == 'Scissors' and computer_choice == 'Paper'):
        result = "You Win!"
    else:
        result = "Computer Wins!"

    # Send the result back to frontend
    return jsonify({'computer': computer_choice, 'result': result})

if __name__ == '__main__':
    app.run(debug=True)
