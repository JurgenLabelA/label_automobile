from pyramid.view import view_defaults, view_config

from label_automobile.models.product import Product


@view_defaults(renderer='json')
class ProductView:
    def __init__(self, request):
        self.request = request
        self.session = request.dbsession

    @view_config(route_name='product.create')
    def create(self):
        
        name = self.request.params.get('name')
        description = self.request.params.get('description')
        price = self.request.params.get('price')

        if name and price:
            new_product = Product(name= name, description= description, price= price)
            self.session.add(new_product)
            return new_product.serialize()
        else:
            return {'Message': 'Missing arguments'}

    @view_config(route_name='product.list')
    def list(self):
        return [product.serialize() for product in self.session.query(Product).all()]

    @view_config(route_name='product.details')
    def delete(self):
        
        product_id = self.request.params.get('product_id')
        relevant_product = self.session.query(Product).get(product_id)

        return relevant_product.serialize()