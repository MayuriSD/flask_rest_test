from flask import Flask
app = Flask(__name__)         #http://localhost:5000/addition/10/20       --> same machine-> 5000 port-- wsgi - code
                                # flask -- cha syntax -->
#Flask ch  --> route -->  of course



@app.route("/addition/<int:num1>/<int:num2>")       #decorator -->     http://localhost:5000/addition/102/34
def addition(num1,num2):                            #addition(10,20)
    result = num1 + num2
    return "Addition is {}".format(result)

@app.route("/welcome")                        #http://localhost:5000/welcome  ---> welcome to Flask web application
def say_welcome():                                  #say_welcome()
    return "Welcome to Flask web application"

if __name__ == '__main__':
    app.run(debug=True)
