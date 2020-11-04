from flask import Flask,request,url_for, flash,Response
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from flask_restful import Api, Resource
from resources.product import PostListResource,PostResource
from models.product import db

app = Flask(__name__)
# app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
# db = SQLAlchemy(app)
# ma = Marshmallow(app)
api = Api(app)
app.config['DEBUG'] = True
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///product.db'
db.init_app(app)


api.add_resource(PostListResource, '/products')
api.add_resource(PostResource, '/products/<int:post_id>')


if __name__ == '__main__':
    app.debug = True
    app.run(debug=True)
