from src.db_actions import db_actions
from flask import request
from flask import Flask, render_template, request, redirect, url_for
from models.Models import Book, Borrower, BookLoan
app = Flask(__name__)

db_action_instance = db_actions('data/books (1).csv', 'data/borrowers (2).csv')


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/new_borrower', methods=['POST'])
def add_borrower():

    if request.method == 'POST':
        first_name = request.form['firstName']
        last_name = request.form['lastName']
        ssn = request.form['ssn']
        email = request.form['email']
        address = request.form['address']
        city = request.form['city']
        state = request.form['state']
        phone = request.form['phone']

        print(first_name, last_name, ssn, email, address, city, state, phone)

        new_borrower = Borrower(
            first_name=first_name,
            last_name=last_name,
            ssn=ssn,
            email=email,
            address=address,
            city=city,
            state=state,
            phone=phone
        )

        db_action_instance.session.add(new_borrower)
        db_action_instance.session.commit()

        return redirect(url_for('success_page'))
    else:
        return render_template('index.html')


@app.route('/success')
def success_page():
    return render_template('success.html')


if __name__ == '__main__':
    app.run(debug=True)
