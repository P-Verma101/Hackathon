# from flask import Flask, render_template, request, redirect, url_for, flash
# import sqlite3
# from werkzeug.security import generate_password_hash, check_password_hash

# app = Flask(__name__)
# app.secret_key = 'NOAPILOL'

# def init_sqlite_db():
#     conn = sqlite3.connect('database.db')
#     print("Opened database successfully")

#     conn.execute('CREATE TABLE IF NOT EXISTS users (username TEXT, password TEXT)')
#     print("initialized the table")
#     conn.close()

# init_sqlite_db()

# @app.route('/')
# def index():
#     return render_template('index.html')

# @app.route('/login/', methods=['GET', 'POST'])
# def login():
#     if request.method == 'POST':
#         username = request.form['username']
#         password = request.form['password']

#         with sqlite3.connect('database.db') as con:
#             cur = con.cursor()
#             cur.execute("SELECT * FROM users WHERE username = ?", (username,))
#             user = cur.fetchone()

#             if user and check_password_hash(user[1], password):
#                 flash('Login successful!', 'success')
#                 return redirect(url_for('index'))
#             else:
#                 flash('Invalid credentials, please try again.', 'danger')

#     return render_template('login.html')

# @app.route('/signup/', methods=['GET', 'POST'])
# def signup():
#     if request.method == 'POST':
#         username = request.form['username']
#         password = request.form['password']
#         hashed_password = generate_password_hash(password, method='pbkdf2:sha256')

#         with sqlite3.connect('database.db') as con:
#             try:
#                 cur = con.cursor()
#                 cur.execute("SELECT * FROM users WHERE username = ?", (username,))
#                 user = cur.fetchone()
#                 if user:
#                     flash('User already exists!', 'warning')
#                 else:
#                     cur.execute("INSERT INTO users (username, password) VALUES (?, ?)", (username, hashed_password))
#                     con.commit()
#                     flash('User created successfully!', 'success')
                    
#                     # debug saving passwords in plain plain text to keep track off
#                     # remove later
#                     with open("userpass.csv", "a") as f:
#                         f.writelines(f"{username},{password}")

#                         # del later
#                     return redirect(url_for('login'))
#             except Exception as e:
#                 con.rollback()
#                 flash(f'Error :{e}', "danger")



#     return render_template('signup.html')

# if __name__ == '__main__':
#     app.run(debug=True)



# from flask import Flask, render_template, request, redirect, url_for, flash, session
# import sqlite3
# from werkzeug.security import generate_password_hash, check_password_hash
# from functools import wraps

# app = Flask(__name__)
# app.secret_key = 'NOAPILOL'

# def init_sqlite_db():
#     conn = sqlite3.connect('database.db')
#     print("Opened database successfully")

#     conn.execute('CREATE TABLE IF NOT EXISTS users (username TEXT PRIMARY KEY, password TEXT)')
#     print("Initialized the table")
#     conn.close()

# init_sqlite_db()

# def login_required(f):
#     @wraps(f)
#     def decorated_function(*args, **kwargs):
#         if 'username' not in session:
#             flash('You need to be logged in to access this page.', 'danger')
#             return redirect(url_for('login'))
#         return f(*args, **kwargs)
#     return decorated_function

# @app.route('/')
# def index():
#     return render_template('index.html')

# @app.route('/login/', methods=['GET', 'POST'])
# def login():
#     if request.method == 'POST':
#         username = request.form['username']
#         password = request.form['password']

#         with sqlite3.connect('database.db') as con:
#             cur = con.cursor()
#             cur.execute("SELECT * FROM users WHERE username = ?", (username,))
#             user = cur.fetchone()

#             if user and check_password_hash(user[1], password):
#                 session['username'] = username
#                 flash('Login successful!', 'success')
#                 return redirect(url_for('dashboard'))
#             else:
#                 flash('Invalid credentials, please try again.', 'danger')

