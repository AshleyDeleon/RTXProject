#!curl -o paper.pdf https://www.cancer.org/content/dam/CRC/PDF/Public/6055.00.pdf 
#where the file is store, button.link or something to get the file 
#thats where insert the python code or in javascript 
#instead of pdf url, took file from device uploaded

from flask import Flask, render_template, request, redirect

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        translate1 = request.form['']
        translate2 = request.form['password']
        # Process the user input as needed
        print('translate1:', email)
        print('translate2:', password)
        # You can store the email and password in a database or perform other actions here
        return redirect('/success')  # Redirect to a success page or any other desired page
    return render_template('home.html')

@app.route('/success')
def success():
    return "Login Successful!"  # Display a success message or render a success template

if __name__ == '__main__':
    app.run(debug=True, port=8080)

    
from langchain.document_loaders import PyPDFLoader # for loading the pdf

pdf_path = "./paper.pdf"
loader = PyPDFLoader(pdf_path)
pages = loader.load_and_split()
print(pages[0].page_content)

#takes those print and translate them into a different lanuage