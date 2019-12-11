from .. import db
from sqlalchemy import Column, ForeignKey, String
from sqlalchemy_utils import UUIDType
from sqlalchemy.orm import relationship


class ProductUserAssociation(db.Model):
    __tablename__ = 'product_user_association'
    user_id = Column(UUIDType(binary=False), ForeignKey('user.id'), primary_key=True)
    product_id = Column(UUIDType(binary=False), ForeignKey('product.id'), primary_key=True)
