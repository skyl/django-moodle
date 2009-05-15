import os, sys
# Use packages?  Anyhoo, altering path at runtime...
sys.path.append('/home/skyl/projects/')
sys.path.append('/home/skyl/projects/skyl/')
# might have to be app.settings, nope
os.environ['DJANGO_SETTINGS_MODULE'] = 'skyl.settings'

import django.core.handlers.wsgi

application = django.core.handlers.wsgi.WSGIHandler()
