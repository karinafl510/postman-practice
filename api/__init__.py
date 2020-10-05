from flask_restful import Api

from app import flaskAppInstance
#from .Task import Task
from .count import count

restServer = Api(flaskAppInstance) 

restServer.add_resource(count,"/api/v1.0/task/<string:choice>") # create resource in flask restful application

