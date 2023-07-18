from app.db import get_db 
import sqlite3
from datetime import datetime,timezone
# -- Operation
# -- ○ id
# -- ○ type (addition, subtraction, multiplication, division, square_root, random_string) 
# -- ○ cost 
class OperationDAO:
    def find_by_type(self,type):
        result = None
        errorMessage = None    
        try:
            result = get_db().execute("SELECT * FROM operation WHERE type = ?", (type,)).fetchone()
        except sqlite3.Error as err:
            errorMessage = err.message
        
        result = dict(result) if result is not None else result    
        return (result,errorMessage) 
    

    

operation_dao = OperationDAO()    