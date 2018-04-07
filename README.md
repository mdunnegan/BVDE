Prerequisites:

Python 3.6, Flask

Python 3.6 can be downloaded here: https://www.python.org/downloads/
Flask can be downloaded here: https://pypi.python.org/pypi/Flask/0.12.2
Note: PIP can be downloaded here: https://pip.pypa.io/en/stable/installing/
Note: If Python 3.6 is not your active version of python `python` commands with `python3`

Running the web service:

Start the service by running `python ws.py`
The service will be available on Localhost, port 5000: http://127.0.0.1:5000/

Additional questions:

I'm not sure artist or song names will ever be close to 1024 characters. This could probably be shortened to 64, safely
Otherwise, the structure of the data seems good. There are relatively few genres compared to artist names or song names, so genres deserves it's own table

I would index songs.title, songs.artist, songs.duration, and genres.name, as these are the columns that get searched on. Many indexes reduce write performance, but this API doesn't support writes.


