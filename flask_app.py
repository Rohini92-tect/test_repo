from flask import Flask, request
from flask_restful import Resource, Api
import os
from flask_router import FlaskRouter
from app.Main import Main


app = Flask(__name__)
api = Api(app)

class Generic(Resource):
    def post(self):
        post_data  = request.get_json()
        body = post_data.get('body')
        header = post_data.get('header')
        action = post_data.get('action')
        router = FlaskRouter(action, "", body,header, {}, {})
        event = router.load()
        print(event,"event")
        data = Main.run(event)
        http_code = data['meta']['status']
        return data, http_code
    
api.add_resource(Generic, "/generic")

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(debug=True,host='0.0.0.0', port=True)

