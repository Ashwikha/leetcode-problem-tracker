from storage import *
import csv
import sqlite3
from database import *
def create_problem():

    title = input("Problem Title: ")
    difficulty = input("Difficulty (Easy/Medium/Hard): ")
    category = input("Category: ")
    date_solved = input("Date Solved (YYYY-MM-DD): ")
    notes = input("Notes: ")

    problems = get_all_problems()

    problem_id = len(problems) + 1

    problem = {
        "id": problem_id,
        "title": title,
        "difficulty": difficulty,
        "category": category,
        "date_solved": date_solved,
        "notes": notes
    }

    add_problem(problem)

    print("Problem Added Successfully!")


def view_problems():

    problems = get_all_problems()

    if len(problems) == 0:
        print("No Problems Found")
        return

    print("\n===== Solved Problems =====\n")

    for problem in problems:

        print(f"ID: {problem['id']}")
        print(f"Title: {problem['title']}")
        print(f"Difficulty: {problem['difficulty']}")
        print(f"Category: {problem['category']}")
        print(f"Date Solved: {problem['date_solved']}")
        print(f"Notes: {problem['notes']}")
        print("-" * 40)


def remove_problem():

    view_problems()

    problem_id = int(input("Enter Problem ID to Delete: "))

    delete_problem(problem_id)

    print("Problem Deleted Successfully!")


def main():

    while True:

        print("\n===== LeetCode Tracker =====")
        print("1. Add Problem")
        print("2. View Problems")
        print("3. Delete Problem")
        print("4. Search by Difficulty")
        print("5. Search by Category")
        print("6. Statistics")
        print("7. Export to CSV")
        print("8. Update Problem")
        print("9. Progress Dashboard")
        print("10. Sort Problems")
        print("11. Exit")

        choice = input("Enter Choice: ")

        if choice == "1":
            create_problem()

        elif choice == "2":
            view_problems()

        elif choice == "3":
            remove_problem()

        elif choice == "4":
            search_by_difficulty()

        elif choice == "5":
            search_by_category()

        elif choice == "6":
            show_statistics()
   
        elif choice == "7":
            export_to_csv()

        elif choice == "8":
            update_problem()

        elif choice == "9":
            show_progress_dashboard()

        elif choice == "10":
            sort_by_difficulty()

        elif choice == "11":
            print("Goodbye!")
            break
           
           
        else:
            print("Invalid Choice")


def search_by_difficulty():
    difficulty = input("Enter difficulty (Easy/Medium/Hard): ")

    problems = get_all_problems()

    found = False

    for problem in problems:
        if problem["difficulty"].lower() == difficulty.lower():
            found = True
            print(f"\nID: {problem['id']}")
            print(f"Title: {problem['title']}")
            print(f"Category: {problem['category']}")
            print(f"Date Solved: {problem['date_solved']}")

    if not found:
            print("No matching problems found!")


def search_by_category():
    category = input("Enter category: ")

    problems = get_all_problems()

    found = False

    for problem in problems:
        if problem["category"].lower() == category.lower():
            found = True

            print(f"ID: {problem['id']}")
            print(f"Title: {problem['title']}")
            print(f"Difficulty: {problem['difficulty']}")
            print(f"Date Solved: {problem['date_solved']}")

    if not found:
        print("No matching problems found!")

def show_statistics():
    problems = get_all_problems()

    total = len(problems)
    easy = 0
    medium = 0
    hard = 0

    for problem in problems:
        difficulty = problem["difficulty"].lower()

        if difficulty == "easy":
            easy += 1
        elif difficulty == "medium":
            medium += 1
        elif difficulty == "hard":
            hard += 1

    print("\n===== Statistics =====")
    print(f"Total Problems: {total}")
    print(f"Easy: {easy}")
    print(f"Medium: {medium}")
    print(f"Hard: {hard}")
   
