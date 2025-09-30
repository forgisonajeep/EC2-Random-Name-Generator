Python 01 Project

# EC2 Random Name Generator

This project is a simple Python script that generates unique names for EC2 instances in a shared AWS environment.

## Features
- User enters how many EC2 instance names to generate  
- User enters their department name  
- Random suffix of letters and numbers ensures names are unique  
- Only **Marketing, Accounting, and FinOps** departments are allowed (case-insensitive)

## Example
```bash
python3 ec2_name_generator.py
How many EC2 names do you need? 3
Enter your department: Marketing
marketing-ec2-a1b2c3
marketing-ec2-x9k8z7
marketing-ec2-0p9qrs
```

## How to Run
```bash
python3 ec2_name_generator.py
```