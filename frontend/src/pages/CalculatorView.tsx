import React from "react";
import "./calculatorStyles.css";
import Button from "react-bootstrap/Button";
import Form from "react-bootstrap/Form";
import Alert from "react-bootstrap/Alert";
import { OperationAPI } from "../network/api";

const EMPTY_VALUE = "";

interface CalculatorViewProps {
  userLoggedIn : any;
}

function CalculatorView(props: CalculatorViewProps) {
  const [balance, setBalance] = React.useState<string>(props.userLoggedIn.user_balance);
  const [firstOperand, setFirstOperand] = React.useState<string>(EMPTY_VALUE);
  const [secondOperand, setSecondOperand] = React.useState<string>(EMPTY_VALUE);

  const [currentText, setCurrentText] = React.useState<string>(EMPTY_VALUE);
  const [currentOperation, setCurrentOperation] = React.useState<string>(EMPTY_VALUE);
  const [errorMessage, setErrorMessage] = React.useState<string>("");

  function getOperandValue(): any[] {
    const useFirstOperand = currentOperation === EMPTY_VALUE;

    let operandValue = useFirstOperand ? firstOperand : secondOperand;

    operandValue = operandValue === EMPTY_VALUE ? "0" : operandValue;

    return [useFirstOperand, operandValue];
  }

  function containsDot(operandValue: string): boolean {
    return operandValue.indexOf(".") > 0;
  }

  function addNumber(n: number) {
    let [useFirstOperand, operandValue] = getOperandValue();

    //avoid adding multiple zeros on the left
    const alreadyHasDot = containsDot(operandValue);
    const operandFloatValue = parseFloat(operandValue);

    if (alreadyHasDot === false && operandFloatValue === 0 && n === 0) {
      operandValue = "0";
    } else {
      operandValue = operandValue + n.toString();
      operandValue = parseFloat(operandValue).toString(); //Adding proper format to the number
    }

    const value = operandValue.toString();

    if (useFirstOperand) {
      //this is the first number
      setFirstOperand(value);
      setCurrentText(value);
    } else {
      //this is the second number
      setSecondOperand(value);
      setCurrentText(currentText + n.toString());
    }
  }

  function addDot() {
    const [useFirstOperand, operandValue] = getOperandValue();

    const alreadyHasDot = containsDot(operandValue);

    if (!alreadyHasDot) {
      const value = operandValue + ".";
      setCurrentText(currentText + ".");

      if (useFirstOperand) {
        //this is the first number
        setFirstOperand(value);
      } else {
        //this is the second number
        setSecondOperand(value);
      }
    }
  }

  function cleanValues(currentText: string) {
    setFirstOperand(EMPTY_VALUE);
    setSecondOperand(EMPTY_VALUE);
    setCurrentOperation(EMPTY_VALUE);
    setCurrentText(currentText);
    setErrorMessage(EMPTY_VALUE);
  }

  function addOperation(op: string) {

    if (op === "R") {
      executeRemoteOperation(null,null, op);
      return;
    }

    //skip this 2 possible states
    if (firstOperand === EMPTY_VALUE || currentOperation !== EMPTY_VALUE) {
      return;
    }

    if (op === "√") {
      executeRemoteOperation(parseFloat(firstOperand),null, op);
    } else {
      setCurrentText(firstOperand + op);
      setCurrentOperation(op);
    }
  }

  /**
   * I decided to write this funtion in order to skip the use of "eval" function.
   */
  function executeRemoteOperation(firstOperandValue: number | null, secondOperandValue: number | null, operator: string): void {
    let operation : string = "";
    switch (operator) {
      case "+":
        operation = "addition";
        break;
      case "-":
        operation = "substraction";
        break;
      case "*":
        operation = "multiplication";
        break;
      case "/":
        operation = "division";
        break;
      case "R":
        operation = "random_string";
        break;
      case "√":
        operation = "square_root";
        break;
    }

    OperationAPI.executeOperation(operation,firstOperandValue,secondOperandValue,
      /*success*/ (data: any) => {
        console.log(data);
        cleanValues(data.result);
        console.log(data.updated_balance);
        setBalance(data.updated_balance)
      },
      /*error*/ (axiosError : any) => setErrorMessage(axiosError.response.data.errorMessage)
      );
  }

  function executeEquals() {
    if (firstOperand === EMPTY_VALUE || currentOperation === EMPTY_VALUE || secondOperand === EMPTY_VALUE) {
      return;
    }

    const validatedFirstOperandValue = parseFloat(firstOperand);
    const validatedSecondOperandValue = parseFloat(secondOperand);

    executeRemoteOperation(validatedFirstOperandValue, validatedSecondOperandValue, currentOperation);
  }

  let errorAlert: any = null;
  if (errorMessage !== "") {
    errorAlert = (
      <Form.Group className="mb-3" controlId="formBasicPassword">
        <Alert key="danger" variant="danger">
          {errorMessage}
        </Alert>
      </Form.Group>
    );
  }

  return (
    <div className="calculator">
      {errorAlert}
      <Form.Group className="mb-3" controlId="exampleForm.ControlInput1">
        <Form.Label className="btn2" style={{ textAlign: "right" }}>
          Current balance : {balance}
        </Form.Label>
      </Form.Group>
      <Form.Group className="mb-3">
        <Form.Control className="btn2" placeholder={currentText} style={{ textAlign: "right" }} disabled />
      </Form.Group>
      <div className="buttons">
        {/* NUMBERS */}
        <Button key="zero" className="btn2 btn-primary letter-zero" onClick={() => addNumber(0)}>
          0
        </Button>
        <Button key="one" className="btn2 btn-primary letter-one" onClick={() => addNumber(1)}>
          1
        </Button>
        <Button key="two" className="btn2 btn-primary letter-two" onClick={() => addNumber(2)}>
          2
        </Button>
        <Button key="three" className="btn2 btn-primary letter-three" onClick={() => addNumber(3)}>
          3
        </Button>
        <Button key="four" className="btn2 btn-primary letter-four" onClick={() => addNumber(4)}>
          4
        </Button>
        <Button key="five" className="btn2 btn-primary letter-five" onClick={() => addNumber(5)}>
          5
        </Button>
        <Button key="six" className="btn2 btn-primary letter-six" onClick={() => addNumber(6)}>
          6
        </Button>
        <Button key="seven" className="btn2 btn-primary letter-seven" onClick={() => addNumber(7)}>
          7
        </Button>
        <Button key="eigth" className="btn2 btn-primary letter-eigth" onClick={() => addNumber(8)}>
          8
        </Button>
        <Button key="nine" className="btn2 btn-primary letter-nine" onClick={() => addNumber(9)}>
          9
        </Button>
        <Button key="dot" className="btn2 btn-primary letter-dot" onClick={() => addDot()}>
          .
        </Button>

        {/* OPERATIONS */}
        <Button key="substract" className="btn2 btn-secondary letter-subtract" onClick={() => addOperation("-")}>
          -
        </Button>
        <Button key="add" className="btn2 btn-secondary letter-add" onClick={() => addOperation("+")}>
          +
        </Button>
        <Button key="multiply" className="btn2 btn-secondary letter-multiply" onClick={() => addOperation("*")}>
          x
        </Button>
        <Button key="divide" className="btn2 btn-secondary letter-divide" onClick={() => addOperation("/")}>
          /
        </Button>
        <Button key="square_root" className="btn2 btn-secondary letter-square_root" onClick={() => addOperation("√")}>
          √
        </Button>
        <Button key="random" className="btn2 btn-secondary letter-random" onClick={() => addOperation("R")}>
          R
        </Button>

        <Button key="equals" className="btn2 btn-success letter-equals" onClick={() => executeEquals()}>
          =
        </Button>
        <Button key="clear" className="btn2 btn-danger letter-clear" onClick={() => cleanValues(EMPTY_VALUE)}>
          C
        </Button>
      </div>
    </div>
  );
}

export default CalculatorView;
