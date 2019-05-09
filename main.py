from app.app import app
from requests import get, post


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')


