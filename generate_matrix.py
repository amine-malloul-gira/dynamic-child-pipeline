import json

projects = ["project1", "project2", "project3"]

matrix = {"include": [{"project": proj} for proj in projects]}

with open("matrix.json", "w") as matrix_file:
    json.dump(matrix, matrix_file)

print("Matrix generated:", json.dumps(matrix, indent=2))