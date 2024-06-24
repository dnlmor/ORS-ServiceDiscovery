from sqlalchemy import Column, String, Integer, DateTime
from .database import Base
import datetime

class Service(Base):
    __tablename__ = 'services'
    id = Column(String, primary_key=True)
    name = Column(String, nullable=False)
    host = Column(String, nullable=False)
    port = Column(Integer, nullable=False)
    registered_at = Column(DateTime, default=datetime.datetime.utcnow)
