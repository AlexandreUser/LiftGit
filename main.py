import os
from controller.MainControlle import app

if __name__ == "__main__":
	app.secret_key = os.urandom(12)
	app.run(host="0.0.0.0",port="5000",debug=True)
