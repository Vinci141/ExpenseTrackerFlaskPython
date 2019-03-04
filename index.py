# Created By: Vinil Mehta
# Build Version 0.1
# Application Purpose: to track expense details via web app.
from distutils.command.config import config

from flask import Flask, render_template, request, url_for
import sqlite3 as sql

app = Flask( __name__ )


@app.route( '/' )
def index():
    return render_template( 'index.html' )


@app.route( '/list' )
def list():
    con = sql.connect( "database.db" )
    con.row_factory = sql.Row
    cur = con.cursor()
    cur.execute( "select * from expenses" )
    rows = cur.fetchall();
    res = cur.execute( "select category,sum(amount) from expenses group by category" )
    return render_template( "list.html", rows=rows, add=res.fetchall() )


@app.route( '/addrec', methods=['POST', 'GET'] )
def addrec():
    if request.method == "POST":
        try:
            msg = "No Records Found!"
            particulars = request.form['particulars']
            category = request.form['ct']
            amount = int( request.form['amount'] )
            date = request.form['date']
            comments = request.form['comments']
            if particulars == "" and category == "" and amount == "" and date == "":
                msg = "No data found !"
                return msg
            else:
                with sql.connect( 'database.db' )as con:
                    msg = "Connected to Database"
                    cur = con.cursor()
                    cur.execute( "INSERT INTO expenses (particulars,category,amount,date,comments) VALUES (?,?,?,?,?)",
                                 (particulars, category, amount, date, comments) )
                    con.commit()
                    msg = "Record successfully added"
                    return msg
        except:
            # handle exception here
            con.rollback()
            msg = "There occurs some failure.Please check !"
            return msg
        finally:
            return render_template( 'result.html', msg=msg )
            # return render_template(url_for('list'))


if __name__ == '__main__':
    app.run( debug=True )
