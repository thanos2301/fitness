import spacy
import sqlite3

nlp = spacy.load("en_core_web_sm")


def find_injury(keywords):
    conn = sqlite3.connect("injuries.db")
    cursor = conn.cursor()

    query = "SELECT * FROM injuries WHERE " + " OR ".join([f"LOWER(injury_name) LIKE ?" for _ in keywords])

    params = [f"%{keyword.lower()}%" for keyword in keywords]

    cursor.execute(query, params)
    result = cursor.fetchall()


    conn.close()
    return result

user_input = input("Please enter your injury: ")

doc = nlp(user_input)
keywords = [token.text for token in doc if token.pos_ in ['NOUN', 'PROPN']]

injuries = find_injury(keywords)

if injuries:
    for injury in injuries:
        print(f"Injury: {injury[0]}")
        print(f"Description: {injury[1]}")
        print(f"Training Plan: {injury[2]}")
        print(f"Exercises: {injury[3]}")
else:
    print("No matching injuries found.")
