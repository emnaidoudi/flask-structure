from flask import Blueprint

dashboard = Blueprint('dashboard', __name__)

@dashboard.route("/gender")
def easyrun():
    return "<h1>gender distribution</h1>"


@dashboard.route("/contarct-type")
def core():
    return "<h1>CDI ...</h1>"    
