from flask import Flask, render_template, request
import process_username as pcu

app = Flask(__name__)


@app.route('/')
def index():
	return render_template('index.html', name='Hillary', ratio='65')

@app.route('/', methods=['POST'])
def index_post():
	text = request.form['text']
	user_dict = pcu.process_username(text)
	return render_template('index.html', name=user_dict['name'], ratio=user_dict['ratio'])

# @app.route('/', methods=['POST'])
# def index_post_reset():
# 	# user_dict = pcu.process_username(text)
# 	return render_template('index.html', str="test")

@app.route('/hello')
def hello():
    return render_template('hello.html',)


if __name__ == '__main__':
    app.run(debug=True)
