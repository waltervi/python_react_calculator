from app.db import get_db 
import sqlite3
from datetime import datetime,timezone
from ..dao.user_dao import user_dao

# -- Record
# -- ○ id
# -- ○ operation_id
# -- ○ user_id
# -- ○ amount
# -- ○ user_balance 
# -- ○ operation_response
# -- ○ date 

class RecordDAO:
    # Besides inserting a new record , this method returns the updated balance
    def insert(self,operation_id, user_id, amount, result):
        errorMessage = None
        try:
            db = get_db()
            cur = db.cursor()
            cur.execute("begin")
            
            updated_balance, errorMessage = user_dao.validate_and_calculate_balance(db, user_id, amount)
            if errorMessage is not None:
                cur.execute("rollback")
                return None,errorMessage

            #Now update the user, then insert the new operation
            user_dao.update_user_balance(cur, updated_balance, user_id)

            date = datetime.now(timezone.utc)
            cur.execute("INSERT INTO record (operation_id, user_id, amount, user_balance, operation_response, date) VALUES (?,?,?,?,?,?)",
                    (operation_id, user_id, amount, updated_balance, result, date),)
            
            cur.execute("commit")
            
        except sqlite3.Error as err:
            cur.execute("rollback")
            errorMessage = err.args[0]
                    
        return updated_balance, errorMessage 
 
    def find_all_by_user_id(self,user_id,last_id= None,page_size=None):
        result = None
        errorMessage = None
        try:
            last_id = 0 if last_id == None else last_id
            page_size = 1000 if page_size == None else page_size
            
            result = get_db().execute("SELECT r.*,o.type FROM record r left join operation o ON r.operation_id = o.id WHERE r.user_id = ? AND r.id > ? AND r.deleted IS NULL ORDER BY r.date DESC LIMIT ?", (user_id,last_id,page_size)).fetchall()
        except sqlite3.Error as err:
            errorMessage = err.message
            
        return (result,errorMessage)
    
    def delete(self,user_id, operationId):
        errorMessage = None    
        try:
            date = datetime.now(timezone.utc)
            get_db().execute("UPDATE record SET deleted = ? WHERE user_id = ? AND id = ?", (date,user_id,operationId))
        except sqlite3.Error as err:
            errorMessage = err.message
        
        return errorMessage     
    
record_dao = RecordDAO()    