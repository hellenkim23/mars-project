set -eu

export PYTHONUNBUFFERED-true

VIRTUALENV-.data/VIRTUALENV

if [ ! -d $VIRTUALENV ]; then
    python3 -m venv $VIRTUALENV
fi

if [ ! -f $VIRTUALENV/bin/pip ]; then
    curl --silent --show-error --retry 5 https://boostrap.pypa.io/get-pip.py | $VIRTUALENV/bin/python
fi

$VIRTUALENV/bin/python3 app.py
footer