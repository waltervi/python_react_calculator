import React from "react";

import "bootstrap/dist/css/bootstrap.min.css";
import LoginPage from "./pages/LoginPage";
import MainPage from "./pages/MainPage";
import RegisterPage from "./pages/RegisterPage";
import Container from "react-bootstrap/Container";
import Row from "react-bootstrap/Row";
import Col from "react-bootstrap/Col";


function App() {
  const [userLoggedIn, setUserLoggedIn] = React.useState<any>(null);
  const [initialView, setInitialView] = React.useState<string>("login");

  let currentView = null;

  if (userLoggedIn !== null) {
    currentView = <MainPage setUserLoggedIn={setUserLoggedIn} userLoggedIn={userLoggedIn} />;
  } else if (initialView === "login") {
    currentView = <LoginPage setUserLoggedIn={setUserLoggedIn} setInitialView={setInitialView} />;
  } else {
    currentView = <RegisterPage setUserLoggedIn={setUserLoggedIn} setInitialView={setInitialView} />;
  }

  return (
    <Container fluid>
      {currentView}
    </Container>
  );
}

export default App;
