from flask import Flask
from flask_restful import Api
from resources import Places
from resources import Tags

app = Flask(__name__)
app.debug = True
api = Api(app, catch_all_404s=True)

api.add_resource(Places, '/places')
api.add_resource(Tags, '/tags')

if __name__ == '__main__':
    app.run()
