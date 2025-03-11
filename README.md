# Calculator Application

## Objective
To create a calculator application that performs basic arithmetic operations (addition, subtraction, multiplication, division) following the Model-View-Controller (MVC) design pattern.

## Features
- User-friendly GUI designed with PyQt.
- Basic arithmetic operations: addition, subtraction, multiplication, division.
- Reset functionality to clear input.
- Error handling for invalid expressions and division by zero.

## Technologies Used
- Python
- PyQt6 (for GUI design)

## Installation
### Prerequisites
Ensure you have Python installed on your system. You can download it from [Python's official website](https://www.python.org/downloads/).

### Install Dependencies
Run the following command to install the required libraries:
```sh
pip install pyqt6
```
## MVC Architecture
### Model (Calculator Logic)
The `Calculator` class handles the mathematical logic and includes:
- `add_to_expression(char)`: Adds characters to the expression.
- `remove_last_character()`: Removes the last character from the expression.
- `clear_expression()`: Clears the expression.
- `calculate()`: Evaluates the expression and returns the result.
- `get_expression()`: Returns the current expression.

### View (GUI Design)
The GUI is built using PyQt6 and includes:
- `QLineEdit` for displaying input and results.
- QPushButtons for digits (0-9) and arithmetic operators (+, -, *, /, =, C).

### Controller (CalculatorWindow)
The `CalculatorWindow` class connects the GUI to the model:
- Captures user input from buttons.
- Updates the expression in the `Calculator` model.
- Displays the result or error messages.

## Sample Input/Output
### Example 1:
#### Input:
```
5 + 3 * 2 =
```
#### Output:
```
11
```
### Example 2:
#### Input:
```
10 / 0 =
```
#### Output:
```
Error: Division by zero
```

## Screenshots
![](https://raw.githubusercontent.com/crymimorta/OOP_assignment_7/refs/heads/main/%D0%A1%D0%BD%D0%B8%D0%BC%D0%BE%D0%BA%20%D1%8D%D0%BA%D1%80%D0%B0%D0%BD%D0%B0%202025-03-11%20161437.png)


