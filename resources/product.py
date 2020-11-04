from flask import Flask, request,Response
from flask_restful import Api, Resource
from models.product import Product,ProductSchema,db
from flask_api import FlaskAPI, status

post_schema = ProductSchema()
posts_schema = ProductSchema(many=True)


class PostListResource(Resource):
    def get(self):
        posts = Product.query.all()
        return posts_schema.dump(posts)

    def post(self):
        data = request.form
        name = data['name']
        description = data['description']
        brand = data['brand']
        price = data['price']
        # product_name =  Product.query.filter_by(name=name).first()
        # if not  Product.query.filter_by(name=product_name):
        #     print("name",product)
        new_product = Product(
            name = name,
            brand = brand,
            description = description,
            price = price
            )
        db.session.add(new_product)
        db.session.commit()
        # return post_schema.dump(new_product),status.HTTP_201_CREATED
        result = post_schema.dump(new_product),status.HTTP_201_CREATED
        return {"message": "Created successfully.", "data": result}

        # else:
        #     response = {
        #         "Name already added for this product."
        #         }
        #     return Response(response,status.HTTP_400_BAD_REQUEST)


class PostResource(Resource):
    def get(self, post_id):
        post = Product.query.get_or_404(post_id)
        return post_schema.dump(post)

    def patch(self, post_id):
        data = request.form
        name = data['name']
        description = data['description']
        brand = data['brand']
        price = data['price']
        product = Product.query.get_or_404(post_id)
        product.name = name
        product.brand = brand
        product.description = description
        product.price = price
        db.session.commit()
        return post_schema.dump(product)

    def delete(self, post_id):
        post = Product.query.get_or_404(post_id)
        db.session.delete(post)
        db.session.commit()
        return f"Product with id {post_id} is deleted.",status.HTTP_200_OK

