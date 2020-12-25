from flask import Flask
from faker import Faker
import string
import random

def generate_str():
    str = ''
    for _ in range(8):
        str += random.choice(string.ascii_lowercase().split(''))
    return str


app = Flask(__name__)

@app.route('/')
def hello():
    return 'Hello'


@app.route('/requirements/')
def requirements():
    with open('./requirements.txt', 'r') as file:
        data = file.read()
    return data


@app.route('/generate-users/')
def generate_users():
    fake = Faker()
    names = []
    for _ in range(100):
        names.append(fake.name())
    emails = [f'{"".join(name.split(" "))}.{generate_str()}@mail.com' for name in names]
    names_str = '----'.join(emails)
    return names_str




if __name__ == '__main__':
    app.run(debug=True)
