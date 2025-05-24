from flask import Flask , render_template

bus_finder = Flask(__name__)
@bus_finder.route('/')
def homepage():
    return render_template ("land.html")

if __name__ == "__main__":

    bus_finder.run(debug =True, port = 7000)
    