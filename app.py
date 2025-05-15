from flask import Flask

app = Flask(__name__)


import sqlite3
from tkinter import messagebox

from flask import Flask, render_template, request



@app.route("/")
def index():
    return render_template("index.html");

@app.route("/main")
def main():
    return render_template("index.html")

@app.route("/menu")
def menu():
    return render_template("menu.html")




@app.route("/admin")
def admin():
    return render_template("servicelogin.html")
@app.route("/cancelapp")
def cancelapp():
    return render_template("cancelapp.html")
@app.route("/reg")
def reg():
    return render_template("register.html")
@app.route("/mn")
def mn():
    return render_template("index.html")
@app.route("/bookapp" )
def bookapp():
         return render_template('bookapp.html')

@app.route("/doctdet" )
def doctdet():
         return render_template('service.html')
@app.route("/service" )
def service():
         return render_template('service.html')
@app.route("/sendsol" )
def sendsol():
         return render_template('sendsol.html')

@app.route("/userlogin")
def userlogin():
    return render_template("userlogin.html")

@app.route("/regsave", methods=["POST", "GET"])
def regsave():
    msg = "msg"
    if request.method == "POST":
        try:
            fname = request.form["fname"]
            msg = "-"
            emailid = request.form["email"]
            contact = request.form["contact"]
            model = request.form["model"]
            make = request.form["make"]
            year = request.form["year"]
            eno = request.form["eno"]
            cno = request.form["cno"]
            cc = request.form["cc"]
            pw = request.form["pw"]
            with sqlite3.connect("vehicle.db") as con:
                cur = con.cursor()
                cur.execute("INSERT into pregister (fname, emailid, contact,model,make,year,eno,cno,cc,pw) values (?,?,?,?,?,?,?,?,?,?)", (fname, emailid, contact,model,make,year,eno,cno,cc,pw))
                con.commit()
                msg = "successfully Added"
        except:
            con.rollback()
            msg = "Try Again"
        finally:

            return render_template("success.html",msg=msg)
@app.route("/query", methods=["POST", "GET"])
def query():
    msg = "msg"
    if request.method == "POST":
        try:
            fname = request.form["fname"]
            msg = "-"
            emailid = request.form["email"]
            contact = request.form["contact"]
            model = request.form["model"]
            make = request.form["make"]
            year = request.form["year"]
            eno = request.form["eno"]
            cno = request.form["cno"]
            cc = request.form["cc"]
            msg = request.form["msg"]
            with sqlite3.connect("vehicle.db") as con:
                cur = con.cursor()
                cur.execute("INSERT into query (fname, email, contact,model,make,year,eno,cno,cc,message) values (?,?,?,?,?,?,?,?,?,?)", (fname, emailid, contact,model,make,year,eno,cno,cc,msg))
                con.commit()
                msg = "successfully Added"
        except:
            con.rollback()
            msg = "Try Again"
        finally:

            return render_template("success.html",msg=msg)
@app.route("/sol", methods=["POST", "GET"])
def sol():
    msg = "msg"
    if request.method == "POST":
        try:
            fname = request.form["fname"]
            msg = "-"
            emailid = request.form["email"]
            contact = request.form["contact"]
            model = request.form["model"]
            make = request.form["make"]
            year = request.form["year"]
            eno = request.form["eno"]
            cno = request.form["cno"]
            cc = request.form["cc"]
            msg = request.form["msg"]
            with sqlite3.connect("vehicle.db") as con:
                cur = con.cursor()
                cur.execute("INSERT into sol (fname, email, contact,model,make,year,eno,cno,cc,solution) values (?,?,?,?,?,?,?,?,?,?)", (fname, emailid, contact,model,make,year,eno,cno,cc,msg))
                con.commit()
                msg = "successfully Added"
        except:
            con.rollback()
            msg = "Try Again"
        finally:

            return render_template("success.html",msg=msg)
