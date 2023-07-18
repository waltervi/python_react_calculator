from flask import Blueprint
from flask import g
from flask import request

from .auth_controller_bp import validate_session
from ..service.operation_service import operation_service
from ..service.records_service import record_service
from .. import getErrorObject

bp = Blueprint("operations", __name__, url_prefix="/v1/operations")

@bp.route("/", methods= ["POST"])
@validate_session
def execute_operation():
    content = request.json
    operation = content["operation"]
    operand1 = content["operand1"]
    operand2 = content["operand2"]
        
    #validations
    if not operation:
        return getErrorObject("type is required"), 400
    
    if operation != "random_string":
        if not operand1 and operand1 != 0:
            return getErrorObject("operand1 is required"), 400

        if (not operand2 and operand2 != 0) and operation != "square_root":
            return getErrorObject("operand2 is required"), 400
    
    #operations
    result = None
    error = None
    
    operation = operation.lower()
    if operation == "addition":
        result, error = operation_service.add(g.user_id, operand1, operand2)
    elif operation == "substraction":
        result, error = operation_service.substract(g.user_id, operand1, operand2)
    elif operation == "multiplication":
        result, error = operation_service.multiply(g.user_id, operand1, operand2)
    elif operation == "division":
        result, error = operation_service.divide(g.user_id, operand1, operand2)
    elif operation == "square_root":
        result, error = operation_service.square_root(g.user_id, operand1)
    elif operation == "random_string":
        result, error = operation_service.random_string(g.user_id)        
    else:
        return getErrorObject("Invalid Operation Type") , 400
    
    if error is not None:
        return error, 400    
    
    return result, 200

@bp.route("/findall", methods= ["GET"])
@validate_session
def find_all_records_by_user_id ():
    last_id = request.args.get("last_id")
    last_id = None if not last_id else last_id
    
    page_size = request.args.get("page_size")
    page_size = None if not page_size else page_size
    
    result, error = record_service.find_all_by_user_id(g.user_id, last_id, page_size)

    if error is not None:
        return error, 500

    return result, 200

@bp.route("/<int:operationId>", methods= ["DELETE"])
@validate_session
def deleteById(operationId):
    #validations
    if not operationId:
        return getErrorObject("operationId is required"), 400

    error = record_service.delete_operation(g.user_id, operationId)

    if error is not None:
        return getErrorObject("Invalid Operation Type") , 400
    
    return "",200