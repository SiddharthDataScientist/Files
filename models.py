
from database import Base
from sqlalchemy import Integer, String, Column, Boolean, DateTime

class File(Base):
    __tablename__ = 'project'
    
    id = Column(Integer, primary_key=True, GENERATED_BY_DEFAULT = True)
    date = Column(DateTime)
    filename = Column(String)
    location = Column(String)


    # id = Column(Integer, primary_key=True, index=True)
    # date_ = Column(String)
    # filename = Column(String)

