import sys 
import os
sys.path.append(os.path.abspath("/home/ubuntu/qualtrics-raven"))

activate_this = '/home/ubuntu/qualtrics-raven/venv/bin/activate_this.py'
execfile(activate_this, dict(__file__=activate_this))

from survey import app as application
