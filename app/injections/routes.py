from flask import Blueprint
import pymongo as pm
import pandas as pd
import datetime
from bson.dbref import DBRef
from flask import Flask,request


injections = Blueprint('injections', __name__)

@injections.route("/easyrun")
def easyrun():
    return "<h1>Injections for easyrun</h1>"


@injections.route("/core")
def core():
    return "<h1>Injections for core</h1>"    



        
 