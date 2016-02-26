## qualtrics-raven

This python flask package creates a [Raven](https://raven.cam.ac.uk) interface for [Qualtrics](https://cambridge.eu.qualtrics.com) surveys. Raven is the authentication mechanism used by the University of Cambridge (it's a bit like, but not identical to, Shibboleth).

Users accessing the site will be asked to log in using their Raven credentials. Once correctly authenticated they'll be redirected to a pre-configured Qualtrics survey.

The package constructs an OAuth-style token containing the CRSID of the user which it passes to Qualtrics. The survey can then be configured to collect this value and store it with survey results.

It's built on Daniel Richman's [Flask_raven](https://github.com/danielchatfield/flask-raven) package.

### Usage

Edit the `qualtrics/config.py` file to add the details of your surveys. You'll need the id of your survey (you can get it from the survey URL) and the Token key (Survey Flow -> Branch on Successful Authentication -> Token).

The following should get you a simmple tests surver running.

```python
cd qualtrics-raven
python survey.py
```

The package has been configured for use with Heroku, but should work anywhere that Flask works. Something like this should work to run it locally if youu have the Heroku Toolbelt installed.

```python
cd qualtrics-raven
virtualenv venv
source venv/bin/activate
pip install -r requirements.txt
heroku local web
```


