def analyze_logs(logs):
    database = 0
    network = 0
    for log in logs:
        messages = log.message
        if "database" in messages.lower():
            print("Database connection issue detected.")
            database += 1
        if "network" in messages.lower():
            print("Network error detected.")
            network += 1
    print (f"Total database issues: {database}")
    print (f"Total network issues: {network}")
    return {"database": database, "network": network}