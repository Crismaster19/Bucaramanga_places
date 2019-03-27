from flask import Flask, request, render_template
app = Flask(__name__)
@app.route("/")
def sumar():
    return render_template("index.html")
@app.route("/restaurantes")
def restar():
    return render_template("trabajo.html")
@app.route("/mojarlasalchicha")
def multiplicar():
    return render_template("rumba.html")
    
if __name__ == "__main__":
 app.run()