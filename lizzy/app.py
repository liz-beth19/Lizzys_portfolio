from flask import Flask, render_template, request, redirect, url_for
import csv,sqlite3

app = Flask(__name__)

# Function to write form submissions to the CSV file
def write_to_database(name,email,tel,message):
    conn = sqlite3.connect('submission.db')
    cursor = conn.cursor()
    query = "INSERT INTO contact_form (name,email,tel,message) VALUEs (?,?,?,?)"
    cursor.execute(query,(name,email,tel,message))
    conn.commit()
    conn.close()
    

    

@app.route('/')
def index():
    return render_template('homepage.html')

@app.route('/about')
def about():
    return render_template('aboutme.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/submit', methods=['POST',"GET"])
def submit():
    if request.method == 'POST':
        name = request.form.get('name')
        email = request.form.get('email')
        tel = request.form.get('tel')
        message = request.form.get('message')

        # Store form data in CSV file
        write_to_database(name,email,tel,message)

        # Redirect to a success page
        return redirect(url_for('success'))
    else:
        return "Error occured"

    return render_template('contact.html')

@app.route('/success')
def success():
    return render_template('success.html')

if __name__ == '__main__':
    app.run(debug=True)
