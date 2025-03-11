#!/usr/bin/env python

import sys
import csv

movie = None
accumulatedRatings = 0
totalRatings = 0

writer = csv.writer(sys.stdout, quoting=csv.QUOTE_NONNUMERIC)
reader = csv.reader(sys.stdin)

for row in reader:
    try:
        current = int(row[0].strip())  # Movie ID
        rating = float(row[1].strip())  # Rating

        if movie != current:
            if movie is not None and totalRatings > 0:
                writer.writerow([movie, round(accumulatedRatings / totalRatings, 4), totalRatings, 'r'])

            movie = current
            accumulatedRatings = rating
            totalRatings = 1
        else:
            accumulatedRatings += rating
            totalRatings += 1

    except (IndexError, ValueError):  # Handles missing columns or non-numeric values
        continue

if movie is not None and totalRatings > 0:
    writer.writerow([movie, round(accumulatedRatings / totalRatings, 4), totalRatings, 'r'])
