


from flask import Flask, render_template, request, redirect, url_for, session

app = Flask(__name__)
app.secret_key = 'Latha@2004'  # Set a secret key for session management

# Define login credentials
USERNAME = 'nesha'
PASSWORD = 'nesha2810'

@app.route('/', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        if username == USERNAME and password == PASSWORD:
            session['logged_in'] = True  # Set session when login is successful
            return redirect(url_for('happy_birthday_to_moon'))
        else:
            return "Invalid credentials. Try again."
    return render_template('login.html')

@app.route('/happy_birthday_to_moon')
def happy_birthday_to_moon():
    if not session.get('logged_in'):  # Check if user is logged in
        return redirect(url_for('login'))
    return render_template('happy_birthday_to_moon.html')

@app.route('/logout')
def logout():
    session.pop('logged_in', None)  # Remove session on logout
    return redirect(url_for('login'))

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8000, debug=False)

