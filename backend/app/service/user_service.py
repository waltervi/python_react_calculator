from ..dao.user_dao import user_dao 
from werkzeug.security import check_password_hash,generate_password_hash
from .. import getErrorObject

class UserService :
    def validate_login(self,username,password):
        row , errorMessage = user_dao.find_by_username(username)
        
        if row is None:
            errorMessage = "Incorrect username."
            return None, getErrorObject(errorMessage)
        
        user = dict(row)
        if not check_password_hash(user["password"], password):
            errorMessage = "Incorrect password."    
        
        #remove password from user before serialization
        del user["password"]    
        return user, getErrorObject(errorMessage)


    #Validates that the username is not already taken. Hashes the password for security.
    def create_user(self,username, password):
        errorMessage = user_dao.insert(username, generate_password_hash(password))
        if errorMessage is not None:
            return "" , getErrorObject(errorMessage)
        
        row, errorMessage = user_dao.find_by_username(username)
        if errorMessage is not None:
            return "" , getErrorObject(errorMessage)
        
        #remove password from user before serialization
        del row["password"]
        return row, None

user_service = UserService()