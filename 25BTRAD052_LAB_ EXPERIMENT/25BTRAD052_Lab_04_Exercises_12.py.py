import json

file = "student.json"

def read():
    try:
        with open(file) as f:
            return json.load(f)
    except:
        return []

data = read()

roll = input("Enter roll number: ")
name = input("Enter name: ")
marks = input("Enter marks: ")

data.append({"Roll": roll, "Name": name, "Marks": marks})

with open(file, "w") as f:
    json.dump(data, f)

print("\nStudent Records:")
for s in data:
    print(s)

search = input("\nSearch roll number: ")

for s in data:
    if s["Roll"] == search:
        print("Found:", s)