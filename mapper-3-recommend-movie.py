#!/usr/bin/env python

import sys
import csv

# Read originalId from command-line arguments (default to 11 if not provided)
try:
    originalId = int(sys.argv[1]) if len(sys.argv) > 1 else 11
except ValueError:
    print("Invalid originalId, using default (11).", file=sys.stderr)
    originalId = 11

reader = csv.reader(sys.stdin)
writer = csv.writer(sys.stdout, quoting=csv.QUOTE_NONNUMERIC)

# Skip header
next(reader, None)

for row in reader:
    try:
        movieId = int(row[0])

        # Tagging the row
        row.insert(0, 'a' if movieId == originalId else 'b')
        writer.writerow(row)
    
    except (ValueError, IndexError):
        continue  # Skip malformed rows
