# qualtrics-raven

This python flask package creates a [Raven](https://raven.cam.ac.uk) interface for [Qualtrics](https://cambridge.eu.qualtrics.com) surveys. Raven is the authentication mechanism used by the University of Cambridge (it's a bit like, but not identical to, Shibboleth).

Users accessing the site will be asked to log in using their Raven credentials. Once correctly authenticated they'll be redirected to a pre-configured Qualtrics survey.

The package constructs an OAuth-style token containing the CRSID of the user which it passes to Qualtrics. The survey can then be configured to collect this value and store it with the survey results.

It's built on Daniel Richman's [Flask_raven](https://github.com/danielchatfield/flask-raven) package.

## Usage

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

## Details

Qualtrics provides a myriad different authentication techniques, which are useful for limiting the pool of people who can complete a survey, as well as avoiding users having to enter basic details that are already made available by the authentication system (e.g. email address).

Of the techniques supported, Shibboleth is the only type provided by the University of Cambridge's Raven SSO system, and sadly the University hasn't paid for the licence to use it with Qualtrics.

Happily Qualtrics does also provided a 'token' approach. This allows any service to generate a token using a shared secret (known only to the service and Qualtrics) to allow access to a particular survey. The token can also contain extra information which can be stored with the form.

Brief and high-level details can be found on Qualtrics [SSO help page](http://www.qualtrics.com/university/researchsuite/advanced-building/survey-flow/authenticator/sso-authentication/#Token). More details of the token format are in the Qualtrics [SSO specification](http://www.qualtrics.com/wp-content/uploads/2013/05/SSO-Single-Sign-On-Specification.pdf) document. The long and short of it is that the token should be structured like this:
```
b64enc( encrypt(key, body | "&mac=" | b64enc( hmac(key, body)) | paddding))
```
Where:
 - `b64enc` is a base64 ecoder.
 - `encrypt` is an encryption function (SHA128, Blowfish or 3DES).
 - `key` is the shared secret.
 - `body` is a text string of key-value pairs (see below).
 - `hmac` is a secure hash function (MD5, SHA1, SHA256 or SHA512).
 - `padding` is a sequence of zero bytes to round the length up to that required by the block cipher.

Qualtrics-raven uses SHA128 for encryption and SHA256 for the HMAC. The padding rounds up to the nearest 16 bytes.

The `body` is a sequence of key-value pairs separated by ampersands (just like a URL parameter list). This much include a timestamp and expiration time in the following format `%Y-%m-%dT%H:%M:%S`. In addition, we include a `crsid` field that passes the users's CRSID to Qualtrics. For example, it might look like this:
```
crsid=dl551&timestamp=2016-02-25T20:30:22&expiration=2016-02-25T20:35:22
```

To summarise the functionality then, this mini qualtrics-raven package uses Daniel Richman's Raven client implementation to force the user to login, after which it constructs this token and sends it on to Qualtrics as athencation to access a survey. Consequently it allows members of the University to use their Raven logins to access Qualtrics surveys.
