# Python GUI Projects (tkinter)

This repository contains three simple, standalone desktop applications built using Python and the standard **tkinter** library.

## Projects Included

| Project | Description | Main Functionality |
| :--- | :--- | :--- |
| **1. BMI Calculator** | A utility to calculate Body Mass Index (BMI) based on user-provided weight and height. | Calculates BMI and categorizes the result (Underweight, Normal, Overweight, Obese). |
| **2. Simple Calculator** | A basic four-function calculator supporting addition, subtraction, multiplication, and division. | Processes user input and evaluates arithmetic expressions using `eval()`. |
| **3. Portfolio Generator** | A simple tool to gather personal information and output a formatted text-based portfolio structure. | Accepts name, bio, skills, and projects, then formats them into a display box. |

---

## 1. BMI Calculator

### `bmi_calculator.py`

### Description
This application uses a graphical interface to take a user's weight (in kilograms) and height (in centimeters) to calculate their Body Mass Index (BMI). It then displays the BMI value and the corresponding health category.

### Features
* Accepts weight (kg) and height (cm).
* Handles invalid inputs (non-numeric, zero height).
* Outputs a rounded BMI score and a category (e.g., "Normal weight").

### Usage
1.  Enter your **weight** in the first field (e.g., 70).
2.  Enter your **height** in the second field (e.g., 175).
3.  Click the **"Calculate BMI"** button.

[![Screenshot-2025-10-06-151320.png](https://i.postimg.cc/CLpsh2KF/Screenshot-2025-10-06-151320.png)](https://postimg.cc/Lhv1vNf7)
---

## 2. Simple Calculator

### `simple_calculator.py`

### Description
A standard, functional calculator interface. It allows users to input simple arithmetic expressions and get the result immediately.

### Features
* Supports basic operations: `+`, `-`, `*`, `/`.
* Includes a **Clear (C)** button to reset the input.
* Displays "Error" for invalid or mathematically impossible operations (e.g., division by zero).

### Usage
1.  Click the number buttons to input your first number.
2.  Click an operator (`+`, `-`, `*`, `/`).
3.  Input the second number.
4.  Click the **`=`** button to see the result.

[![Screenshot-2025-10-06-151349.png](https://i.postimg.cc/3JwJv8Nv/Screenshot-2025-10-06-151349.png)](https://postimg.cc/8sqS8Vhp)
---

## 3. Portfolio Generator

### `portfolio_generator.py`

### Description
A form-based application designed to quickly structure the content for a personal portfolio. The user inputs key details, and the tool compiles them into a clean, formatted text output.

### Features
* Input fields for **Name**, **Bio**, **Skills**, and **Projects**.
* Skills and Projects fields support **one item per line**.
* Generates a simple, readable text structure in the output box.

### Usage
1.  Fill out the **Name** and **Bio** fields.
2.  Type your **Skills** (e.g., "Python", "Tkinter") each on a new line.
3.  Type your **Projects** (e.g., "This Calculator App") each on a new line.
4.  Click the **"Generate Portfolio"** button.

[![Screenshot-2025-10-06-151812.png](https://i.postimg.cc/KcphCnc3/Screenshot-2025-10-06-151812.png)](https://postimg.cc/V5thC0Cz)
---

## Setup and Running the Projects

### Prerequisites

You only need **Python 3.x** installed. The `tkinter` library is included by default with most Python installations, so no additional dependencies are required.

### How to Run

1.  **Save the Code:** Save each of the three code snippets into separate files (e.g., `bmi_calculator.py`, `calculator.py`, `portfolio_generator.py`).
2.  **Run from Terminal:** Navigate to the directory where you saved the files in your command line/terminal.
3.  Execute the desired script using:

    ```bash
    python <filename>.py
    # Example: python bmi_calculator.py
    ```
