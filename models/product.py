
from marshmallow_sqlalchemy import ModelSchema
from marshmallow import fields
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Product(db.Model):
    """ Protduc model """
    __tablename__ = "product"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(20))
    description = db.Column(db.String(100),nullable=False)
    brand = db.Column(db.String(20),nullable=False)
    price = db.Column(db.Float,nullable=False)

    def __str__(self):
        return self.name


class ProductSchema(ModelSchema):
    class Meta(ModelSchema.Meta):
        model = Product
        sqla_session = db.session
    id = fields.Number(dump_only=True)
    name = fields.String(required=True)
    description = fields.String(required=True)
    brand = fields.String(required=True)
    price = fields.Number(required=True)

# class ProductSchema(ModelSchema):
#     class Meta(ModelSchema.Meta):
#         fields = ("id", "name", "description","brand","price")