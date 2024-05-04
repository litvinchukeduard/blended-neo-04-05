import re
"""
The event occurred on 2024-05-04 12:30:45. It was an important moment. 
The second event occured at 2024-05-04 13:30:01
"""

# (year, month, day, hour, minute, second)
# (2024, 05, 04, 12, 30, 45)
# (2024, 05, 04, 13, 30, 01)
def parse_text(text: str) -> list[tuple]:
    pattern = r'(\d{4})\-(\d{2})\-(\d{2}) (\d{2})\:(\d{2}):(\d{2})'
    # match = re.search(pattern, text)
    # print(match.group())
    for time_info in re.findall(pattern, text):
        yield time_info

date_generator = parse_text("The event occurred on 2024-05-04 12:30:45. It was an important moment. The second event occured at 2024-05-04 13:30:01")
for date in date_generator:
    print(date)
