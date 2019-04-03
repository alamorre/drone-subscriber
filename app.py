from flask import Flask

app = Flask(__name__)

@app.route('/', methods=["GET","POST"])
def index():
    if request.method == "POST":
        print('posted')
        return 'Post world'
    else:
        print('getted')
        return 'Get world'


if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0")

