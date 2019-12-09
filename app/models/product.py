from .. import db
from sqlalchemy import Column, String, Integer
from sqlalchemy_utils import UUIDType


class Product(db.Model):
    __tablename__ = 'product'

    id = Column(UUIDType(binary=False), primary_key=True)
    name = Column(String(100), nullable=False, index=True)
    price = Column(Integer(), nullable=False)
    condition = Column(String(500), nullable=False)
    description = Column(String(2000))
