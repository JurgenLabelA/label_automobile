from label_automobile.models.product import Product
from pyramid.view import view_defaults, view_config

from label_automobile.models.shopping_cart import ShoppingCart


@view_defaults(renderer='json')
class ShoppingCartView:
    def __init__(self, request):
        self.request = request
        self.session = request.dbsession

    @view_config(route_name='shopping_cart.create')
    def create(self):

        cart_product_id = self.request.params.get('product_id')
        auth_user_id = self.request.params.get('user_id')

        new_shopping_cart = ShoppingCart(user_id=auth_user_id)
        if cart_product_id:
            new_shopping_cart.add_product(
                self.session.query(Product).get(cart_product_id)
                )
        
        return new_shopping_cart.serialize()

    def add_product(self):

        cart_product_id = self.request.params.get('product_id')
        shopping_cart_id = self.request.params.get('sc_id')

        relevant_shopping_cart = self.session.query(ShoppingCart).get(shopping_cart_id)
        relevant_shopping_cart.add_product(
                self.session.query(Product).get(cart_product_id)
                )

        return relevant_shopping_cart.serialize()