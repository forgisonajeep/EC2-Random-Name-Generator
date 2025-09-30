import random
import string

# ask user how many names to generate
number_of_instances = int(input("How many EC2 names do you need? "))
department = input("Enter your department: ").strip().lower()

# generate names
for i in range(number_of_instances):
    rand_num = random.randint(1000, 9999)  # 4-digit number
    rand_letter = ''.join(random.choices(string.ascii_lowercase, k=4))  # 4 random letters
    instance_name = f"redLUIT-{department}-ec2-{rand_num}{rand_letter}"
    print(instance_name)