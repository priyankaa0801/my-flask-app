from flask import Flask
render_template,request
@app.route("/")
def home():
    return render_template("Registration.html")
@app.route('/submit',method=[POST])
def submit():
    name=request.form[name]
    return render_template("Successful.html",name=name)
if __name__==__main__:
    app.run(host="0.0.0.0",port=5000)