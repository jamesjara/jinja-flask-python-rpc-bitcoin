import sys
sys.path.insert(1, '/var/www/bitcoin/app/')

activate_this = '/var/www/bitcoin/venv/bin/activate_this.py'
execfile(activate_this, dict(__file__=activate_this))

from wallet import app as application
