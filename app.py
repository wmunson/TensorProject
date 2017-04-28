from flask import Flask, request, render_template
from config import DevConfig
from model import make_test_csv, run_analysis
import json
from flask_cors import CORS, cross_origin



app = Flask(__name__)
CORS(app)
app.config.from_object("config.DevConfig")

# db = SQLAlchemy(app)







@app.route('/', methods=['GET'])
def show_homepage():
	return render_template('main.html')

@app.route('/analyze', methods=['GET'])
def show_results():
	data = request.args.get('link')
	count = make_test_csv(data)
	# print(type(count))
	result = run_analysis()
	# print(type(result))
	obj={'words':count,'result':float(result)}
	return json.dumps(obj)

# @app.route



if __name__ == "__main__":
	# YOU CAN CHOOSE WHICH PORT IS BEST
	app.run(debug=True, port=8000)