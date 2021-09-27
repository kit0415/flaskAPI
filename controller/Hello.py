from flask_restful import Resource
from flask import request
from datetime import date

class Hello(Resource):
    def get(self):
        
        return {'status': 'success', 'data': "HI"}, 200

    def post(self):
        json_data = request.get_json(force=True)
        if not json_data:
            return {'message': 'No input data provided'}, 400
        # Validate and deserialize input
        

        result = {
            "method":"post",
            "invokeDateTime": date.today()
        }

        return {"status": 'success', 'data': result}, 201

    def put(self):
        json_data = request.get_json(force=True)
        if not json_data:
            return {'message': 'No input data provided'}, 400
        # Validate and deserialize input
       

        result = {
            "method":"put",
            "invokeDateTime": date.today()
        }

        return {"status": 'success', 'data': result}, 204

    def delete(self):
        json_data = request.get_json(force=True)
        if not json_data:
            return {'message': 'No input data provided'}, 400
        # Validate and deserialize input
      

        result = {
            "method":"delete",
            "invokeDateTime": date.today()
        }

        return {"status": 'success', 'data': result}, 204