def export_to_csv():
    problems = get_all_problems()

    with open("problems.csv", "w", newline="") as file:
        writer = csv.writer(file)

        writer.writerow([
            "ID",
            "Title",
            "Difficulty",
            "Category",
            "Date Solved",
            "Notes"
        ])

        for problem in problems:
            writer.writerow([
                problem["id"],
                problem["title"],
                problem["difficulty"],
                problem["category"],
                problem["date_solved"],
                problem["notes"]
            ])

    print("Problems exported to problems.csv successfully!")

def update_problem():

    view_problems()

    problem_id = int(input("Enter Problem ID to Update: "))

    problems = get_all_problems()

    found = False

    for problem in problems:

        if problem["id"] == problem_id:

            found = True

            problem["title"] = input("New Title: ")
            problem["difficulty"] = input("New Difficulty: ")
            problem["category"] = input("New Category: ")
            problem["date_solved"] = input("New Date Solved: ")
            problem["notes"] = input("New Notes: ")

            save_data(problems)

            print("Problem Updated Successfully!")
            break

    if not found:
        print("Problem ID not found!")

def show_progress_dashboard():

    problems = get_all_problems()

    total = len(problems)

    if total == 0:
        print("No problems solved yet!")
        return

    easy = 0
    medium = 0
    hard = 0

    for problem in problems:

        difficulty = problem["difficulty"].lower()

        if difficulty == "easy":
            easy += 1
        elif difficulty == "medium":
            medium += 1
        elif difficulty == "hard":
            hard += 1

    easy_percent = (easy / total) * 100
    medium_percent = (medium / total) * 100
    hard_percent = (hard / total) * 100

    print("\n===== Progress Dashboard =====")
    print(f"Total Problems Solved: {total}")
    print(f"Easy   : {easy} ({easy_percent:.1f}%)")
    print(f"Medium : {medium} ({medium_percent:.1f}%)")
    print(f"Hard   : {hard} ({hard_percent:.1f}%)")

def sort_by_difficulty():

    problems = get_all_problems()

    order = {
        "easy": 1,
        "medium": 2,
        "hard": 3
    }

    sorted_problems = sorted(
        problems,
        key=lambda p: order[p["difficulty"].lower()]
    )

    print("\n===== Sorted Problems =====")

    for problem in sorted_problems:
        print(f"\nID: {problem['id']}")
        print(f"Title: {problem['title']}")
        print(f"Difficulty: {problem['difficulty']}")
        print(f"Category: {problem['category']}")


from database import create_table
create_table() 
      

def add_problem_db(problem):

    conn = sqlite3.connect("leetcode_tracker.db")
    cursor = conn.cursor()

    cursor.execute("""
    INSERT INTO problems
    (title,difficulty,category,date_solved,notes)
    VALUES (?,?,?,?,?)
    """, (
        problem["title"],
        problem["difficulty"],
        problem["category"],
        problem["date_solved"],
        problem["notes"]
    ))

    conn.commit()
    conn.close()

def view_problems_db():

    conn = sqlite3.connect("leetcode_tracker.db")
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM problems")

    rows = cursor.fetchall()

    for row in rows:
        for row in rows:
         print(f"\nID: {row[0]}")
    print(f"Title: {row[1]}")
    print(f"Difficulty: {row[2]}")
    print(f"Category: {row[3]}")
    print(f"Date Solved: {row[4]}")
    print(f"Notes: {row[5]}")

    conn.close()

def search_problem():

    keyword = input("Enter Problem Title: ").lower()

    problems = get_all_problems()

    found = False

    for problem in problems:

        if keyword in problem["title"].lower():

            print("\nFound Problem:")
            print(f"ID: {problem['id']}")
            print(f"Title: {problem['title']}")
            print(f"Difficulty: {problem['difficulty']}")
            print(f"Category: {problem['category']}")
            print(f"Date Solved: {problem['date_solved']}")
            print(f"Notes: {problem['notes']}")

            found = True

    if not found:
        print("Problem not found.")

problem = {
    "title": "Two Sum",
    "difficulty": "Easy",
    "category": "Arrays",
    "date_solved": "2026-06-11",
    "notes": "Hash Map"
}
rows = get_all_problems_db()

for row in rows:
    print(row)

add_problem_db(problem)


main()
