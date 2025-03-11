#!/usr/bin/env python

import sys
import csv

# Constants for filtering
MAX_RECOS = 14
MIN_RATING = 3.0
MIN_SIMILAR = 0.95

print("movieId,title,genre,rating,totalRatings")
writer = csv.writer(sys.stdout, quoting=csv.QUOTE_NONNUMERIC)

reader = csv.reader(sys.stdin, delimiter="\t")

for recos, row in enumerate(reader):
    if recos >= MAX_RECOS:
        break  # Stop when max recommendations reached

    try:
        similarity = float(row[1].strip())
        rating = float(row[5].strip())

        if rating < MIN_RATING or similarity < MIN_SIMILAR:
            continue  # Skip movies that don't meet criteria

        movieId = int(row[2].strip())
        title = row[3].strip()
        genre = row[4].strip()
        totalRatings = int(row[6].strip())

        writer.writerow([movieId, title, genre, rating, totalRatings])

    except (ValueError, IndexError):
        continue  # Skip invalid rows
