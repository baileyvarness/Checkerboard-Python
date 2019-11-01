from flask import Flask, render_template
app = Flask(__name__)



@app.route('/')
def checkerboard():
    print("Checking CSS")
    return render_template("index.html")

@app.route('/<times>')
def adding_rows(times):
    print("Server Stuff")
    return render_template("eight_by_four.html", num_times=int(times))



if __name__=="__main__":
    app.run(debug=True)

# @app.route('/play/<times>/<color>')
# def play_adding_box_color(times,color):
#     print("Server Stuff")
#     #return "Hello"
#     return render_template("box_color.html", num_times=int(times), box_color=(color))