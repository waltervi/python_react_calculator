import axios from "axios";

type APICallback =(data : any) => void;
 

export const OperationAPI = {
  listAll : (successCallBack : APICallback, errorCallback? : APICallback) => {
    const url = "/v1/operations/findall";
    axios
      .get(url)
      .then(function (response) {
        // handle success
        if ( successCallBack ) {
          successCallBack(response.data);
        }
      })
      .catch(function (error) {
        if ( errorCallback ) {
          errorCallback(error);
        }
      });
  },
  executeOperation : (operation:string,operand1 : number|null, operand2 : number|null,successCallBack : APICallback, errorCallback? : APICallback) => {
    const url = "/v1/operations/";
  
    const body = {
      operation: operation,
      operand1: operand1, 
      operand2: operand2
    };

    axios
      .post(url,body)
      .then(function (response) {
        // handle success
        if ( successCallBack ) {
          successCallBack(response.data);
        }
      })
      .catch(function (error) {
        if ( errorCallback ) {
          errorCallback(error);
        }
      });
  },
  deleteOperation : (operationId:number, successCallBack : APICallback, errorCallback? : APICallback) => {
    const url = "/v1/operations/" + operationId;
  
    axios
      .delete(url)
      .then(function (response) {
        // handle success
        if ( successCallBack ) {
          successCallBack(response.data);
        }
      })
      .catch(function (error) {
        if ( errorCallback ) {
          errorCallback(error);
        }
      });
  }  
};

export const UserAPI = {
  loginUser : (username : string, password:string,successCallBack : APICallback, errorCallback? : APICallback) => {
    const url = "/v1/auth/login";
    const body = {
      username: username,
      password: password
    };
  
    axios
      .post(url,body)
      .then(function (response) {
        // handle success
        if ( successCallBack ) {
          successCallBack(response.data);
        }
      })
      .catch(function (error) {
        if ( errorCallback ) {
          errorCallback(error);
        }
      });
  },
  registerUser : (username : string, password:string,successCallBack : APICallback, errorCallback? : APICallback) => {
    const url = "/v1/auth/register";
    const body = {
      username: username,
      password: password
    };
  
    axios
      .post(url,body)
      .then(function (response) {
        // handle success
        if ( successCallBack ) {
          successCallBack(response.data);
        }
      })
      .catch(function (error) {
        if ( errorCallback ) {
          errorCallback(error);
        }
      });
  }
  
};