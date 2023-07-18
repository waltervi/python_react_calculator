import React from "react";
import DataTable from "react-data-table-component";
import Row from "react-bootstrap/Row";
import Col from "react-bootstrap/Col";
import Button from "react-bootstrap/Button";
import { OperationAPI } from "../network/api";
import Alert from "react-bootstrap/Alert";

export default function UseRecords() {
  const [errorMessage, setErrorMessage] = React.useState<string>("");
  const [tableData, setTableData] = React.useState<any>([]);

  const columns = [
    {
      name: "Id",
      selector: (row: any) => row.id,
      sortable: true,
    },
    {
      name: "Type",
      selector: (row: any) => row.type,
      sortable: true,
    },
    {
      name: "Amount",
      selector: (row: any) => row.amount,
      sortable: true,
    },
    {
      name: "Response",
      selector: (row: any) => row.operation_response,
      sortable: true,
    },
    {
      name: "Balance",
      selector: (row: any) => row.user_balance,
      sortable: true,
    },
    {
      name: "Date",
      selector: (row: any) => { return new Date(row.date).toISOString();},
      sortable: true,
    },
    {
      cell:(row : any) => <Button size="sm" onClick={(e) =>handleDeleteButtonClick(e)} id={row.id}>Delete</Button>,
      ignoreRowClick: true,
      allowOverflow: true,
      button: true,
    }
  ];

  const handleDeleteButtonClick = (state : any) => {
    OperationAPI.deleteOperation(state.target.id,
      /*success*/ (data: any) => {
        OperationAPI.listAll(
          /*success*/ (data: any) => setTableData(data),
          /*error*/ (axiosError: any) => setErrorMessage(axiosError.response.data.errorMessage)
        );
      },
      /*error*/ (axiosError: any) => setErrorMessage(axiosError.response.data.errorMessage)
    );    
  };

  React.useEffect(() => {
    OperationAPI.listAll(
      /*success*/ (data: any) => setTableData(data),
      /*error*/ (axiosError: any) => setErrorMessage(axiosError.response.data.errorMessage)
    );
  }, []);

  let errorAlert: any = null;
  if (errorMessage !== "") {
    errorAlert = (
      <Row>
        <Col xl={4}></Col>
        <Col xl={4}>
          <Alert key="danger" variant="danger">
            {errorMessage}
          </Alert>
        </Col>
        <Col xl={4}></Col>
      </Row>
    );
  }
  return (
    <>
      {errorAlert}
      <Row>
        <Col xl={2}></Col>
        <Col xl={8}>
          <DataTable pagination columns={columns} data={tableData} />
        </Col>
        <Col xl={2}></Col>
      </Row>
    </>
  );
}
