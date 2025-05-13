from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from db.database import Base

class Hemocentro(Base):
    __tablename__ = 'hemocentro'
    
    id = Column(Integer, primary_key=True, index=True)
    nome = Column(String(255), nullable=False)
    data = Column(DateTime, nullable=False)
    cidade = Column(String(255), nullable=False)
    tipo = Column(String(255), nullable=False)
    nivel = Column(String(255), nullable=False)