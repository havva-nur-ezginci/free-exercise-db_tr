import json
import requests

# GitHub'dan JSON verisini indirme
url = 'https://raw.githubusercontent.com/yuhonas/free-exercise-db/main/dist/exercises.json'
response = requests.get(url)
data = response.json()

# "equipment" değeri "body only" olan egzersizlerde bulunan primaryMuscles çeşitlerini tutmak için küme (set) oluşturma
primary_muscles_set = set()

# Her bir egzersizi döngü ile kontrol etme
for exercise in data:
    if exercise.get('equipment') == 'body only' and exercise.get('primaryMuscles'):
        primary_muscles_set.update(exercise['primaryMuscles'])

# Kümedeki farklı primaryMuscles çeşitlerinin sayısı
num_unique_primary_muscles = len(primary_muscles_set)

print(f"Equipment değeri 'body only' olan egzersizlerde {num_unique_primary_muscles} farklı primaryMuscles çeşidi bulunmaktadır.")
print("Farklı primaryMuscles çeşitleri:")
for muscle in sorted(primary_muscles_set):
    print(muscle)

"""
abdominals
abductors
adductors
biceps
calves
chest
forearms
glutes
hamstrings
lats
lower back
neck
quadriceps
shoulders
triceps


"""
