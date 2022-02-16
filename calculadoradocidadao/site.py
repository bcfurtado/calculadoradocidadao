from flask import Flask
from flask_restful import Api

from calculadoradocidadao.views import HomeView, CorrigirPelaSelicView


app = Flask(__name__)
api = Api(app)

api.add_resource(HomeView, '/')
api.add_resource(CorrigirPelaSelicView, '/corrigirpelaselic')
