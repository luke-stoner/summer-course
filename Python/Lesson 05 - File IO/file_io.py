import os
from pathlib import Path
from datetime import datetime


original_dir = Path.cwd

#1
print(Path.cwd)

#2
projects = Path('projects')
projects.mkdir(exist_ok=True)
os.chdir(projects)
print('\nExercise 2: changed into', Path.cwd())

#3
print(os.listdir())

#4
Path('data').mkdir(exist_ok=True)
print(os.listdir())

#5
Path('a/b/c').mkdir(parents=True, exist_ok=True)
print(os.listdir())
print([p.name for p in Path('a').iterdir()])