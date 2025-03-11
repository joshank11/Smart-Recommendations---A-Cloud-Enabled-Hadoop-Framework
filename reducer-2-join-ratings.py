#!/usr/bin/env python

import sys
import csv

class Profile:
    def __init__(self):
        self.movieId = None
        self.title = None
        self.genre = None
        self.rating = None
        self.totalRatings = None

def setProfile(row, profile=None):
    if profile is None:
        profile = Profile()

    if row[1] == 'profile':
        profile.movieId = int(row[0].strip())
        profile.title = row[2].strip()
        profile.genre = row[3].strip()
    elif row[1] == 'rating':
        profile.movieId = int(row[0].strip())
        profile.rating = float(row[2].strip())
        profile.totalRatings = int(row[3].strip())
    
    return profile

movieId = None
profile = None

print('movieId,title,genre,rating,totalRatings')

writer = csv.writer(sys.stdout, quoting=csv.QUOTE_NONNUMERIC)
reader = csv.reader(sys.stdin)

for row in reader:
    try:
        cid = int(row[0].strip())  # Convert movieId to int

        if movieId != cid:
            if movieId is not None:
                writer.writerow([
                    profile.movieId, profile.title, profile.genre,
                    profile.rating if profile.rating is not None else "N/A",
                    profile.totalRatings if profile.totalRatings is not None else 0
                ])

            movieId = cid
            profile = setProfile(row)
        else:
            profile = setProfile(row, profile)
    
    except (ValueError, IndexError):
        continue  # Skip malformed rows

if movieId is not None:
    writer.writerow([
        profile.movieId, profile.title, profile.genre,
        profile.rating if profile.rating is not None else "N/A",
        profile.totalRatings if profile.totalRatings is not None else 0
    ])
