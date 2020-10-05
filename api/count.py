# define functions for HTTP verb methods used in rest apps

from flask_restful import Resource # convert class as resource
from flask import request
import logging as logger
from .calcs import days_between, weeks_between, months_between


class count(Resource): # Task class is inheriting from Resource class

    def get(self,choice):
        logger.debug("Inside get method of count")

        return {"Type" : "Calculating {}".format(choice)},200

    def post(self,choice):
        logger.debug("Inside post method of count")

        # retrieve data from postman body
        req_data = request.get_json()
        date1 = req_data['Date 1']
        date2 = req_data['Date 2']

        # calculation functions
        days = days_between(date1, date2)
        weeks = weeks_between(date1, date2)
        months = months_between(date1, date2)

        if choice=='days':
            return {"Days" : "{}".format(days)},200
        if choice=='weeks':
            return {"Weeks" : "{}".format(weeks)},200
        if choice=='months':
            return {"Months" : "{}".format(months)},200
        if choice=='all':
            return {
                "Days" : "{} days".format(days),
                "Weeks" : "{} weeks".format(weeks),
                "Months" : "{} months".format(months)
            },200


    def put(self,choice):
        logger.debug("Inside put method of count")
        return {"message" : "inside put method of count. CHOICE-TYPE = {}".format(choice)},200

    def delete(self,choice):
        logger.debug("Inside delete method of count")
        return {"message" : "inside delete method of count. CHOICE-TYPE = {}".format(choice)},200


# get(self,date1,date2)
# post(self,choice)
    # if choice=days
    # return xx