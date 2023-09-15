from flask import Flask, render_template

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
db = SQLAlchemy(app)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    credits = db.Column(db.Integer, default=0)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/buy', methods=['POST'])
def buy_credit():
    user = User.query.first()
    user.credits += 1
    db.session.commit()
    return redirect('/')

@app.route('/sell', methods=['POST'])
def sell_credit():
    user = User.query.first()
    if user.credits > 0:
        user.credits -= 1
        db.session.commit()
    return redirect('/')

if __name__ == '__main__':
    db.create_all()
    app.run(debug=True)
