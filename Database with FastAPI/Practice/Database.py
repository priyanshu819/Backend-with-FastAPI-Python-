from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Create Url Link
url='sqlite:///./demo.db0'

# Create Engine
engine=create_engine(
    url,  connect_args={'check_sa_meThrede'False}
)