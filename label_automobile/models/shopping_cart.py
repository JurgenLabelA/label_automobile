from sqlalchemy import Column, String, Integer, Boolean, DateTime, ForeignKey
from sqlalchemy.orm import relationship

from label_automobile.models.meta import Base, BaseModel

class ShoppingCart(BaseModel, Base):
    __tablename__ = 'shopping_cart'

    user_id = Column(ForeignKey('user.id'), nullable=False)

    order = relationship('Order', back_populates='shopping_cart', uselist=False)
    
    product = relationship('Product', secondary='sc_product', back_populates='shopping_cart')