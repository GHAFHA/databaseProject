from src.db_actions import db_actions
from flask import request
from flask import Flask, render_template, request, redirect, url_for
from models.Models import Book, Borrower, BookLoan
app = Flask(__name__)

db_action_instance = db_actions('data/books (1).csv', 'data/borrowers (2).csv')
id = 1001


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/checkout')
def checkout():
    return render_template('checkout.html')


@app.route('/admin')
def admin():
    return render_template('admin.html')


@app.route('/viewfines')
def viewfines():
    return render_template('viewfines.html')


@app.route('/new_borrower', methods=['GET', 'POST'])
def add_borrower():
    global id

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
            ID0000id=(f'ID0000{id}'),
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

        id += 1

        return redirect(url_for('/'))
    else:
        return render_template('new_borrower.html')


@app.route('/checkout', methods=['GET', 'POST'])
def check_out_book():
    if request.method == 'POST':
        borrower_id = request.form['card_number']
        ISBN10 = request.form['ISBN10']
        date_out = request.form['date_out']
        due_date = request.form['due_date']
        date_in = request.form['date_in']

        new_book_loan = BookLoan(
            borrower_id=borrower_id,
            ISBN10=ISBN10,
            date_out=date_out,
            due_date=due_date,
            date_in=date_in
        )

        db_action_instance.session.add(new_book_loan)
        db_action_instance.session.commit()

        return redirect(url_for('/'))
    else:
        return render_template('checkout.html')


@app.route('/success')
def success_page():
    return render_template('success.html')


if __name__ == '__main__':
    app.run(debug=True)
