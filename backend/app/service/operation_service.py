from .. import getErrorObject
import math 

from ..dao.operation_dao import operation_dao
from ..dao.record_dao import record_dao
import urllib.request

class OperationService:
    ##########################################################################
    def add(self,user_id,operand1, operand2):
        if user_id is None or operand1 is None or operand2  is None :
            return (None, getErrorObject("Invalid parameters"))
            
        operation, errorMessage = operation_dao.find_by_type("ADDITION")
        if errorMessage is not None:
            return (None, getErrorObject(errorMessage))
            
        if operation is None:
            return (None, getErrorObject("Operation not found"))
        
        result = operand1 + operand2        
        updated_balance, errorMessage = record_dao.insert(operation["id"], user_id, operation["cost"], result)
        if errorMessage is not None:
            return (None, getErrorObject(errorMessage))
        
        returned_value = { "result" : result, "updated_balance" : updated_balance}
        
        return (returned_value,None)

    ##########################################################################
    def substract(self,user_id,operand1, operand2):
        if user_id is None or operand1 is None or operand2  is None :
            return (None, getErrorObject("Invalid parameters"))
            
        operation, errorMessage = operation_dao.find_by_type("SUBSTRACTION")
        if errorMessage is not None:
            return (None, getErrorObject(errorMessage))
            
        result = operand1 - operand2    
        updated_balance, errorMessage = record_dao.insert(operation["id"], user_id, operation["cost"], result)
        if errorMessage is not None:
            return (None, getErrorObject(errorMessage))
            
        returned_value = { "result" : result, "updated_balance" : updated_balance}
        
        return (returned_value,None)


    ##########################################################################
    def multiply(self,user_id,operand1, operand2):
        if user_id is None or operand1 is None or operand2  is None :
            return (None, getErrorObject("Invalid parameters"))
            
        operation, errorMessage = operation_dao.find_by_type("MULTIPLICATION")
        if errorMessage is not None:
            return (None, getErrorObject(errorMessage))
        
        result = operand1 * operand2    
        updated_balance, errorMessage = record_dao.insert(operation["id"], user_id, operation["cost"], result)
        if errorMessage is not None:
            return (None, getErrorObject(errorMessage))    
        
        returned_value = { "result" : result, "updated_balance" : updated_balance}
        return (returned_value,None)

    ##########################    ##########################################################################
    def add(self,user_id,operand1, operand2):
        if user_id is None or operand1 is None or operand2  is None :
            return (None, getErrorObject("Invalid parameters"))
            
        operation, errorMessage = operation_dao.find_by_type("ADDITION")
        if errorMessage is not None:
            return (None, getErrorObject(errorMessage))
            
        if operation is None:
            return (None, getErrorObject("Operation not found"))
        
        result = operand1 + operand2        
        updated_balance, errorMessage = record_dao.insert(operation["id"], user_id, operation["cost"], result)
        if errorMessage is not None:
            return (None, getErrorObject(errorMessage))
        
        returned_value = { "result" : result, "updated_balance" : updated_balance}
        
        return (returned_value,None)################################################
    def divide(self,user_id,operand1, operand2):
        if user_id is None or operand1 is None or operand2  is None :
            return (None, getErrorObject("Invalid parameters"))
            
        if operand2 == 0 :
            return (None, getErrorObject("Division by zero"))
                
        operation, errorMessage = operation_dao.find_by_type("DIVISION")
        if errorMessage is not None:
            return (None, getErrorObject(errorMessage))

        result = operand1 / operand2         
        updated_balance, errorMessage = record_dao.insert(operation["id"], user_id, operation["cost"], result)
        if errorMessage is not None:
            return (None, getErrorObject(errorMessage))  
        
        returned_value = { "result" : result, "updated_balance" : updated_balance}
        return (returned_value,None)


    ##########################################################################
    def square_root(self,user_id,operand1):
        if user_id is None or operand1 is None:
            return (None, getErrorObject("Invalid parameters"))
                
        operation, errorMessage = operation_dao.find_by_type("SQUARE_ROOT")
        if errorMessage is not None:
            return (None, getErrorObject(errorMessage))
            
        result = math.sqrt(operand1)     
        updated_balance, errorMessage = record_dao.insert(operation["id"], user_id, operation["cost"], result)
        if errorMessage is not None:
            return (None, getErrorObject(errorMessage))  
        
        returned_value = { "result" : result, "updated_balance" : updated_balance} 
        return (returned_value,None)

    ##########################################################################
    def random_string(self,user_id):
        if user_id is None:
            return (None, getErrorObject("Invalid user_id"))
                
        operation, errorMessage = operation_dao.find_by_type("RANDOM_STRING")
        if errorMessage is not None:
            return (None, getErrorObject(errorMessage))
        
        url = "https://www.random.org/strings/?num=1&len=8&digits=on&upperalpha=on&loweralpha=on&unique=on&format=plain&rnd=new"
        response = urllib.request.urlopen(url).read()
        
        result = response.decode('utf-8')
            
        updated_balance, errorMessage = record_dao.insert(operation["id"], user_id, operation["cost"], result)
        if errorMessage is not None:
            return (None, getErrorObject(errorMessage))  
        
        returned_value = { "result" : result, "updated_balance" : updated_balance} 
        return (returned_value,None)
    

    
operation_service = OperationService()