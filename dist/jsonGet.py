
import json
import requests

# GitHub'dan JSON verisini indirme
url = 'https://raw.githubusercontent.com/yuhonas/free-exercise-db/main/dist/exercises.json'
response = requests.get(url)
data = response.json()

# "beginner" seviyesindeki egzersizleri filtreleme
beginner_exercises = [exercise for exercise in data if exercise.get('equipment') == 'body only']

# Sonucu bir txt dosyasına yazdırma
with open('body_only_tr.json', 'w', encoding='utf-8') as output_file:
    json.dump(beginner_exercises, output_file, indent=2, ensure_ascii=False)

