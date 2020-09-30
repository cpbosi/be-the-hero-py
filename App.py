from flask import *
import sqlite3 

app = Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/newong')
def newong():
    return render_template("newong.html")

@app.route('/saveong', methods = ["POST", "GET"])
def saveong():
    msg = "msg"
    if request.method == "POST":
        try:
            name = request.form["name"]
            email = request.form["email"]
            whatsapp = request.form["whatsapp"]

            with sqlite3.connect("ong.db") as con:
                cur = con.cursor()
                cur.execute("INSERT into Ong (name, email, whatsapp) values (?,?,?)",(name,email,whatsapp))  
                con.commit()  
                msg = "Ong successfully Added"
        except:
            con.rollback();
            msg = "Error adding a Ong"
        finally:
            return render_template("success.html", msg = msg)
            con.close()
        
@app.route('/listong')
def listong():
    con = sqlite3.connect("ong.db")
    con.row_factory = sqlite3.Row
    cur = con.cursor()
    cur.execute("select * from Ong")
    rows = cur.fetchall()
    return render_template("listong.html", rows = rows)


@app.route('/deleteong')
def deleteong():
    return render_template("deleteong.html")

@app.route('/delete', methods = ["POST"])
def delete():
    id = request.form["id"]
    with sqlite3.connect("ong.db") as con:
        try:
            cur = con.cursor()
            cur.execute("delete from Ong where id = ?",id)  
            msg = "Ong successfully deleted"
        except:
            msg = "can't be deleted"
        finally:
            return render_template("delete.html", msg = msg)

app.run(debug = True)