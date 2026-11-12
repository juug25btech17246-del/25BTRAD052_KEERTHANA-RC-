try:
    with open("log.txt", "w") as f:
        f.write("INFO: System started\n")
        f.write("ERROR: File not found\n")
        f.write("WARNING: Low memory\n")
        f.write("INFO: User logged in\n")
        f.write("ERROR: Connection failed\n")

    count = {"ERROR": 0, "WARNING": 0, "INFO": 0}

    with open("log.txt", "r") as f:
        for line in f:
            for key in count:
                if key in line:
                    count[key] += 1

    print("Log File Summary")
    for key, value in count.items():
        print(key, ":", value)

except FileNotFoundError:
    print("File not found")

except Exception as e:
    print("Error:", e)