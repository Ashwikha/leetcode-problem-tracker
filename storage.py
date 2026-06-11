import json
import os

print(os.path.abspath("problems.json"))
def load_data():
    if not os.path.exists("problems.json"):
        return []

    with open("problems.json", "r") as file:
        content = file.read().strip()

        if not content:
            return []

        return json.loads(content)
    

def save_data(data):
    with open("problems.json", "w") as file:
        json.dump(data, file, indent=4)

def add_problem(problem):
    data = load_data()

    data.append(problem)

    save_data(data)

def get_all_problems():
    return load_data()

def delete_problem(problem_id):

    data = load_data()

    data = [
        problem
        for problem in data
        if problem["id"] != problem_id
    ]

    save_data(data)



