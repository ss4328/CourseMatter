# CourseMatter
Django Web-App for managing courses/users. BlogMatter takes your Markdown Content, renders it into a HTML templates, and spits out a complete, Dynamic Blog ready to be served by Heroku, Nginx or another web server.

# Core Competencies
- Fast deployment via heroku
- Completely Free
- Custom Blog Models
- Integrated Heroku-PostGreSQL 
- Syntax Highlighting for course-content (you can add code to the course content via markdown!)

## Getting Started
- Set up the repo
- Read up on the configuration
- Create a superuser for Django admin Panel 
- Fork/Contribute your own modifications (Optional)

### 1. Set up the repo
You could also leverage a virtual environment (Highly recommended)
```bash
python3 -m venv <repo name>
source <repo name>/bin/activate
```

Set up the repo:
```bash
git clone https://github.com/ss4328/CourseMatter.git
pip install -m requirements.txt 
cd CourseMatter
python manage.py runserver
# => Starting development server at http://127.0.0.1:8000/
```
### 2. Configuration
All settings are managed via CourseMatter/settings.py
- [Markdownify's flag settings](https://github.com/matthewwithanm/python-markdownify)
- Static File Directories (Set up in STATIC_URL variable)
- To make DB migrations, 
```bash
python manage.py migrate
```

### 3. Superuser Creation
From the root directory (where manage.py resides), run:
```bash
python manage.py createsuperuser 
```
Expected Flow: 
```bash
Enter your desired username and press enter.
Username: admin
Email address: admin@example.com
Password: **********
Password (again): *********
Superuser created successfully.
```

### 4. Browsing by tags
After creating some a content object (manually you can navigate to /add_content), you can click on the tag and then navigate to all the posts available for the tag.

## Demo

## Hosting
I think the easiest option to go along is to host on Heroku. Why?
- We've already set up the Procfile in the project with auto migration build support. 
- It's as easy as:
```bash
brew install heroku/brew/heroku
heroku login
=> heroku: Press any key to open up the browser to login or q to exit
 ›   Warning: If browser does not open, visit
 ›   https://cli-auth.heroku.com/auth/browser/***
=> heroku: Waiting for login...
=> Logging in... done
=> Logged in as me@example.com
heroku create
git push heroku master
heroku open
```
- Production logs are easily viewable
```bash
heroku logs --tail
```
- Migrations are easy on the server
```bash
heroku python manage.py makemigrations
heroku python manage.py migrate
```

Optionally now you could do some simple DNS Setup if you've a custom domain.


### Follow up & Important links
1. https://blog.usejournal.com/deploying-django-to-heroku-connecting-heroku-postgres-fcc960d290d1
2. https://devcenter.heroku.com/articles/django-app-configuration


### Work in Progress
1. User Profile integration (currenty disrupted the registration flow)
2. Course-Content Hierarchy - a simple many-to-one relationship
3. Instructor-privileges integration
4. Hosting gunicorn error resolutions



