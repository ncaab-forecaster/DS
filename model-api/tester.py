import json
import requests

# if you want to test local
# url = "http://localhost:9000"

# if you want to test deployed
url = "http://ncaab.herokuapp.com"

val = {"year": 2018,
       "month": 11,
       "day": 6,
       "home_name": "Kansas",
       "home_rank": 1.0,
       "away_name": "Michigan State",
       "away_rank": 10.0}

# you'll get a 200 response if the keys align
# and something bad if the keys don't align.
if __name__ == '__main__':
    r_success = requests.post(url, data=json.dumps(val))
    print(
        f"Request responded: {r_success}.\nResponse was\n{r_success.json()}")
