#!/usr/bin/env python

import sys
import csv

writer = csv.writer(sys.stdout, quoting=csv.QUOTE_NONNUMERIC)
reader = csv.reader(sys.stdin)

for row in reader:
    try:
        if row[0].strip() == 'movieId':
            continue  # Skip header row

        movie_id = int(row[0].strip())

        if len(row) == 4:  # Ratings.csv format (movieId, rating, totalRatings)
            writer.writerow([movie_id, 'rating', float(row[1].strip()), int(row[2].strip())])
        else:  # Movies.csv format (movieId, title, genres)
            writer.writerow([movie_id, 'profile', row[1].strip(), row[2].strip()])

    except (IndexError, ValueError):
        continue  # Skip malformed rows
