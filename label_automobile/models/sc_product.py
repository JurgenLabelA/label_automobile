from sqlalchemy import Column, String, Integer, Boolean, DateTime, ForeignKey
from sqlalchemy.orm import relationship

from label_automobile.models.meta import Base, BaseModel

class ScProduct(BaseModel, Base):
    __tablename__ = 'sc_product'

    sc_id = Column(ForeignKey('shopping_cart.id'), nullable=False)
    product_id = Column(ForeignKey('product.id'), nullable=False)
