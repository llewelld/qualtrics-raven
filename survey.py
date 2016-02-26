from flask import Flask, session, redirect
from flask_raven import raven_auth
from qualtrics import tokenqualtrics
from qualtrics import config

app = Flask(__name__)

app.config.update(
    SECRET_KEY='super-secret-key'
)

@app.route('/survey/<name>')
@raven_auth()
def home(name):
    crsid = session['_raven']
    result = config.failurepage
    if crsid != None:
        print 'Header: ' + crsid
        if name in config.surveyinfo: 
            survey = config.surveyinfo[name]
            print survey.qid
            data = dict()
            data['crsid'] = crsid
            url = tokenqualtrics.gettoken(survey.qid, survey.key, data)
            result = redirect(url, 302)

    return result

if __name__ == '__main__':
    app.run(debug=True)
