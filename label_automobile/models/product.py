from sqlalchemy import Column, String, Integer, Boolean, DateTime, ForeignKey
from sqlalchemy.orm import relationship

from label_automobile.models.meta import Base, BaseModel


class Product(BaseModel, Base):
    __tablename__ = 'product'

    name = Column(String, nullable=False)
    description = Column(String, nullable=True)
    price = Column(Integer, nullable=False)
    
    shopping_cart = relationship('ShoppingCart', secondary='sc_product', backref='product')

    def __init__(self, name='No name', description= None, price=0):

        self.name = name
        self.description = description
        self.price = price

    def serialize(self):

        return {
            'Product name': self.name,
            'Product description': self.description,
            'Product price': self.price,
        }
    