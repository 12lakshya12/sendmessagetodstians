from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('trail.html')

@app.route('/submit', methods=['GET','POST'])
def submit():
    data = request.form
    data2 = str(data)+"\n"
    print(data)
    with open('response.txt','a') as f:
        f.write(data2)
    # do something with the data here
    return 'Data submitted anonymously!'

if __name__ == '__main__':
    app.run(debug=True)