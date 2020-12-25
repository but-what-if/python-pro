from flask import Flask
from faker import Faker
import string, random, requests, csv


def generate_str():
    str = ''.join(random.choices(string.ascii_lowercase, k=8))
    return str



def csv_reader():
    with open('hw.csv', 'r') as file:
        reader = csv.DictReader(file, fieldnames=['Index', 'Height(Inches)', 'Weight(Pounds)' ], delimiter=',')
        index = []
        heights = []
        weights = []
        data = {}
        for line in reader:
            index.append(line["Index"])
            heights.append(line["Height(Inches)"])
            weights.append(line["Weight(Pounds)"])
        index.pop(0)
        heights.pop(0)
        weights.pop(0)
        index = [int(item.rstrip().strip()) for item in index]
        heights = [float(item.rstrip().strip()) for item in heights]
        weights = [float(item.rstrip().strip()) for item in weights]
        data['index'] = index
        data['height'] = heights
        data['weight'] = weights

        return data



app = Flask(__name__)


@app.route('/')
def hello():
    return 'Hello'


@app.route('/space/')
def get_astronauts():
    r = requests.get('http://api.open-notify.org/astros.json')
    astronauts = r.json()
    return astronauts


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
    names_str = '-------'.join(emails)
    return names_str


@app.route('/mean/')
def convert():
    data = csv_reader()
    height = round((sum(data['height'])/len(data['height']))*2.54, 3)
    weight = round((sum(data['weight'])/len(data['weight']))*0.454, 3)
    return f'Average height: {height} cm  -  Average weight: {weight} kg'





if __name__ == '__main__':
    app.run(debug=True)
