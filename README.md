# Smart Campus Resource Optimization System

## Project Information

-   **Student Name:** Shreya Koushal
-   **Registration Number:** 26MIM10148
-   **Project Type:** VITyarthi -- Build Your Own Project
-   **Programming Language:** Python

## 1. Project Overview

The **Smart Campus Resource Optimization System** is a modular,
menu-driven Python project designed to help analyze the usage and
utilization of campus resources.

The system allows a user to register resource information, calculate
changes in resource usage, analyze utilization, detect possible
inefficiency or wastage, receive optimization recommendations, generate
a resource analysis report, and validate resource data.

The project is divided into seven functional modules and a main program
that connects all the modules through a central menu.

## 2. Problem Statement

Campus resources such as electricity, water, classrooms, and
laboratories may have changing levels of usage. Without a structured
method for recording and analyzing this information, identifying unusual
consumption and possible inefficiency can be difficult.

This project provides a simple Python-based system for entering resource
information, performing usage calculations, analyzing utilization,
identifying possible inefficiency, and providing basic optimization
recommendations.

## 3. Objectives

-   Register and organize basic campus resource information.
-   Calculate the difference between previous and current resource
    usage.
-   Calculate percentage change in resource usage.
-   Analyze resource utilization based on capacity and actual usage.
-   Detect significant increases in resource consumption.
-   Provide resource-specific optimization recommendations.
-   Generate a basic resource analysis report.
-   Validate important resource information before processing.

## 4. Features

### 1. Resource Registration

Collects: - Resource ID - Resource name - Resource type - Location -
Capacity

### 2. Resource Usage Calculation

Calculates: - Previous usage - Current usage - Usage difference -
Percentage change

### 3. Resource Utilization Analysis

Calculates utilization percentage and classifies the resource as: -
Underutilized - Efficiently Utilized - Highly Utilized

### 4. Inefficiency and Wastage Detection

Analyzes the increase in usage and identifies: - High inefficiency -
Moderate increase - Normal usage - Reduced usage

### 5. Optimization and Recommendation

Provides recommendations based on resource type, including: -
Electricity - Water - Classroom - Laboratory - Other resources

### 6. Report Generation

Generates a resource analysis report containing: - Resource
information - Resource status - Recommendation

### 7. Validation and System Control

Checks: - Capacity must be a valid number. - Capacity must be greater
than zero. - Resource ID cannot be empty. - Resource name cannot be
empty. - Resource type cannot be empty. - Location cannot be empty.

## 5. Project Structure

``` text
Smart-Campus-Resource-Optimization-System/
│
├── MODULE MAIN.py
├── MODULE1.py
├── MODULE2.py
├── MODULE3.py
├── MODULE4.py
├── MODULE5.py
├── MODULE6.py
├── MODULE7.py
├── README.md
└── Project_Report.pdf
```

### Module Description

  -----------------------------------------------------------------------
  File                    Module                  Purpose
  ----------------------- ----------------------- -----------------------
  `MODULE MAIN.py`        Main Program            Displays the menu and
                                                  connects all modules

  `MODULE1.py`            Resource Registration   Registers campus
                                                  resources

  `MODULE2.py`            Resource Usage          Calculates usage
                          Calculation             difference and
                                                  percentage change

  `MODULE3.py`            Resource Utilization    Calculates and
                          Analysis                classifies utilization

  `MODULE4.py`            Inefficiency Detection  Detects significant
                                                  usage increases

  `MODULE5.py`            Optimization &          Provides
                          Recommendation          resource-specific
                                                  recommendations

  `MODULE6.py`            Report Generation       Generates a resource
                                                  analysis report

  `MODULE7.py`            Validation & System     Validates entered
                          Control                 resource data
  -----------------------------------------------------------------------

## 6. Technologies and Tools Used

-   **Python 3**
-   Python functions
-   Lists
-   Dictionaries
-   `while` loops
-   `if`, `elif`, and `else` statements
-   Arithmetic operations
-   `try-except` error handling
-   Python modules and imports
-   Console-based input/output

No external Python libraries are required by the submitted source code.

## 7. How to Install

### Step 1: Install Python

Install Python 3 on your computer.

### Step 2: Download or Clone the Project

Place all project files in the same folder.

### Step 3: Open the Project Folder

Open the folder using a terminal, Command Prompt, VS Code, or another
Python-compatible editor.

## 8. How to Run the Project

Run the main program:

``` bash
python "MODULE MAIN.py"
```

The system will display the main menu:

``` text
SMART CAMPUS MANAGEMENT SYSTEM

1. Resorce Registration
2. Resource Usage Calculation
3. Resource Utilization Analysis
4. Inefficiency and Wastage Detection
5. Optimization and Recommendation
6. Report Generation
7. Validation and System Control
8. Exit
```

Enter the number corresponding to the module you want to use.

## 9. System Workflow

``` text
Start
  ↓
Display Main Menu
  ↓
Enter User Choice
  ↓
Select Required Module
  ↓
Enter Required Data
  ↓
Process Data
  ↓
Display Result
  ↓
Continue?
  ├── Yes → Return to Main Menu
  └── No  → Exit
```

## 10. Important Calculations

### Usage Difference

``` text
Usage Difference = Current Usage - Previous Usage
```

### Percentage Change

``` text
Percentage Change =
((Current Usage - Previous Usage) / Previous Usage) × 100
```

The program handles the case where previous usage is zero.

### Utilization Percentage

``` text
Utilization Percentage =
(Actual Usage / Total Capacity) × 100
```

## 11. Testing

The project can be tested by entering different valid and invalid
inputs.

### Suggested Test Cases

  -----------------------------------------------------------------------
  Test Case               Input/Condition         Expected Result
  ----------------------- ----------------------- -----------------------
  1                       Select option 1         Resource registration
                                                  module opens

  2                       Select option 2         Usage calculation
                                                  module opens

  3                       Previous usage and      Usage difference and
                          current usage entered   percentage change
                                                  displayed

  4                       Capacity ≤ 0            Invalid capacity
                                                  message

  5                       Usage increase \> 30%   High inefficiency alert

  6                       Usage increase \> 10%   Moderate increase
                                                  message

  7                       Non-numeric capacity    Invalid data message

  8                       Empty resource ID       Validation error

  9                       Empty resource name     Validation error

  10                      Select option 8         System exits
  -----------------------------------------------------------------------

## 12. Error Handling and Validation

The project includes basic validation to prevent invalid input from
being processed.

Examples include: - Checking whether capacity is greater than zero. -
Handling non-numeric capacity using `try-except`. - Checking for empty
resource ID, name, type, and location. - Checking previous usage before
calculating percentage-based values.

## 13. Limitations of the Current Version

-   The current project is console-based.
-   Resource information is not stored permanently in a database.
-   The modules currently receive their required inputs independently.
-   No graphical dashboard is included.
-   No authentication system is included.
-   No automated notification system is included.

## 14. Future Enhancements

Possible future improvements include:

-   Database integration for permanent resource storage.
-   Historical resource usage tracking.
-   Graphs and dashboards for visual analysis.
-   Automatic alerts for unusual resource consumption.
-   User authentication and role-based access.
-   Integration of registered resource data with all analysis modules.
-   Automated testing.
-   Improved reporting and data visualization.

## 15. Author

**Shreya Koushal**\
**Registration Number: 26MIM10148**

## 16. Project Report

A detailed project report containing the project introduction, problem
statement, requirements, architecture, design diagrams, implementation
details, testing approach, challenges, learnings, future enhancements,
and references is included separately as the project report PDF.
