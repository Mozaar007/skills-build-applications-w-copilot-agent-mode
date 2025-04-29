# Test data for octofit_db

data = {
    "users": [
        {"email": "thundergod@mhigh.edu", "name": "Thor"},
        {"email": "metalgeek@mhigh.edu", "name": "Tony Stark"},
        {"email": "zerocool@mhigh.edu", "name": "Steve Rogers"},
        {"email": "crashoverride@hmhigh.edu", "name": "Natasha Romanoff"},
        {"email": "sleeptoken@mhigh.edu", "name": "Bruce Banner"},
    ],
    "teams": [
        {"name": "Blue Team"},
        {"name": "Gold Team"},
    ],
    "activities": [
        {"user": "thundergod@mhigh.edu", "description": "Cycling", "date": "2025-04-29T10:00:00Z"},
        {"user": "metalgeek@mhigh.edu", "description": "Crossfit", "date": "2025-04-29T11:00:00Z"},
        {"user": "zerocool@mhigh.edu", "description": "Running", "date": "2025-04-29T12:00:00Z"},
        {"user": "crashoverride@hmhigh.edu", "description": "Strength", "date": "2025-04-29T13:00:00Z"},
        {"user": "sleeptoken@mhigh.edu", "description": "Swimming", "date": "2025-04-29T14:00:00Z"},
    ],
    "leaderboard": [
        {"team": "Blue Team", "score": 100},
        {"team": "Gold Team", "score": 90},
    ],
    "workouts": [
        {"user": "thundergod@mhigh.edu", "type": "Cycling", "duration": 60},
        {"user": "metalgeek@mhigh.edu", "type": "Crossfit", "duration": 120},
        {"user": "zerocool@mhigh.edu", "type": "Running", "duration": 90},
        {"user": "crashoverride@hmhigh.edu", "type": "Strength", "duration": 30},
        {"user": "sleeptoken@mhigh.edu", "type": "Swimming", "duration": 75},
    ],
}