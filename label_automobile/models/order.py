from sqlalchemy import Column, String, Boolean, DateTime, ForeignKey
from sqlalchemy.orm import relationship

from label_automobile.models.meta import Base, BaseModel


class Order(BaseModel, Base):
    __tablename__ = 'order'
    
    shopping_cart_id = Column(ForeignKey('shopping_cart.id'), nullable=False)
    delivery_datetime = Column(DateTime(timezone=True), nullable=False)
    address = Column(String, nullable=False)

    shopping_cart = relationship("ShoppingCart", back_populates="order", uselist=False)

    def __init__(self, shopping_cart_id, delivery_datetime, address):

        self.shopping_cart_id = shopping_cart_id
        self.delivery_datetime = delivery_datetime
        self.address = address
    