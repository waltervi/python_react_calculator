from .. import getErrorObject
from ..dao.record_dao import record_dao

class RecordService:
    def find_all_by_user_id (self,user_id,last_id= None,page_size= None):
        if user_id is None :
            return (None, getErrorObject("Invalid user_id"))
            
        result, error = record_dao.find_all_by_user_id(user_id, last_id, page_size)

        transformed = [ dict(row) for row in result if row is not None ]

        return (transformed,getErrorObject(error))

    ##########################################################################
    def delete_operation(self,user_id,operationId):
        if user_id is None or operationId is None:
            return getErrorObject("Invalid parameters")
            
        errorMessage = record_dao.delete(user_id,operationId)
        if errorMessage is not None:
            return getErrorObject(errorMessage)
        
        return None
    
record_service = RecordService()