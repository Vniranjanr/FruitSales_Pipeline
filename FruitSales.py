import os
import subprocess

import pandas as pd
import matplotlib.pyplot as plt

fruits = []
sales = []

for _ in range(5):
    fruit = input("Enter fruit name: ")
    sale = int(input(f"Enter sales for {fruit}: "))
    fruits.append(fruit)
    sales.append(sale)

import pandas as pd

data = {"Fruit": fruits, "Sales": sales}
df = pd.DataFrame(data)

# Save to Excel
from datetime import datetime

today = datetime.today().strftime("%Y%m%d")  # e.g., '20250801'
excel_filename = f"fruit_sales_{today}.xlsx"
df.to_excel(excel_filename, index=False)

upload = input("Do you want to upload the Excel file to GitHub? (yes/no): ").lower()

if upload == 'yes':
    # 5. Move file to local cloned repo (optional if already inside repo)
    repo_path = "C:/Users/vnira/PycharmProjects/FruitSales/FruitSales_Pipeline"  # change this to your actual repo path
    dest_path = os.path.join(repo_path, excel_filename)
    os.replace(excel_filename, dest_path)

    # 6. Git commands
    os.chdir(repo_path)  # change working directory to repo
    subprocess.run(["git", "add", excel_filename])
    subprocess.run(["git", "commit", "-m", "Add fruit sales Excel file"])
    subprocess.run(["git", "push"])

    print("✅ Excel file uploaded to GitHub via local repo.")
