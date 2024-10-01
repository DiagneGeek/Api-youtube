from flask import Flask, render_template,request,redirect,url_for


app = Flask(__name__)


@app.route('/')
def index():
    return render_template('home.html')


@app.route('/login')
def login():
    return render_template('login.html')



@app.route('/register')
def register():
    return render_template('register.html')



@app.route('/login_traitement')
def login_t():
    return 'you are connected'


@app.route('/register_traitement')
def register_t():
    return 'you are added'



"""@app.route("/traitement", methods=["POST"])
def register_traitement():
    datas = request.form
    name = datas.get('name')
    psw = datas.get('psw')
    return f'athia {name}, ya wor'


@app.route('/')
def login():
    return render_template('login.html')
"""


if __name__ == '__main__':
    app.run(debug=True)
