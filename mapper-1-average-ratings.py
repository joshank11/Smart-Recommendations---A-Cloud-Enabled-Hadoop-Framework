#!/usr/bin/env python

import sys
import csv

reader = csv.reader(sys.stdin)
next(reader, None)  # Skip header row

for row in reader:
    try:
        movie_id, rating = row[1], row[2]
        print(f"{movie_id},{rating}")
    except IndexError:
        continue  # Skip malformed rows
