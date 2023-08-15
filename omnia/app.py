from flask import Flask, render_template, request
import smtplib

app = Flask(__name__)
app.static_folder = 'static'  # Make sure this is correctly set

@app.route('/about')
def about():
    return render_template('about.html')


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        first_name = request.form['firstName']
        last_name = request.form['lastName']
        email = request.form['email']
        print(first_name, last_name, email)
        # Send email
        send_email(first_name, last_name, email)
        print('email sent')
        return render_template('index.html', email_sent=True)

    return render_template('index.html', email_sent=False)

def send_email(first_name, last_name, email):
    sender_email = 'saatvik4400@gmail.com'
    sender_password = 'njofbpawwjkncvsz'

    subject = 'Welcome to Omnia'
    message = f'Hello {first_name} {last_name},\n\nThank you for signing up at Omnia!'

    try:
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(sender_email, sender_password)
        server.sendmail(sender_email, email, f'Subject: {subject}\n\n{message}')
        server.quit()
    except Exception as e:
        print('Error sending email:', e)

if __name__ == '__main__':
    app.run(host='0.0.0.0')
