# Student Marksheet Application

This is a Python application built with Tkinter that allows users to enter grades and credits for multiple subjects and calculates the total credits and SGPA (Semester Grade Point Average) based on the input. The application features an organized user interface with different sections for student information, subject details, and result display.

## Features

- **Student Information Input**: Fields to enter the student's name, registration number, and roll number.
- **Subject Details**: Input fields for entering subject names, credits, and grades.
- **Results Calculation**: Computes total credits and SGPA based on the grades and credits provided.
- **Error Handling**: Validates input and displays error messages for invalid grades or credits.
- **Organized Layout**: Uses frames to separate different sections of the application for clarity.

## Installation

To run this application, ensure you have Python installed on your system. You do not need any additional libraries as Tkinter is included with the standard Python installation.

1. **Clone the Repository**:
    ```sh
    git clone 'link'
    cd student-marksheet
    ```

2. **Run the Application**:
    ```sh
    python marksheet_app.py
    ```

## Usage

1. **Enter Student Information**:
   - Fill in the student's name, registration number, and roll number.

2. **Enter Subject Details**:
   - Input the subject names, credits, and grades for each subject. Credits are predefined in the code and can be modified as needed.
   - The grades should be one of the following: A, B, C, D, P, or F.

3. **Calculate Results**:
   - Click the "Calculate" button to compute the total credits and SGPA.
   - The results will be displayed below the subject details.

## Code Overview

The application consists of the following components:

- **`info_frame`**: For entering student information.
- **`subject_frame`**: For entering subject details and displaying calculated points.
- **`result_frame`**: For displaying the total credits and SGPA.

**Functionality**:
- The `calculate_results` function processes the grades and credits, calculates the total points and credits, and updates the UI with the results.

