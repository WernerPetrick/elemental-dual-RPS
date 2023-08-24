from flask import Flask, render_template, request, url_for, jsonify
import random

victorious = False
pc_score = 0
user_score = 0

app = Flask(__name__)

character_options = ['Forest', 'Fire', 'Water']

character_images = {
    'Forest': '../static/assets/forest.jpg',
    'Fire': '../static/assets/fire.jpg',
    'Water': '../static/assets/water.jpg'
}

def computer_turn():
    
    pc_weapon_choice = random.choice(character_options)
    
    return pc_weapon_choice
    
def get_outcome(user, pc):
    
    if user == pc:
        victorious = 'Draw'
    elif user == 'Forest' and pc == 'Water':
        victorious = True
    elif user == 'Fire' and pc == 'Forest':
        victorious = True
    elif user == 'Water' and pc == 'Fire':
        victorious = True
    elif user == 'Forest' and pc == 'Fire':
        victorious = False
    elif user == 'Fire' and pc == 'Water':
        victorious = False
    elif user == 'Water' and pc == 'Forest':
        victorious = False
    else:
        victorious = False
        
    return victorious

@app.route("/", methods=['GET', 'POST'])
def index():
    
    global pc_score
    global user_score
    
    return render_template("index.html", pc_score = pc_score, user_score = user_score)

@app.route("/user_choice", methods=['GET','POST'])
def user_choice():
    
    incoming_data = request.form.to_dict()
    selected_weapon = incoming_data.get('title')
    pc_choice = computer_turn()
    
    return render_template('gameplay.html', pc_character = pc_choice, user_character = selected_weapon, user_image = character_images[selected_weapon], pc_image = character_images[pc_choice])

@app.route("/results", methods=['GET'])
def results():
    
    global pc_score
    global user_score
    
    user = request.args.get('user')
    pc = request.args.get('pc')
    
    outcome = get_outcome(user, pc)
    
    if outcome == 'Draw':
        pass
    elif outcome == True:
        user_score += 1
    elif outcome == False:
        pc_score += 1
         
    return render_template('results.html', results = outcome, pc_score = pc_score, user_score = user_score)

if __name__ == "__main__":
    app.run()
