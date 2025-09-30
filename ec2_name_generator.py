import random
import string

allowed_departments = {"marketing", "accounting", "finops"}
pool = string.ascii_lowercase + string.digits

# Ask how many names (instances) the user wants
instances = int(input("How many EC2 names do you need? "))

# Ask what department the user belongs to
department = input("Enter your department: ").strip().lower()

# Check if department is allowed
if department not in allowed_departments:
    print("This generator is only for Marketing, Accounting, or FinOps.")
else:
    names = []
    while len(names) < instances:
        # Generate a random 6-character suffix
        suffix = "".join(random.choice(pool) for _ in range(6))
        
        # Build the EC2 name
        name = f"{department}-ec2-{suffix}"
        
        # Ensure name is unique before adding
        if name not in names:
            names.append(name)
    
    # Print all generated names
    for name in names:
        print(name)