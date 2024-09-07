students = [
    {
        "name": "John",
        "score": 80},
    {
        "name": "Jane",
        "score": 90},
    {
        "name": "Joe",
        "score": 70},
    {
        "name": "Jill",
        "score": 60},
    {
        "name": "Jim",
        "score": 50},
    {
        "name": "Jen",
        "score": 40},
]

for student in students:
    if student["score"] >= 70:
        print(student["name"])