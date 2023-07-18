from app.db import get_db 
import sqlite3

# -- User
# -- ○ id
# -- ○ username (email)
# -- ○ password
# -- ○ status (active, inactive)
# -- ○ current_balance (Moved from Record to this table)
 

class UserDAO:
    def find_by_username (self,username):
        result = None
        errorMessage = None    
        try:
            result = get_db().execute("SELECT * FROM user WHERE username = ?", (username,)).fetchone()
        except sqlite3.Error as err:
            errorMessage = err.message
    
        result = dict(result) if result is not None else result 
        return (result,errorMessage)

    def insert(self,username, password):
        errorMessage = None
        try:
            db = get_db()
            cur = db.cursor()
            cur.execute("begin")
            cur.execute("INSERT INTO user (username, password,status,user_balance) VALUES (?,?,?,?)",(username, password,0,1000),)
            cur.execute("commit")
        except db.IntegrityError:
            # The username was already taken, which caused the commit to fail. Show a validation error.
            errorMessage = f"User {username} is already registered." 
            cur.execute("rollback")
        except sqlite3.Error as err:
            errorMessage = err.message
            cur.execute("rollback")
                    
        return errorMessage 

    def validate_and_calculate_balance(self,db, user_id, amount ):
        user = db.execute("SELECT * FROM user WHERE id = ?", (user_id,)).fetchone()
        if user is None:
            return (None,"User not found")

        if user['user_balance'] <= 0:
            return (None,"Operation denied. User balance must be greater than 0.")

        updated_balance = user['user_balance'] - amount

        if updated_balance <= 0:
            return (None,"Operation denied. Insufficient balance.")   
        
        return updated_balance,None 

    def update_user_balance(self,cur,updated_balance, user_id):
        cur.execute("UPDATE user SET user_balance = ? WHERE id = ?",(updated_balance, user_id))
        
        
user_dao = UserDAO()        