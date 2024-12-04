import sqlite3
import pygame
from datetime import datetime
from logic.components.character import Character  # Import the Character class
from logic.components.health import Health  # Ensure Health class is available

# Path to the database
DB_PATH = '../logic/score_db_connection/dogtective_scores_db.sql'

# Create a connection to the database
conn = sqlite3.connect(DB_PATH)
cursor = conn.cursor()

# Create a table if it doesn't exist
cursor.execute('''CREATE TABLE IF NOT EXISTS scores
                  (id INTEGER PRIMARY KEY AUTOINCREMENT, score INTEGER, timestamp TEXT)''')
conn.commit()

class Timer:
    def __init__(self):
        self.start_ticks = pygame.time.get_ticks()

    def update(self):
        elapsed_seconds = (pygame.time.get_ticks() - self.start_ticks) // 1000
        return elapsed_seconds

class Score:
    def __init__(self, timer, character):
        self.timer = timer
        self.character = character
        self.points = 0

    def update_score(self):
        elapsed_time = self.timer.update()
        health_points = self.character.health.current  # Access the health from the Character instance
        self.points = elapsed_time * 10 + health_points * 5
        return self.points

    def save_to_db(self):
        timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        cursor.execute("INSERT INTO scores (score, timestamp) VALUES (?, ?)", (self.points, timestamp))
        conn.commit()

def game_on(timer, character, score):
    pygame.display.flip()
    return score.update_score()

# Example of how to use these classes
timer = Timer()
character = Character(name="Dogtective", health=Health(max_health=5))  # Create Character with Health instance
score = Score(timer, character)
game_running = True

while game_running:
    # Update game state here
    character.health.decrease_health(1)  # Example of health decrease
    score_value = game_on(timer, character, score)
    print(f"Score: {score_value}")
    score.save_to_db()  # Save score to database
    # Add your condition to stop the game, e.g., game_running = False if some condition is met

# Close the database connection when done
conn.close()
