import json
import pickle
from sklearn.ensemble import RandomForestRegressor
import category_encoders
import numpy as np
from flask_cors import CORS
from flask import Flask, request
import pandas as pd


app = Flask(__name__)
CORS(app)
@app.route("/", methods=['POST'])
def address():
    '''Takes json dictionaries and return prediction values'''

    # receive input
    inputs = request.get_json(force=True)

    # get data from json
    year = inputs['year']
    month = inputs['month']
    day = inputs['day']
    home_name = inputs['home_name']
    home_rank = inputs['home_rank']
    away_name = inputs['away_name']
    away_rank = inputs['away_rank']

    # unpickle
    filename = "pipe.pkl"
    infile = open(filename, "rb")
    model = pickle.load(infile)
    infile.close()

    cols = ['year', 'month', 'day', 'home_name',
            'home_rank', 'away_name', 'away_rank']
    feats = [year, month, day, home_name, home_rank, away_name, away_rank]

    df = pd.DataFrame(feats).T
    df.columns = cols

    # predict
    score = model.predict(df)

    # use a dictionary to format output for json
    out = {'home_score': score[0][0],
           'away_score': score[0][1]}

    # give output to sender
    return app.response_class(
        response=json.dumps(out),
        status=200,
        mimetype='application/json'
    )


if __name__ == '__main__':
    app.run(port=9000, debug=True)
