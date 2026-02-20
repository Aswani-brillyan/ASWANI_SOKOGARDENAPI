from flask import *
import pymysql 



app=Flask(__name__)


@app.route("/api/signup",methods=["POST"])
def signup():
    # code to excecute
    username =request.form['username']
    email=request.form['email']
    phone=request.form['phone']
    password=request.form['password']

    print(username,email,phone,password)
    # created db connection
    connection = pymysql.connect(host='localhost',user='root',password='',database="aswani_sokogarden")
    # create cursor
    cursor=connection.cursor()
    # create sql query
    sql="insert into users (username,email,phone,password) values(%s,%s,%s,%s)"
    data = (username, email, phone,password)

    cursor.execute(sql,data)

    connection.commit()

    # return
    return jsonify({"message":"Sign up api"})





if __name__=="__main__":
    app.run(debug=True)