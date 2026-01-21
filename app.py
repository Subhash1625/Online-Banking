<<<<<<< HEAD
from flask import Flask, render_template, request, redirect, url_for, session, flash
=======
from flask import Flask, render_template, request, redirect, url_for, session
>>>>>>> fb96b92cb73b5599d0987adabf1cc9896858c01f
from database.tables import create_tables
from database.utility import (
    addUser,
    validate_user,
    get_balance,
    update_balance
)

app = Flask(__name__)
app.secret_key = "supersecretkey"

create_tables()
<<<<<<< HEAD




USERS = {
    "admin": {"password": "admin123", "balance": 5000},
    "subhash": {"password": "subhash123", "balance": 3000},
    "user1": {"password": "user123", "balance": 1000}
    # you can add more users here
}






=======

addUser('user2', 'pass2')




>>>>>>> fb96b92cb73b5599d0987adabf1cc9896858c01f


@app.route('/')
def home():
    return render_template('home.html')


@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        if not username or not password:
            return render_template('register.html', msg="Fill all fields")

        if addUser(username, password):
            return redirect(url_for('login'))

        return render_template('register.html', msg="User already exists")

    return render_template('register.html')


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')

<<<<<<< HEAD
        if username in USERS and USERS[username]['password'] == password:
=======
        
        if username == 'admin' and password == 'admin123':
>>>>>>> fb96b92cb73b5599d0987adabf1cc9896858c01f
            session['user'] = username
            return redirect(url_for('dashboard'))

        return render_template('login.html', msg="Invalid username or password")

    return render_template('login.html')




@app.route('/dashboard')
def dashboard():
    if 'user' not in session:
        return redirect(url_for('login'))

    return render_template('dashboard.html', user=session['user'])


@app.route('/balance')
def balance():
    if 'user' not in session:
        return redirect(url_for('login'))
<<<<<<< HEAD

    username = session['user']
    bal = USERS[username]['balance']
    return render_template('balance.html', balance=bal)

=======

    bal = get_balance(session['user'])
    return render_template('balance.html', balance=bal)
>>>>>>> fb96b92cb73b5599d0987adabf1cc9896858c01f



@app.route('/deposit', methods=['GET', 'POST'])
def deposit():
    if 'user' not in session:
        return redirect(url_for('login'))

    msg = None
    if request.method == 'POST':
<<<<<<< HEAD
        username = session['user']
        amount = int(request.form.get('amount', 0))

        # Update balance
        USERS[username]['balance'] += amount

        return render_template('deposit.html', msg=f"₹{amount} deposited successfully!")

    return render_template('deposit.html')
=======
        try:
            amount = int(request.form['amount'])
            if amount <= 0:
                msg = "Enter a positive amount"
            else:
                
                bal = get_balance(session['user'])
                
                update_balance(session['user'], bal + amount)
                return redirect(url_for('balance'))
        except ValueError:
            msg = "Enter a valid number"

    return render_template('deposit.html', msg=msg)

>>>>>>> fb96b92cb73b5599d0987adabf1cc9896858c01f






@app.route('/withdraw', methods=['GET', 'POST'])
def withdraw():
    if 'user' not in session:
        return redirect(url_for('login'))

    if request.method == 'POST':
<<<<<<< HEAD
        username = session['user']
        amount = int(request.form.get('amount', 0))

        if amount <= 0:
            msg = "Enter a valid amount."
        elif amount > USERS[username]['balance']:
            msg = "Insufficient balance."
        else:
            USERS[username]['balance'] -= amount
            msg = f"₹{amount} withdrawn successfully!"

        return render_template('withdraw.html', msg=msg)
=======
        amount = int(request.form['amount'])
        bal = get_balance(session['user'])

        if amount > bal:
            return render_template('withdraw.html', msg="Insufficient balance")

        update_balance(session['user'], bal - amount)
        return redirect(url_for('balance'))
>>>>>>> fb96b92cb73b5599d0987adabf1cc9896858c01f

    return render_template('withdraw.html')


<<<<<<< HEAD


=======
>>>>>>> fb96b92cb73b5599d0987adabf1cc9896858c01f
@app.route('/transfer', methods=['GET', 'POST'])
def transfer():
    if 'user' not in session:
        return redirect(url_for('login'))
<<<<<<< HEAD

    if request.method == 'POST':
        sender = session['user']
        receiver = request.form.get('receiver')
        amount = int(request.form.get('amount', 0))

        # Check if receiver exists
        if receiver not in USERS:
            return render_template('transfer.html', msg="Receiver does not exist!")

        # Check if sender has enough balance
        if USERS[sender]['balance'] < amount:
            return render_template('transfer.html', msg="Insufficient balance!")

        # Perform transfer
        USERS[sender]['balance'] -= amount
        USERS[receiver]['balance'] += amount

        return render_template('transfer.html', msg=f"₹{amount} transferred to {receiver} successfully!")

    return render_template('transfer.html')
=======

    msg = None

    if request.method == 'POST':
        to_user = request.form.get('to_user')
        amount_str = request.form.get('amount')

        if not to_user or not amount_str:
            msg = "All fields are required"
        else:
            try:
                amount = int(amount_str)
                if amount <= 0:
                    msg = "Enter a positive amount"
                else:
                    from_user = session['user']

                    if from_user == to_user:
                        msg = "You cannot transfer to yourself"
                    else:
                        sender_balance = get_balance(from_user)

                        if sender_balance < amount:
                            msg = "Insufficient balance"
                        else:
                            receiver_balance = get_balance(to_user)

                            if receiver_balance is None:
                                msg = "Receiver account does not exist"
                            else:
                                # update balances
                                update_balance(from_user, sender_balance - amount)
                                update_balance(to_user, receiver_balance + amount)

                                return redirect(url_for('balance'))

            except ValueError:
                msg = "Enter a valid number"
>>>>>>> fb96b92cb73b5599d0987adabf1cc9896858c01f

    return render_template('transfer.html', msg=msg)


@app.route('/logout')
def logout():
    session.pop('user', None)
    return redirect(url_for('home'))


if __name__ == '__main__':
    app.run(debug=True)
