from flask import Flask
import logging as logger

logger.basicConfig(level="DEBUG")

# create flask instance
flaskAppInstance = Flask(__name__)

# when file is run with python interpreter, code in this block
# will run
if __name__ == '__main__':
    logger.debug("Staring the application")
    from api import *
    flaskAppInstance.run(host="0.0.0.0",port=5000,debug=True,use_reloader=True) # 0.0.0.0 can accept request from any server
    