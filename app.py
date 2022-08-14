from flask import Flask
from studentdata import student
app=Flask(__name__)

@app.route("/students")
def ss():
    return student
@app.route("/students/21pc14")
def s1():
    return student['21pc14']
@app.route("/students/21pc22")
def s2():
    return student['21pc22']
if __name__=="__main__":
    app.run()
