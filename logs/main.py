import re
from collections import Counter

logs = """2024-01-22 08:30:01 INFO User logged in successfully.
2024-01-22 08:45:23 DEBUG Attempting to connect to the database.
2024-01-22 09:00:45 ERROR Database connection failed.
2024-01-22 09:15:10 INFO Data export completed.
2024-01-22 10:30:55 WARNING Disk usage above 80%.
2024-01-22 11:05:00 DEBUG Starting data backup process.
2024-01-22 11:30:15 ERROR Backup process failed.
2024-01-22 12:00:00 INFO User logged out.
2024-01-22 12:45:05 DEBUG Checking system health.
2024-01-22 13:30:30 INFO Scheduled maintenance."""

pattern = r'(\d{4}\-\d{2}\-\d{2}) (\d{2}\:\d{2}:\d{2}) (\w+) ([\w .]+)'

result_list = []
for log in logs.split('\n'):
    result_list.append(re.match(pattern, log).groups())

# print(result_list)

level_list = [log[2] for log in result_list]
log_counter = Counter(level_list)
print(log_counter)
