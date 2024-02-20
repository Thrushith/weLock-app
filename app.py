from flask import Flask, render_template, request, redirect, session, url_for, jsonify
import sqlite3

app = Flask(__name__)
app.secret_key = 'your_secret_key'

# Database initialization
def init_db():
    conn = sqlite3.connect('database.db')
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS text_data (id INTEGER PRIMARY KEY AUTOINCREMENT, heading TEXT, content TEXT)''')
    conn.commit()
    conn.close()

init_db()

# Login route
@app.route('/', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        if request.form['username'] == 'rushi' and request.form['password'] == '123':
            session['logged_in'] = True
            return redirect(url_for('dashboard'))
        else:
            return 'Invalid login'
    return render_template('login.html')

# Dashboard route
@app.route('/dashboard', methods=['GET', 'POST'])
def dashboard():
    if not session.get('logged_in'):
        return redirect(url_for('login'))
    
    conn = sqlite3.connect('database.db')
    c = conn.cursor()

    if request.method == 'POST':
        heading = request.form['heading']
        content = request.form['content']
        c.execute('INSERT INTO text_data (heading, content) VALUES (?, ?)', (heading, content))
        conn.commit()

    c.execute('SELECT * FROM text_data')
    data = c.fetchall()
    conn.close()
    return render_template('dashboard.html', data=data)

# Delete individual data route
@app.route('/delete_data/<int:data_id>', methods=['POST'])
def delete_data(data_id):
    conn = sqlite3.connect('database.db')
    c = conn.cursor()
    c.execute('DELETE FROM text_data WHERE id=?', (data_id,))
    conn.commit()
    conn.close()
    return redirect(url_for('dashboard'))


# Logout route
@app.route('/logout')
def logout():
    session.pop('logged_in', None)
    return redirect(url_for('login'))

if __name__ == '__main__':
    app.run(debug=True)
