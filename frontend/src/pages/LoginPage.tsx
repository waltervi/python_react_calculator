import React from "react";
import "bootstrap/dist/css/bootstrap.min.css";
import Form from "react-bootstrap/Form";
import Button from "react-bootstrap/Button";
import Alert from "react-bootstrap/Alert";
import Row from "react-bootstrap/Row";
import Col from "react-bootstrap/Col";
import { UserAPI } from "../network/api";

interface LoginPageProps {
  setUserLoggedIn: any;
  setInitialView: any;
}

function LoginPage(props: LoginPageProps) {
  const [username, setUsername] = React.useState<string>("");
  const [password, setPassword] = React.useState<string>("");
  const [errorMessage, setErrorMessage] = React.useState<string>("");

  function loginUser() {
    UserAPI.loginUser(
      username,
      password,
      /*success*/ (data: any) => {
        props.setUserLoggedIn(data);
        props.setInitialView("login");
      },
      /*error*/ (axiosError: any) => {
        setErrorMessage(axiosError.response.data.errorMessage);
      }
    );
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
    <Row>
      <Col xl={4}></Col>
      <Col xl={4}>
        <Form>
          <h3>Login Page</h3>
          <Form.Group className="mb-3" controlId="formBasicEmail">
            <Form.Label>Email address</Form.Label>
            <Form.Control type="email" placeholder="Enter email" value={username} onChange={(e) => setUsername(e.target.value)} />
            <Form.Text className="text-muted">We'll never share your email with anyone else.</Form.Text>
          </Form.Group>

          <Form.Group className="mb-3" controlId="formBasicPassword">
            <Form.Label>Password </Form.Label>
            <Form.Control size="lg" type="password" placeholder="Password" value={password} onChange={(e) => setPassword(e.target.value)} />
          </Form.Group>

          <Form.Group className="mb-3" controlId="formBasicPassword">
            <Button variant="primary" type="button" onClick={loginUser}>
              Submit
            </Button>
          </Form.Group>

          {errorAlert}

          <Form.Group className="mb-3" controlId="formBasicPassword">
            <Button variant="primary" type="button" onClick={() => props.setInitialView("register")}>
              Register new user
            </Button>
          </Form.Group>
        </Form>
      </Col>
      <Col xl={4}></Col>
    </Row>
  );
}

export default LoginPage;
