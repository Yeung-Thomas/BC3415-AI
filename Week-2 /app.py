# Backend for index.html

from flask import Flask, request, render_template

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])

# Create function
def index(): 
    if request.method == "POST":
        rate = float(request.form.get("rate"))
        return(render_template("index.html", result=(rate * -50.6)+90.2))
    else:
        return(render_template("index.html", result="Waiting for rate"))
    
if __name__ == "__main__":
    app.run()
    
# (__name__) confirms identity
# __name__ == "__main__" confirms that you want to launch code
# in index(), float() is required to transfer text to number
