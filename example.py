from flask import Flask, session, redirect
from flask_raven import raven_auth
from qualtrics import tokenqualtrics

app = Flask(__name__)

app.config.update(
    SECRET_KEY='super-secret-key'
)

@app.route('/survey/<surveyid>')
@raven_auth()
def home(surveyid):
    crsid = session['_raven']
    print surveyid
    if crsid != None:
        print 'Header: ' + crsid
        data = dict()
        data['crsid'] = crsid
        url = tokenqualtrics.gettoken(surveyid, data)
        result = redirect(url, 302)
    else:
        result = 'You stare into the void and blink.'
    return result

if __name__ == '__main__':
    app.run(debug=True)
