#!/usr/bin/env python

import sys
import csv

writer = csv.writer(sys.stdout, delimiter='\t', quoting=csv.QUOTE_NONNUMERIC)
reader = csv.reader(sys.stdin)

for row in reader:
    try:
        rating = float(row[4].strip())
        totalRatings = int(row[5].strip())
        similarity = float(row[0].strip())

        # Creating a sortable key (higher rating, higher totalRatings, higher similarity)
        key = f"{rating:06.3f}-{totalRatings:06d}-{similarity:.6f}"

        row.insert(0, key)
        writer.writerow(row)

    except (ValueError, IndexError):
        continue  # Skip invalid rows
