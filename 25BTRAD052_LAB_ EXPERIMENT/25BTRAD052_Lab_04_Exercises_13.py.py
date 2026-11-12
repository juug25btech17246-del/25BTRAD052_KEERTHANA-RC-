import csv

with open("employee.csv", "w", newline="") as f:
    w = csv.writer(f)
    w.writerow(["Name", "Basic", "Allowance", "Deduction"])
    w.writerow(["Ravi", 20000, 3000, 2000])
    w.writerow(["Priya", 25000, 4000, 3000])

with open("employee.csv", "r") as f:
    r = csv.DictReader(f)

    for e in r:
        gross = int(e["Basic"]) + int(e["Allowance"])
        net = gross - int(e["Deduction"])

        print("Name:", e["Name"])
        print("Gross Salary:", gross)
        print("Net Salary:", net)