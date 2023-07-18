import { Link } from "react-router-dom";
import { Switch, Route ,Redirect } from "react-router-dom";
import Navbar from "react-bootstrap/Navbar";
import Nav from "react-bootstrap/Nav";
import Container from "react-bootstrap/Container";
import CalculatorView from "./CalculatorView";
import UseRecords from "./UseRecords";

interface MainPageProps {
  setUserLoggedIn: (value: any) => void;
  userLoggedIn: any;
}



function MainPage(props: MainPageProps) {
  return (
    <>
      <Navbar expand="lg" className="bg-body-tertiary">
        <Container>
          <Navbar.Collapse id="basic-navbar-nav">
            <Nav className="me-auto">
              <Link to="/calculator">Calculator</Link>
            </Nav>
            <Nav className="me-auto">
              <Link to="/user_records">User records</Link>
            </Nav>
          </Navbar.Collapse>
          <Navbar.Toggle />
          <Nav className="me-auto">
            <Navbar.Text>
              Signed in as: <a href="#login">{props.userLoggedIn.username}</a>
            </Navbar.Text>
            <Nav.Link onClick={() => props.setUserLoggedIn(null)}>Logout</Nav.Link>
          </Nav>
        </Container>
      </Navbar>
      <Switch>
        <Route
          exact
          path="/"
          render={() => {
            return props.userLoggedIn ? <Redirect to="/login" /> : <Redirect to="/calculator" />;
          }}
        />
        <Route path="/calculator">
          <CalculatorView userLoggedIn={props.userLoggedIn} />
        </Route>
        <Route path="/user_records">
          <UseRecords />
        </Route>
        <Route path="/login">
          <UseRecords />
        </Route>
        <Route path="/register">
          <UseRecords />
        </Route>
      </Switch>
    </>
  );
}

export default MainPage;
