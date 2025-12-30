# from flask import Flask, render_template, redirect, request, url_for, session

# app = Flask(__name__)
# app.secret_key = 'supersecretkey'
# accounts = {
#     'user': 'pass',
#     'user2': 'pass2'}


# amounts = {
#     'user': 1000
#     , 'user2': 1500

# }

# @app.route('/')
# def home():
#     return render_template('home.html')



# @app.route("/login", methods=['GET', 'POST'])
# def login_post():
#     if request.method == 'POST':
#         username = request.form['username']
#         password = request.form['password']

#         if not username or not password:
#             return render_template('login.html', msg="Enter the details")

#         if username in accounts and accounts[username] == password:
#             session['user'] = username   # ✅ FIX
#             return redirect(url_for('dashboard'))

#         return render_template('login.html', msg="Incorrect credentials")

#     return render_template("login.html")


# @app.route('/dashboard')
# def dashboard():
#     if 'user' in session:
#         return render_template('dashboard.html', user=session['user'])
#     return redirect(url_for('login_post')) 


# @app.route('/balance')
# def balance():
#     if 'user' in session:
#         user = session['user']
#         return render_template('balance.html', balance=amounts[user])
#     return redirect(url_for('login_post'))



# @app.route('/withdraw', methods=['GET', 'POST'])
# def withdraw():
#     if 'user' not in session:
#         return redirect(url_for('login_post'))
    
#     user = session['user']
    
#     if request.method == 'POST':
#         amount = request.form.get('amount')
        
#         if not amount or not amount.isdigit():
#             return "Enter a valid amount", 400
        
#         amount = int(amount)
        
#         if amount <= 0:
#             return "Amount must be greater than zero", 400
        
#         if amount > amounts[user]:
#             return "Insufficient balance", 400
        
#         # Perform withdrawal
#         amounts[user] -= amount
        
#         # Optional: flash message or just redirect to balance
#         return redirect(url_for('balance'))  # Better: show updated balance
    
#     # This only runs on GET request
#     return render_template('withdraw.html')


# @app.route('/deposit', methods=['GET', 'POST'])
# def deposit():
#     if 'user' not in session:
#         return redirect(url_for('login_post'))
#     user = session['user']
#     if request.method == 'POST':
#         amount = request.form.get('amount')
    
#         if not amount or not amount.isdigit():
#             return "Enter a valid amount", 400
#         amount = int(amount)
#         if amount <= 0:
#             return "Amount must be greater than zero", 400
    
#         amounts[user] += amount
#         return redirect(url_for('balance'))  # ← Redirect after success!

#     return render_template('deposit.html')  # Only on GET



# @app.route('/transfer', methods=['GET', 'POST'])
# def transfer():
#     if 'user' not in session:
#         return redirect(url_for('login_post'))

#     sender = session['user']

#     if request.method == 'POST':
#         receiver = request.form.get('receiver')
#         amount = request.form.get('amount')

#         if receiver not in amounts:
#             return render_template('transfer.html',
#                                    msg="Receiver account not found")

#         if receiver == sender:
#             return render_template('transfer.html',
#                                    msg="Cannot transfer to same account")

#         if not amount or not amount.isdigit():
#             return render_template('transfer.html',
#                                    msg="Enter valid amount")

#         amount = int(amount)

#         if amount <= 0:
#             return render_template('transfer.html',
#                                    msg="Amount must be greater than zero")

#         if amount > amounts[sender]:
#             return render_template('transfer.html',
#                                    msg="Insufficient balance")

#         # ✅ Transfer
#         amounts[sender] -= amount
#         amounts[receiver] += amount

#         return redirect(url_for('balance'))

#     return render_template('transfer.html')








# @app.route('/logout')
# def logout():
#     session.pop('user', None)
#     return render_template('home.html')





# if __name__ == '__main__':
#     app.run(debug=True)

from flask import Flask, render_template, redirect, request, url_for, session

app = Flask(__name__)
app.secret_key = 'supersecretkey'


accounts = {
    'user': 'pass',
    'user2': 'pass2'
}


amounts = {
    'user': 100000,
    'user2': 50000
}



@app.route('/')
def home():
    return render_template('home.html')



@app.route('/login', methods=['GET', 'POST'])
def login_post():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')

        if not username or not password:
            return render_template('login.html', msg="Enter all details")

        if username in accounts and accounts[username] == password:
            session['user'] = username
            return redirect(url_for('dashboard'))

        return render_template('login.html', msg="Invalid username or password")

    return render_template('login.html')



@app.route('/dashboard')
def dashboard():
    if 'user' not in session:
        return redirect(url_for('login_post'))

    return render_template('dashboard.html', user=session['user'])



@app.route('/balance')
def balance():
    if 'user' not in session:
        return redirect(url_for('login_post'))

    user = session['user']
    return render_template('balance.html', balance=amounts[user])



@app.route('/deposit', methods=['GET', 'POST'])
def deposit():
    if 'user' not in session:
        return redirect(url_for('login_post'))

    user = session['user']

    if request.method == 'POST':
        amount = request.form.get('amount')

        if not amount or not amount.isdigit():
            return render_template('deposit.html', msg="Enter valid amount")

        amount = int(amount)

        if amount <= 0:
            return render_template('deposit.html', msg="Amount must be > 0")

        amounts[user] += amount
        return redirect(url_for('balance'))

    return render_template('deposit.html')



@app.route('/withdraw', methods=['GET', 'POST'])
def withdraw():
    if 'user' not in session:
        return redirect(url_for('login_post'))

    user = session['user']

    if request.method == 'POST':
        amount = request.form.get('amount')

        if not amount or not amount.isdigit():
            return render_template('withdraw.html', msg="Enter valid amount")

        amount = int(amount)

        if amount <= 0:
            return render_template('withdraw.html', msg="Amount must be > 0")

        if amount > amounts[user]:
            return render_template('withdraw.html', msg="Insufficient balance")

        amounts[user] -= amount
        return redirect(url_for('balance'))

    return render_template('withdraw.html')



@app.route('/transfer', methods=['GET', 'POST'])
def transfer():
    if 'user' not in session:
        return redirect(url_for('login_post'))

    sender = session['user']

    if request.method == 'POST':
        receiver = request.form.get('receiver')
        amount = request.form.get('amount')

        if receiver not in amounts:
            return render_template('transfer.html', msg="Receiver not found")

        if receiver == sender:
            return render_template('transfer.html', msg="Cannot transfer to same account")

        if not amount or not amount.isdigit():
            return render_template('transfer.html', msg="Enter valid amount")

        amount = int(amount)

        if amount <= 0:
            return render_template('transfer.html', msg="Amount must be > 0")

        if amount > amounts[sender]:
            return render_template('transfer.html', msg="Insufficient balance")

        amounts[sender] -= amount
        amounts[receiver] += amount

        return redirect(url_for('balance'))

    return render_template('transfer.html')



@app.route('/logout')
def logout():
    session.pop('user', None)
    return redirect(url_for('home'))



if __name__ == '__main__':
    app.run(debug=True)

