# Import the Flask app instance from app package
from app import app     

import config


if __name__ == '__main__' :
    print(f'Jottings App is Jamming on port: {config.PORT}')
    app.run(debug = True, port = config.PORT)




''''
In `run.py`, we're importing the `app` object from the `app` package and running 
the Flask development server on the specified port from the `config.py` file
'''
