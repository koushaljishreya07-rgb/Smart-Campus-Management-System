# Project Statement

## Project Title

**Smart Campus Resource Optimization System**

## Student Information

-   **Student Name:** Shreya Koushal
-   **Registration Number:** 26MIM10148
-   **Project Type:** VITyarthi -- Build Your Own Project
-   **Programming Language:** Python

## 1. Problem Statement

Campus resources such as electricity, water, classrooms, and
laboratories can experience changing levels of usage. Without a
structured method for recording and analyzing resource information, it
can be difficult to identify unusual consumption, utilization levels,
and possible inefficiency.

The **Smart Campus Resource Optimization System** addresses this problem
through a modular Python-based application that allows users to enter
resource information, calculate usage changes, analyze utilization,
detect possible inefficiency, and receive basic optimization
recommendations.

## 2. Scope of the Project

The project focuses on providing a simple console-based system for basic
campus resource analysis.

The current scope includes:

-   Resource registration.
-   Resource usage calculation.
-   Resource utilization analysis.
-   Inefficiency and wastage detection.
-   Optimization recommendations.
-   Resource analysis report generation.
-   Resource data validation and system control.

The system is implemented as a main program connected to seven separate
Python modules.

## 3. Target Users

The project is intended for users who need a simple way to record and
analyze campus resource information, such as:

-   Campus administrators.
-   Resource management staff.
-   Facility management personnel.
-   Educational institutions interested in basic resource monitoring.

The current implementation is a prototype and is designed primarily to
demonstrate the application of Python programming concepts to a
real-world campus-management problem.

## 4. High-Level Features

### Resource Registration

Allows the user to enter:

-   Resource ID
-   Resource name
-   Resource type
-   Location
-   Capacity

### Resource Usage Calculation

Calculates:

-   Previous usage
-   Current usage
-   Usage difference
-   Percentage change

### Resource Utilization Analysis

Compares actual resource usage with total capacity and classifies
utilization as:

-   Underutilized
-   Efficiently Utilized
-   Highly Utilized

### Inefficiency and Wastage Detection

Analyzes changes in resource usage and provides status messages for:

-   High inefficiency
-   Moderate increase
-   Normal usage
-   Reduced usage

### Optimization and Recommendation

Provides recommendations according to resource type and usage level,
including recommendations for electricity, water, classrooms,
laboratories, and other resources.

### Report Generation

Generates a basic resource analysis report containing resource details,
status, and recommendation.

### Validation and System Control

Validates important input information, including capacity and required
resource fields, and handles invalid numeric input.

## 5. Project Workflow

The overall workflow is:

``` text
Start
  ↓
Main Menu
  ↓
Select Module
  ↓
Enter Resource Data
  ↓
Process / Analyze Data
  ↓
Display Result
  ↓
Continue?
  ├── Yes → Main Menu
  └── No  → Exit
```

## 6. Project Structure

The project consists of:

-   `MODULE MAIN.py` -- Main menu and module controller.
-   `MODULE1.py` -- Resource Registration.
-   `MODULE2.py` -- Resource Usage Calculation.
-   `MODULE3.py` -- Resource Utilization Analysis.
-   `MODULE4.py` -- Inefficiency and Wastage Detection.
-   `MODULE5.py` -- Optimization and Recommendation.
-   `MODULE6.py` -- Report Generation.
-   `MODULE7.py` -- Validation and System Control.

## 7. Project Goal

The main goal of the project is to demonstrate how fundamental Python
programming concepts can be combined into a modular application that
addresses a practical campus resource-management problem.

The project emphasizes structured input, calculations, conditional
decision-making, validation, modular programming, and user-friendly
console interaction.
