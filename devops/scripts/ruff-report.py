import sys
import re

logFile: str = sys.argv[1]

with open(logFile) as file:
    lines = file.readlines()

lenLines = len(lines)

if lenLines == 1 and lines[0] == "All checks passed!\n":
    print("::notice::✅ All checks passed !")
else:
    for i in range(lenLines - 1, 0, -1):
        match = re.match(r'Found (\d+) errors?\.', lines[i])
        if match:
            print(f"::error::{match.group()} Look at Ruff report.log for details.")
            break
    exit(code=1)
