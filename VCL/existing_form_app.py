# existing_form_app.py (Py Base - Real Alive)
import json

def fill_form():
    name = input("Name? ")
    age = input("Age? ")
    with open('responses.json', 'w') as f:
        json.dump({'name': name, 'age': age}, f)

fill_form()
