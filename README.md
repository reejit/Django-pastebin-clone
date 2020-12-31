# Django pastebin clone
    Pastebin clone using DRF to help you share codes and notes with your friends,
    if you don’t know Pastebin , just google it 

# Features:
    • Each user can create edit delete any of his pastes.
    • allow anonymous guests to create pastes as well.
    • Each user can filter pastes by dates.
    • Each user can choose to share this snippet with certain users
    • token-based authentication system.
    • Helper scripts to export statistics about the project in excel or csv (eg. Number of pastes for each user) 
    • Each paste has a shortened URL 
    • Each paste can be either shared to public or  a certain users or set to private only for the creator
    
# Run:
    clone repo
    pip install django==2.0.0 django_rest_framework==3.12.2
    python manage.py runserver
    
# For All API endpoints:
    go to: http://yourhost/docs/ , eg. http://localhost:8000/docs/
