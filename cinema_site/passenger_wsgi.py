import sys, os
INTERP = os.path.expanduser("~/venv/bin/python3")

if sys.executable != INTERP: os.execl(INTERP, INTERP, *sys.argv)

from project.wsgi import application