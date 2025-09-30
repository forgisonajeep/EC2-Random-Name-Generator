Python 01 Project

# EC2 Random Name Generator

This project is a simple Python script that generates unique names for EC2 instances in a shared AWS environment.

## Features
- User enters how many EC2 instance names to generate  
- User enters their department name  
- Random suffix of letters and numbers ensures names are unique  
- Advanced version restricts departments to **Marketing, Accounting, and FinOps** (case-insensitive)  

## Scripts
- **ec2_name_generator_foundational.py** → Any department is accepted.  
- **ec2_name_generator_advanced.py** → Only Marketing, Accounting, and FinOps are allowed.  

---

## Example: Foundational
```bash
$ python3 ec2_name_generator_foundational.py
How many EC2 names do you need? 2
Enter your department: hr
redLUIT-hr-ec2-4938kqjn
redLUIT-hr-ec2-8201mzpt
```

---

## Example: Advanced
```bash
$ python3 ec2_name_generator_advanced.py
How many EC2 names do you need? 2
Enter your department: FinOps
redLUIT-finops-ec2-2849qjdz
redLUIT-finops-ec2-3951nktp
```

Invalid department:
```bash
$ python3 ec2_name_generator_advanced.py
How many EC2 names do you need? 2
Enter your department: HR
This generator is only for Marketing, Accounting, or FinOps.
```

---

## How to Run
Clone the repo, move into the folder, and run either script:

```bash
git clone https://github.com/forgisonajeep/EC2-Random-Name-Generator.git
cd EC2-Random-Name-Generator
python3 ec2_name_generator_foundational.py
```

or  

```bash
python3 ec2_name_generator_advanced.py
```