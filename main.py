from flask import Flask, request
from faker import Faker
import string, random, requests, csv, sqlite3



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




#### USERS/PHONES

@app.route('/users/list/')
def users_list():

    try:
        connection = sqlite3.connect('./db.sqlite3')
        cursor = connection.cursor()

        cursor.execute("SELECT * FROM users;")
        result = cursor.fetchall()

        connection.commit()
    finally:
        connection.close()

    return str(result)


@app.route('/users/create/')
def users_create():

    first_name = request.args['firstName']
    last_name = request.args['lastName']
    is_student = int(request.args['isStudent'] == 'true')  # true or false
    ID = random.randint(1, 100_000)  # TODO

    try:
        connection = sqlite3.connect('./db.sqlite3')
        cursor = connection.cursor()

        query = f"INSERT INTO users VALUES ({ID}, '{first_name}', '{last_name}', {is_student});"
        cursor.execute(query)

        connection.commit()
    finally:
        connection.close()

    return "OK"

@app.route('/phones/create/')
def phones_create():

    phone = request.args['phone']
    user_id = request.args['userId']

    try:
        connection = sqlite3.connect('./db.sqlite3')
        cursor = connection.cursor()

        query = f"INSERT INTO phones VALUES (null, '{phone}', '{user_id}');"
        cursor.execute(query)

        connection.commit()
    finally:
        connection.close()

    return "OK"

@app.route('/phones/list/')
def phones_list():

    try:
        connection = sqlite3.connect('./db.sqlite3')
        cursor = connection.cursor()

        cursor.execute("SELECT * FROM phones;")
        result = cursor.fetchall()

        connection.commit()
    finally:
        connection.close()

    return str(result)


@app.route('/users/phones/')
def users_phones():

    try:
        connection = sqlite3.connect('./db.sqlite3')
        cursor = connection.cursor()

        query = f"""
        SELECT users.first_name, users.last_name, users.id, phones.value
        FROM users
        INNER JOIN phones ON phones.user_id = users.id;
        """
        cursor.execute(query)
        result = cursor.fetchall()

        connection.commit()
    finally:
        connection.close()

    return str(result)


@app.route('/emails/create/')
def emails_create():

    email = request.args['email']
    user_id = request.args['userId']

    try:
        connection = sqlite3.connect('./db.sqlite3')
        cursor = connection.cursor()

        query = f"INSERT INTO emails VALUES (null, '{email}', '{user_id}');"
        cursor.execute(query)

        connection.commit()
    finally:
        connection.close()

    return "OK"

@app.route('/emails/list/')
def emails_list():

    try:
        connection = sqlite3.connect('./db.sqlite3')
        cursor = connection.cursor()

        cursor.execute("SELECT * FROM emails;")
        result = cursor.fetchall()

        connection.commit()
    finally:
        connection.close()

    return str(result)

@app.route('/emails/update/')
def emails_update():
    email = request.args['email']
    user_id = request.args['userId']

    try:
        connection = sqlite3.connect('./db.sqlite3')
        cursor = connection.cursor()

        query = f"UPDATE emails SET value = '{email}' WHERE emails.user_id = '{user_id}';"
        cursor.execute(query)

        connection.commit()
    finally:
        connection.close()

    return 'OK'


@app.route('/emails/delete/')
def emails_delete():
    user_id = request.args['userId']

    try:
        connection = sqlite3.connect('./db.sqlite3')
        cursor = connection.cursor()

        query = f"DELETE FROM emails WHERE emails.user_id = '{user_id}';"
        cursor.execute(query)

        connection.commit()
    finally:
        connection.close()

    return 'OK'


@app.route('/users/emails/')
def users_emails():

    try:
        connection = sqlite3.connect('./db.sqlite3')
        cursor = connection.cursor()

        query = f"""
        SELECT users.first_name, users.last_name, users.id, emails.value
        FROM users
        INNER JOIN emails ON emails.user_id = users.id;
        """
        cursor.execute(query)
        result = cursor.fetchall()

        connection.commit()
    finally:
        connection.close()

    return str(result)



if __name__ == '__main__':
    app.run(debug=True)
