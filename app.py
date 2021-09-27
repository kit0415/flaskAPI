from flask import Blueprint
from flask_restful import Api
#from controller.Category import CategoryResource

from controller.Hello import Hello


api_bp = Blueprint('api',__name__)
api = Api(api_bp)


#Routes
api.add_resource(Hello,'/Hi')
#api.add_resource(CategoryResource,'/Category')