#     return render_template('login.html')

# @app.route('/signup/', methods=['GET', 'POST'])
# def signup():
#     if request.method == 'POST':
#         username = request.form['username']
#         password = request.form['password']
#         hashed_password = generate_password_hash(password, method='pbkdf2:sha256')

#         with sqlite3.connect('database.db') as con:
#             try:
#                 cur = con.cursor()
#                 cur.execute("SELECT * FROM users WHERE username = ?", (username,))
#                 user = cur.fetchone()
#                 if user:
#                     flash('User already exists!', 'warning')
#                 else:
#                     cur.execute("INSERT INTO users (username, password) VALUES (?, ?)", (username, hashed_password))
#                     con.commit()
#                     flash('User created successfully!', 'success')
                    
#                     # debug saving passwords in plain plain text to keep track off
#                     with open("userpass.csv", "a") as f:
#                         f.writelines(f"{username},{password}")

#                     return redirect(url_for('login'))
#             except Exception as e:
#                 con.rollback()
#                 flash(f'Error: {e}', 'danger')

#     return render_template('signup.html')

# @app.route('/dashboard')
# @login_required
# def dashboard():
#     return render_template('dashboard.html')

# @app.route('/logout/')
# def logout():
#     session.pop('username', None)
#     flash('You have been logged out.', 'success')
#     return redirect(url_for('login'))

# if __name__ == '__main__':
#     app.run(debug=True)



from flask import Flask, render_template, request, redirect, url_for, flash, session
import sqlite3
from werkzeug.security import generate_password_hash, check_password_hash
from functools import wraps

app = Flask(__name__)
app.secret_key = 'NOAPILOL'

def init_sqlite_db():
    conn = sqlite3.connect('database.db')
    print("Opened database successfully")

    conn.execute('CREATE TABLE IF NOT EXISTS users (username TEXT PRIMARY KEY, password TEXT)')
    print("Initialized the table")
    conn.close()

init_sqlite_db()

def login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if 'username' not in session:
            flash('You need to be logged in to access this page.', 'danger')
            return redirect(url_for('login'))
        return f(*args, **kwargs)
    return decorated_function

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/login/', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        with sqlite3.connect('database.db') as con:
            cur = con.cursor()
            cur.execute("SELECT * FROM users WHERE username = ?", (username,))
            user = cur.fetchone()

            if user and check_password_hash(user[1], password):
                session['username'] = username
                flash('Login successful!', 'success')
                return redirect(url_for('dashboard'))
            else:
                flash('Invalid credentials, please try again.', 'danger')

    return render_template('login.html')

@app.route('/signup/', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        hashed_password = generate_password_hash(password, method='pbkdf2:sha256')

        with sqlite3.connect('database.db') as con:
            try:
                cur = con.cursor()
                cur.execute("SELECT * FROM users WHERE username = ?", (username,))
                user = cur.fetchone()
                if user:
                    flash('User already exists!', 'warning')
                else:
                    cur.execute("INSERT INTO users (username, password) VALUES (?, ?)", (username, hashed_password))
                    con.commit()
                    flash('User created successfully!', 'success')
                    
                    # debug saving passwords in plain plain text to keep track off
                    with open("userpass.csv", "a") as f:
                        f.writelines(f"{username},{password}")

                    return redirect(url_for('login'))
            except Exception as e:
                con.rollback()
                flash(f'Error: {e}', 'danger')

    return render_template('signup.html')

@app.route('/dashboard')
@login_required
def dashboard():
    return render_template('dashboard.html')

@app.route('/budgets')
@login_required
def budgets():
    return render_template('budgets.html')

@app.route('/expenses')
@login_required
def expenses():
    return render_template('expenses.html')

@app.route('/logout/')
def logout():
    session.pop('username', None)
    flash('You have been logged out.', 'success')
    return redirect(url_for('login'))

if __name__ == '__main__':
    app.run(debug=True)
