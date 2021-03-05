from flask import Flask, render_template, url_for, request, redirect
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)

# database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite3'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# init DB
db = SQLAlchemy(app)

class OngModel(db.Model):
    __tablename__ = 'ongs'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    email = db.Column(db.String(100))
    date_created = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self):
        return f'Ong(id={self.id}, name={self.name}, email={self.email})'


@app.route('/', methods=['POST', 'GET'])
def index():
    if request.method == "POST":
        name = request.form["name"]
        email = request.form["email"]
        ong = OngModel(name=name, email=email)
        try:
            db.session.add(ong)
            db.session.commit();
            return redirect("/")
        except:
            return "Error adding a Ong"
    else:
        ongs = OngModel.query.order_by(OngModel.date_created).all()
        return render_template("index.html", ongs=ongs)

@app.route('/delete/<int:id>')
def delete(id):
    ong = OngModel.query.get_or_404(id)

    try:
        db.session.delete(ong)
        db.session.commit()
        return redirect("/")
    except:
        return "Error deleting ONG"

@app.route('/update/<int:id>', methods=['POST', 'GET'])
def update(id):
    ong = OngModel.query.get_or_404(id)

    if request.method == 'POST':
        ong.name = request.form["name"]
        ong.email = request.form["email"]

        try:
            db.session.commit()
            return redirect('/')
        except:
            return "Error updating ONG"
    else:
        return render_template('update.html', ong=ong)


if __name__ == "__main__":
    app.run(debug = True)