import datetime

filename = "logs.txt"  # Replace with the actual filename and path

def Solution(end_time, severity, duration):
    ending_timestamp = end_time  # Replace with the desired ending timestamp
    length = len(severity)
    count = 0
    # Convert ending_timestamp to a datetime object
    ending_time = datetime.datetime.strptime(ending_timestamp, "%a, %d %b %Y %H:%M:%S %Z")
    print(f'EndTime: {ending_time}')
    starting_time = ending_time - datetime.timedelta(seconds=duration)


    with open(filename, "r") as file:
        logs = [line.strip() for line in file if line.strip()]

    for line in logs:
        line = line.strip()
        print(f'Line: {line}')
        if line:
            try:
                split_string = line.split("-")
                timestamp = split_string[0]
                # print(f'timestamp: {timestamp}')
                log_time = datetime.datetime.strptime(timestamp, "%a, %d %b %Y %H:%M:%S %Z")
                # print(f'Log Time: {log_time}')
                # duration = ending_time - log_time
                # if duration <= datetime.timedelta(seconds=10) and duration >= datetime.timedelta(seconds=0):
                #     logs.append(line)
                print(f'Start TIme: {starting_time}')
                print(f'Check TIme: {log_time}')
                print(f'Endin TIme: {ending_time}')
                if starting_time <= log_time <= ending_time:
                    print(f'Found Time and Error: {split_string[1][:length]}')
                    if split_string[1][:length] == severity:

                        count += 1
                    
            except ValueError:
                # Log format mismatch, or unexpected data after timestamp
                # Handle the error or ignore the log
                pass

    print(f'Count: {count}')


Solution("Mon, 26 Aug 2019 18:41:33 GMT", "INFO", 5)