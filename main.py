from app import app
#from api.py import app #This might be right?
from requests import get, post
#should we put pip install -r requirements.txt here?

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')


