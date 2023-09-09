from flask import Flask , request , render_template , jsonify
from form import Form_validation
import os
import datetime
import time
import requests


app = Flask(__name__)
app.config['SECRET_KEY'] = os.urandom(24)


@app.route('/', methods=['GET'])
def get_information():
    form = Form_validation(request.args)
    utc_time = ""

    if form.validate():

            slack_name = form.slack_name.data
            track = form.track.data
            current_day = datetime.date.today().strftime("%A")
            utc_time = time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime())
            github_file_url = "https://github.com/lyndalebdjiri/stageOneHNGX/blob/cd68c8d5a4852df358ed37064c8220da634ed570/Backend/Run.py"
            github_repo_url = "https://github.com/lyndalebdjiri/HNGInternship-stageOne.git"
            response = requests.get("http://example.com/api", params={"slack_name": slack_name, "track": track})
            status_code = response.status_cod

            response = {
                "slack_name": slack_name,
                "current_day": current_day,
                "utc_time": utc_time,
                "track": track,
                "github_file_url": github_file_url,
                "github_repo_url": github_repo_url,
                "status_code":status_code ,
            }
            return jsonify(response)
    else:
        print(f'{form.errors}')
    return render_template("html/form.html",form=form)


if __name__ == '__main__':
    app.run(debug = True)
