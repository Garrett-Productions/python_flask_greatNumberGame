from flask import Flask, render_template, request, redirect, session
app = Flask(__name__)
app.secret_key = "shredthegnarrrrrrr"

import random 

# print(random.randint(1, 100))
randomNumber = random.randint(1,100)
print(randomNumber)

@app.route("/")
def index():
    return render_template("index.html",randomNumber = randomNumber)


@app.route("/process", methods=["POST"])
def process():
    print(request.form)
    print(randomNumber)
    session['number'] = int(request.form['number'])
    print("hey im here and this is what's in session", session['number'])
    return redirect("/")


@app.route("/submission")
def show():
    return render_template("/")


@app.route("/clear")
def clearSession():
    session.clear()
    return redirect("/")


if __name__ == "__main__":
    app.run(debug=True, port = 5001)
    
    
    #Let's add a separate method that will be solely responsible 
    #for rendering the show page, and then change the last line of our 
    #method handling the POST data from render_template to redirect to the 
    #route that will render the page:

#TAKEWAYAS FROM WORKING W CADEN

#the import random number I can use, I need to capture it a var to then use it in my templates and methods
#I carried my Var called "randomNumber" into my ("/") route by declaring it as a var in the return statement in the ("/") route