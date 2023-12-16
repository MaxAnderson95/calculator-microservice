import datetime
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy import Column, Integer, Float, String, DateTime, Boolean
from config import settings

if settings.get("DB_URL"):
    engine = create_engine(settings.DB_URL)
else:
    engine = create_engine(
        f"postgresql://{settings.DB_USER}:{settings.DB_PASSWORD}@{settings.DB_HOST}:{settings.DB_PORT}/{settings.DB_NAME}"
    )

Session = sessionmaker(bind=engine)


class Base(DeclarativeBase):
    pass


class CalculationLogEntry(Base):
    __tablename__ = 'calculation_log'
    id = Column(Integer, primary_key=True)
    operation = Column(String)
    num1 = Column(Float)
    num2 = Column(Float)
    result = Column(Float)
    cache_hit = Column(Boolean)
    created_at = Column(DateTime, default=datetime.datetime.utcnow)


Base.metadata.create_all(engine)
