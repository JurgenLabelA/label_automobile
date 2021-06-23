from pyramid.view import view_defaults, view_config

from label_automobile.models.order import Order


@view_defaults(renderer='json')
class OrderView:
    def __init__(self, request):
        self.request = request
        self.session = request.dbsession

    @view_config(route_name='order.create')
    def create(self):
        sc_id = self.request.params.get('sc_id', None)
        delivery_date = self.request.params.get('delivery_date', None)
        address = self.request.params.get('address', None)

        if sc_id and delivery_date and address:
            order = Order(
                shopping_cart_id=sc_id, 
                delivery_datetime=delivery_date,
                address=address)
            self.session.add(order)

            return {

            }
        else:
            return {

            }

    @view_config(route_name='user.list')
    def list(self):
        return [{
            "Delivery date": order.delivery_datetime,
            "Delivery address": order.address,
        } for order in self.session.query(Order).all()]

    @view_config(route_name='order.delete')
    def delete(self):
        
        order_id = self.request.params.get('order_id', None)
        relevant_order = self.session.query(Order).get(order_id)
        self.session.delete(relevant_order)

        return {'Message': 'Success!'}
