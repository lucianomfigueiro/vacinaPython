from flask import Flask, jsonify
from flask_restful import Resource,Api

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///banco.db'
app.config['SQALCHEMY_TRACK_MODIFICATIONS'] = False
api = Api(app)

class HelloWorld(Resource):
    def get(self):
        return {'hello': 'world'}

api.add_resource(HelloWorld, '/')

@app.before_first_request
def cria_banco():
    banco.create_all()

if __name__ == '__main__':
    from sql_alchemy import banco
    banco.init_app(app)
    app.run(debug=True)