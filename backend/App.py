from flask import Flask, json
from flask_cors import CORS
from flask_restful import Api, reqparse
from Problems import *
from Tools import *

app = Flask(__name__)
cors = CORS(app)
api = Api(app)


@app.route('/solve', methods=['GET'])
def problems_get():
  parser = reqparse.RequestParser()
  parser.add_argument('problem', required=True, type=int)
  parser.add_argument('input', required=True, type=int)
  args = parser.parse_args()
  problemNum = args['problem']
  param = args['input']
  solutionName = 'solve_' + '{:0>3}'.format(problemNum) + '(' + str(param) + ')'
  # Note: This is a dangerous use of 'exec' by including user input. Do not use this in any sort of production environment!
  # It also has a silly misuse of a global variable, but exec doesn't return anything so I had to get the results back somehow
  print(solutionName)
  exec(f"""locals()['returnVal'] = {solutionName}""")
  print(locals()['returnVal'])
  result = locals()['returnVal']
  return app.response_class(response=json.dumps(result), status=200, mimetype='application/json')


@app.route('/tools', methods=['GET'])
def tools_get():
  parser = reqparse.RequestParser()
  parser.add_argument('n', required=True, type=int)
  args = parser.parse_args()
  result = getNthPrimeNumber(args['n'])
  return app.response_class(response=json.dumps(result), status=200, mimetype='application/json')


if __name__ == '__main__':
    app.run()
