# BMI Calculator

## Overview
The BMI Calculator is a Python program that calculates Body Mass Index (BMI) based on user-provided weight and height measurements. It provides both the numerical BMI value and a classification category according to standard health guidelines.

## Features
- Input validation for weight and height values
- Clear BMI classification based on WHO standards
- User-friendly prompts with error handling
- Handles both metric units (kg and meters)

## Installation
1. Ensure you have Python 3.x installed on your system
2. Download or clone the `Bmi.py` file from this repository

## Usage
Run the script using Python:
```
python Bmi.py
```

Follow the prompts:
1. Enter your weight in kilograms (must be between 10-500 kg)
2. Enter your height in meters (must be between 0.5-3 meters)

The program will then calculate and display your BMI along with the appropriate classification.

## BMI Classification
- Underweight: BMI less than 18.5
- Normal weight: BMI between 18.5 and 24.9
- Overweight: BMI between 25 and 29.9
- Obesity: BMI of 30 or greater

## Example
```
BMI Calculator
Enter weight (kg): 68
Enter height (meters): 1.75

Your BMI is: 22.20
You are classified as: Normal weight
```

## Requirements
- Python 3.x
- No external dependencies required

## Important Notes
- This calculator uses the standard BMI formula: weight (kg) / (height (m))²
- BMI is a screening tool, not a direct measure of body fat or health
- Consult with healthcare professionals for personalized health advice
- The calculator includes input validation to ensure reasonable values

## Contributing
Feel free to fork this project and submit pull requests for any improvements, such as adding imperial units support or enhanced visualizations.

## License
This project is open source and available under the MIT License.