@app.route("/dsave", methods=["POST", "GET"])
def dsave():
    msg = "msg"
    if request.method == "POST":
        try:
            dname = request.form["dname"]
            msg = "-"
            contact = request.form["contact"]
            emailid = request.form["emailid"]
            spec = request.form["spec"]
            dtime = request.form["dtime"]

            with sqlite3.connect("vehicle.db") as con:
                cur = con.cursor()
                cur.execute("INSERT into service(dname, email, contact, spec,dtime) values (?,?,?,?,?)", (dname, emailid, contact, spec,dtime))
                con.commit()
                msg = " Saved Successfully"
        except:
            con.rollback()
            msg = "Try Again"
        finally:

            return render_template("success.html",msg=msg)

@app.route("/loginfac", methods=["POST", "GET"])
def loginfac():
    msg = "msg"
    if request.method == "POST":
            un = request.form["un"]
            pw = request.form["pw"]

            with sqlite3.connect("vehicle.db") as con:

             with con:
                cur = con.cursor()
                cur.execute("SELECT * FROM pregister")
                rows = cur.fetchall()
                for row in rows:
                    dbUser = row[1]
                    dbPass = row[9]
                    if dbUser == un and dbPass==pw:
                        return render_template('sendquery.html')

@app.route("/dlogin", methods=["POST", "GET"])
def dlogin():
    msg = "msg"
    if request.method == "POST":
            un = request.form["un"]
            pw = request.form["pw"]
            if un=="":
                msg("Enter Username")
                return render_template("success.html",msg=msg)
            else:
                if pw == "":
                    msg("Enter Password")
                    return render_template("success.html", msg=msg)
                else:
                    if "admin" == un and "admin"==pw:
                        return render_template('menu.html')
@app.route("/appsave", methods=["POST", "GET"])
def appsave():
    msg5 = "msg"
    if request.method == "POST":

            fname1 = request.form["fname"]
            msg1 ="-"
            contact1 = request.form["contact"]
            emailid1 = request.form["emailid"]
            dname1 = request.form["dname"]
            adate1 = request.form["adate"]
            atime1 = request.form["atime"]
            with sqlite3.connect("vehicle.db") as con:

                appno2=1
                cur = con.cursor()
                cur.execute("SELECT * FROM bookapp")
                rows = cur.fetchall()
                for row in rows:
                    appno2 = row[7]
                appno2 =int(appno2)+1

            with sqlite3.connect("vehicle.db") as con:
                cur = con.cursor()
                cur.execute("INSERT into bookapp(fname, emailid, contact, msg,dname,adate,atime,appno) values (?,?,?,?,?,?,?,?)", (fname1, emailid1, contact1, msg1,dname1,adate1,atime1,appno2))
                con.commit()
                msg5 = "successfully Added"
            return render_template("bookapp.html")











@app.route("/viewappt")
def viewappt():
    with sqlite3.connect("vehicle.db") as con:
        with con:
            cur = con.cursor()
            cur.execute("SELECT * FROM bookapp")
            rows = cur.fetchall()
            return render_template('viewapp.html', data=rows)
        con.close()
@app.route("/viewservice")
def viewservice():
    with sqlite3.connect("vehicle.db") as con:
        with con:
            cur = con.cursor()
            cur.execute("SELECT * FROM service")
            rows = cur.fetchall()
            return render_template('viewservice.html', data=rows)
        con.close()

@app.route("/viewquery")
def viewquery():
    with sqlite3.connect("vehicle.db") as con:
        with con:
            cur = con.cursor()
            cur.execute("SELECT * FROM query")
            rows = cur.fetchall()
            return render_template('viewquery.html', data=rows)
        con.close()


@app.route("/viewsol")
def viewsol():
    with sqlite3.connect("vehicle.db") as con:
        with con:
            cur = con.cursor()
            cur.execute("SELECT * FROM sol")
            rows = cur.fetchall()
            return render_template('viewsol.html', data=rows)
        con.close()






if __name__ == '__main__':
    app.run()
