from flask import Flask, render_template

app = Flask(__name__)

arr = ['arson', 'bangle', 'clinche', 42]

@app.route('/user/<name>')
def user(name):
    # return "<h1>Hello {}</h1>".format(name)
    tg = "<h1>AH one tag </h1>"
    text = "igoekldsvgnoev"
    return render_template('user.html', name=name, hh = tg, text=text, arr=arr)

@app.route('/')
def hello_world():  # put application's code here
    return 'Hello World!'

# custom pages with errors
@app.errorhandler(404)
def page_with_error(e):
    return render_template('er.html'), 404

@app.errorhandler(500)
def page_with_error(e):
    return render_template('noserver.html'), 500



@app.errorhandler(502)
def page_with_error(e):
    return render_template('502.html'), 502



if __name__ == '__main__':
    app.run()
