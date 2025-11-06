import sys
import re

logFile: str = sys.argv[1]

with open(logFile) as file:
    lines = file.readlines()

lenLines = len(lines)

if lenLines == 1 and lines[0] == "All checks passed!\n":
    print(f"::notice::✅ All checks passed !")
else:
    for i in range(lenLines - 1, 0, -1):
        match = re.match(r'Found (\d+) errors?\.', lines[i])
        if match:
            print(f"::error::{match.group()} Look at ruff-report.log for details.")
            break
    exit(code=1)

# lineNb = 0
# while lineNb < len(lines):
#     line = lines[lineNb].strip()

#     match = re.match(r'([EWFC]\d{3}) (.+)', line)
#     if match:
#         code = match.group(1)
#         message = match.group(2)

#         lineNb += 1
#         location = lines[lineNb].strip()
#         locMatch = re.match(r'-->\s+(.+):(\d+):(\d+)', location)
#         if locMatch:
#             file = locMatch.group(1)
#             fileLine = locMatch.group(2)
#             fileColumn = locMatch.group(3)

#             lineNb += 1
#             help = lines[lineNb]
#             helpLines: list[str] = []
#             while re.match(r'\|', help) or re.match(r'(.+)\|', help) or re.match(r'(.+)\|(.+)', help) or re.match(r'help:(.+)', help):
#                 helpLines.append(help)
#                 lineNb += 1
#                 help = lines[lineNb]
#             helpMessage = "\n"
#             for helpLine in helpLines:
#                 helpMessage += helpLine

#             print(f"::error file={file},line={fileLine},col={fileColumn}::{code} {message} {helpMessage}")
#     lineNb += 1
