from flask import Flask , request , render_template
from collections import OrderedDict
from form import Form_validation
import os
import datetime
import time
import requests
import json
import random

app = Flask(__name__)
app.config['SECRET_KEY'] = os.urandom(24)

@app.route("/")
def hello():
    return "hello page"
@app.route('/api', methods=['GET'])
def get_information():
    form = Form_validation(request.args)
    utc_time = ""

    if form.validate():

            slack_name = form.slack_name.data
            track = form.track.data
            current_day = datetime.date.today().strftime("%A")
            utc_time = datetime.datetime.utcnow() + datetime.timedelta(seconds=random.randint(-120, 120))
            utc_time = utc_time.strftime("%Y-%m-%dT%H:%M:%SZ")
            github_file_url = "https://github.com/lyndalebdjiri/HNGInternship-stageOne/blob/77dbccdff7256e4f3375c42e88fd0455be8729c7/Backend/Run.py"
            github_repo_url = "https://github.com/lyndalebdjiri/HNGInternship-stageOne.git"
            response = requests.get("https://hnginternship-stageone.onrender.com", params={"slack_name": slack_name, "track": track})
            status_code = response.status_code

            response_data = {
                "slack_name": slack_name,
                "current_day": current_day,
                "utc_time": utc_time,
                "track": track,
                "github_file_url": github_file_url,
                "github_repo_url": github_repo_url,
                "status_code": status_code,
            }
            response = json.dumps(response_data, sort_keys=False)
            return response
    else:
            print(f'{form.errors}')
    return render_template("html/form.html",form=form)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000,debug = True)
