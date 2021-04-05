#!/user/bin/python3
import sys
sys.path.insert(0, "/var/www/lauma_plau10_rma10/")
sys.path.insert(0, "/var/www/lauma_plau10_rma10/app/")

import logging
logging.basicConfig(stream=sys.stderr)

from app import app as application
