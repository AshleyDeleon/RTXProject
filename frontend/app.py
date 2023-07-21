from flask import Flask, render_template, request, redirect

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        # Process the user input as needed
        print('Email:', email)
        print('Password:', password)
        # You can store the email and password in a database or perform other actions here
        return redirect('/success')  # Redirect to a success page or any other desired page
    return render_template('home.html')

@app.route('/success')
def success():
    return "Login Successful!"  # Display a success message or render a success template

if __name__ == '__main__':
    app.run(debug=True, port=9000)
 