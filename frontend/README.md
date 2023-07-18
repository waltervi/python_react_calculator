# Coding Challenge FrontEnd

## Pending tasks
* Logic bug: When the user logs out, then the new logging does not show the calculator by default

## Tools decision

### Plain Reactjs
I decided to go plain reactjs to show how I manage the configuration files. NextJs was an option, but I thought not using it was better for this coding challenge.
Besides this decision, using NextJS or any other React framework was not specified.

### No Redux
Since this is a demo, I decided not to use Redux or the RTK. Just plain state usage.

### No testcases on the front
Due to time involved in writing tests.

## Calculator design and features

The design of the calculator has been taken from : https://codesandbox.io/s/react-bootstrap-calculator-92czh?file=/src/index.js
I added all the logic on top of this design and some UI changes for the square root and random buttons.

At first sight I tried to add more than the basic features specified in the documentation, but this generated a lot of bugs. So I rolled back and decided to go for something more SIMPLE without bugs.

Internally the calculator:

* Holds values for the 2 operands (numbers) plus an operation(addition, substraction, etc).
* In order to use an operation(addition, substraction, etc), the end user must enter a valid first operand.
* After selecting an operation, the user must enter a valid second operand.
* After that, the only operation allowed is EQUALS (to get the result). 
** After pushing equals, the result is displayed, and all the values for operands and operation are resetted internally in the calculator
** The result will continue to be displayed, until the user inserts another number, to continue with the use of the calculator.

For the datatable , I decided to go with -> https://react-data-table-component.netlify.app/


## How to run the project

Inside this directory (frontend)

    $ npm install
    $ npm start
    

This will open a default browser on port 3000 
The project needs the backed side working on port 5000






