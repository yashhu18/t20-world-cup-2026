import json
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

teams_file = os.path.join(BASE_DIR, "../data/teams.json")
fixtures_file = os.path.join(BASE_DIR, "../data/fixtures.json")
matches_file = os.path.join(BASE_DIR, "../data/matches.json")

# Load JSON safely
def load_json(file_path):
    with open(file_path) as f:
        return json.load(f)

print("📋 Teams participating:")
teams = load_json(teams_file)
print(teams)

print("\n📅 Fixtures:")
fixtures = load_json(fixtures_file)
print(fixtures)

print("\n🏟 Matches:")
matches = load_json(matches_file)
print(matches)