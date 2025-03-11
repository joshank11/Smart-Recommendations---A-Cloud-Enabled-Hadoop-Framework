#!/usr/bin/env python

import sys
from math import sqrt
import csv

# Read factors from command-line args (default: 1 for genre, 4 for rating)
try:
    GENRE_FACTOR = float(sys.argv[1]) if len(sys.argv) > 1 else 1
    RATING_FACTOR = float(sys.argv[2]) if len(sys.argv) > 2 else 4
except ValueError:
    print("Invalid factors, using defaults (GENRE=1, RATING=4).", file=sys.stderr)
    GENRE_FACTOR, RATING_FACTOR = 1, 4

movieId, genres, rating, totalRatings, setA = None, None, 0, 0, None

reader = csv.reader(sys.stdin)
writer = csv.writer(sys.stdout, quoting=csv.QUOTE_NONNUMERIC)

for row in reader:
    try:
        kind = row[0]
        cMovieId = int(row[1])
        cTitle = row[2]
        cAllGenre = row[3]
        cGenres = set(cAllGenre.split('|'))
        cRating = float(row[4])
        cTotalRatings = int(row[5])

        if kind == 'a':  # Reference movie
            movieId, genres, rating, totalRatings = cMovieId, cGenres, cRating, cTotalRatings
            setA = [GENRE_FACTOR] * len(genres) + [cRating * RATING_FACTOR, cTotalRatings ** (1 / 3)]
            continue

        # Compute genre-based vector
        setB = [GENRE_FACTOR if genre in cGenres else 0 for genre in genres]
        
        if sum(setB) == 0:
            continue  # Skip movies with no common genres

        setB.extend([cRating * RATING_FACTOR, cTotalRatings ** (1 / 3)])

        # Compute cosine similarity
        numerator = sum(a * b for a, b in zip(setA, setB))
        denominatorA = sqrt(sum(a ** 2 for a in setA))
        denominatorB = sqrt(sum(b ** 2 for b in setB))
        denominator = denominatorA * denominatorB

        if denominator == 0:
            continue  # Avoid division by zero

        similarity = round(numerator / denominator, 5)
        writer.writerow([similarity, cMovieId, cTitle, cAllGenre, cRating, cTotalRatings])

    except (ValueError, IndexError):
        continue  # Skip invalid rows
