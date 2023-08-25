# elemental-dual-RPS
 Fun Twist on the classic Rock Paper Scissors Game

# Rock-Paper-Scissors Flask App

This is a simple Rock-Paper-Scissors game implemented using Flask, a Python web framework. The game allows users to play Rock-Paper-Scissors against a computer opponent. The app keeps track of the user's and computer's scores throughout the gameplay.

## How to Play

1. Clone the repository to your local machine:

```bash
git clone https://github.com/your-username/elemental-dual-RPS.git
```

2. Navigate to the app directory:

```bash
cd elemental-dual-RPS
```

3. Install the required dependencies using `pip`:

```bash
pip install flask
```

4. Run the Flask app:

```bash
python app.py
```

5. Open a web browser and go to `http://127.0.0.1:5000/` to access the game.

## Gameplay

1. Upon opening the app in your web browser, you will be presented with the game's main page.

2. Click on your weapon of choice: "Forest," "Fire," or "Water."

3. The computer opponent will randomly select its weapon.

4. The results page will show both your choice and the computer's choice, along with the outcome of the round.

5. The scores of both you and the computer will be displayed on the main page.

6. Continue playing rounds until you decide to stop.

## Files

- `app.py`: This is the main Flask application file containing the game logic and routes.
- `static/assets/`: This directory contains the images used for the different characters ("Forest," "Fire," and "Water").
- `templates/`: This directory contains the HTML templates used for rendering the web pages.

## Code Explanation

The Flask app consists of several routes:

- `index`: Renders the main page of the game, displaying the user's and computer's scores.
- `user_choice`: Handles the user's weapon selection and initiates the computer's turn.
- `results`: Determines the outcome of the round, updates the scores, and displays the results.

The `get_outcome` function defines the rules of the Rock-Paper-Scissors game and determines the winner of each round.

## Important Note

The app's code could be further improved by using proper error handling, separating concerns (e.g., using a separate module for game logic), and enhancing the user interface. Additionally, incorporating CSS for better styling would enhance the overall experience.

Feel free to fork, modify, and improve this app according to your preferences and development practices. Happy coding!
