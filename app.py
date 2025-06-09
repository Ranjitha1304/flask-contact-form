from flask import Flask, render_template, request, flash, redirect, url_for
import re

app = Flask(__name__)
app.secret_key = 'your_secret_key'

# Email validation using regex
def is_valid_email(email):
    return re.match(r"[^@]+@[^@]+\.[^@]+", email)

# Name should contain only letters and spaces
def is_valid_name(name):
    return re.match(r"^[A-Za-z\s]+$", name)

@app.route('/', methods=['GET', 'POST'])
def contact():
    name = ''
    email = ''
    message = ''

    if request.method == 'POST':
        name = request.form.get('name', '').strip()
        email = request.form.get('email', '').strip()
        message = request.form.get('message', '').strip()

        # Validation
        if not name or not email or not message:
            flash("All fields are required.", "error")
        elif len(name) < 3:
            flash("Name must be at least 3 characters long.", "error")
        elif not is_valid_name(name):
            flash("Name must contain only letters and spaces.", "error")
        elif not is_valid_email(email):
            flash("Invalid email format.", "error")
        elif len(message) < 20:
            flash("Message must be at least 20 characters long.", "error")
        else:
            flash("Your message has been sent successfully!", "success")
            return redirect(url_for('contact'))

    return render_template('contact.html', name=name, email=email, message=message)

if __name__ == '__main__':
    import os
    port = int(os.environ.get("PORT", 5000))
    app.run(debug=False, host='0.0.0.0', port=port)

