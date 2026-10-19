# import sys
# from collections import Counter

# if len(sys.argv) < 2:
#     print(f"Usage: {sys.argv[0]} <filename>", file=sys.stderr)
#     sys.exit(2)

# filename = sys.argv[1]
# print(len(filename))

# with open(filename) as f:
#     lines = f.readlines()
# print("Total lines:", len(lines))

# counts = Counter()
# for line in lines:
#     fields = line.split()
#     if len(fields) > 0:
#         key = fields[0]
#         counts[key] += 1
# print("Top 5:")
# for item, n in counts.most_common(5):
#     print(item, n)
import re
import sys
from collections import Counter
filename = sys.argv[1]
with open(filename) as f:
    lines = f.readlines()
print("Total lines:", len(lines))

counts = Counter()
for line in lines:
#     fields = line.split()
#     if len(fields) > 7:
#         key = fields[7]
#         counts[key] += 1
# print("Top 5:")
    match = re.search(r'\[(\d+)\]', line)
    if match:
        pid = match.group(1)
        counts[pid] += 1

print("Top 5 PIDs:")
for item, n in counts.most_common(5):
    print(item, n)


