#!/usr/bin/python3
"""
This class City inherits BaseModel
"""

import os
from models.base_model import BaseModel
STORAGE_TYPE=os.environ.get('HBNB_TYPE_STORAGE')


class City(BaseModel):
    """
    The public class attributes should be empty
    """
    if STORAGE_TYPE == "db":
        __tablename__= 'cities'
    else:    
        state_id = ""
        name = ""
        places=[]
        
