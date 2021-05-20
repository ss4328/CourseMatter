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
python3 -r venv <repo name>
source <repo name>/bin/activate
```

Set up the repo:
```bash
git clone https://github.com/ss4328/CourseMatter.git
pip install -r requirements.txt 
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

Note: I used admin, admin as user,password for simplicity. You can try to log in with that if the SQLite DB is committed in the end. 

### 4. Browsing by tags
After creating some a content object (manually you can navigate to /add_content), you can click on the tag and then navigate to all the posts available for the tag.


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


## Demo

Home Page
![img](https://i.postimg.cc/LX9q74hC/home1.png)

![img](https://i.postimg.cc/JnpyWwk1/home2.png)

admin panel
![admin](https://i.postimg.cc/RVL0rx52/admin.png)

content-detail
![img](https://i.postimg.cc/v8PnJnrW/content-detail.png)

course-detail
![img](https://i.postimg.cc/dVCTZSzB/course-detail.png)

dashboard
![img](https://i.postimg.cc/L6w1XM05/dashboard.png)

edit-Profile
![img](https://i.postimg.cc/25Fb2LjL/edit-Profile.png)

login/Signup
![img](https://i.postimg.cc/MKvBqG5g/login.png)

tag-view
![img](https://i.postimg.cc/Xv0BfkW0/tag-view.png)



## Tech Stack
- I used Django for Back-end for the following reasons:
    - Allows integrated admin panel to save development time
    - Very friendly support for user management
    - In built view rendering forms which I used liberally
    - Very easy-to-frame query inspection by manage.py dbshell
    - In-build user groups.
    - Django uses MVC, which is very powerful pattern. You call the Controller the “view”, and the View the “template”
        - In mvt, a request to a URL is dispatched to a View. This View calls into the Model, performs manipulations and prepares data for output. The data is passed to a Template that is rendered an emitted as a response. ideally in web frameworks, the controller is hidden from view.
- And I used Bootstrap Framework for the front-end. I'm proficient in React which could have been used to improve performance and code readability. However, Bootstrap is very dev-friendly and quick to use and create.
    - Allows for Responsive UI which is VERY nice to have.
    - Amazing documentation and community.
    - Traded off performance for development speed. 

- Heroku for Deployment: Very nice support for PostGreSQL and very easy deployment.
- PostGreSQL - object-relational database, table inheritance and function overloading which although not used much, are amazing for later stages of the product and allow more flexibility & relational features.



## Summary of what's built
For all purposes, Author is just an alias for a teacher
### Content/Course
- CRUD for course, CRUD for Course Content
- Integrated Markdown support to allow:
    - Photos via markdown
    - Videos via markdown
    - Code via markdown
    - Tables via markdown
- Custom Course and Content Model via one-to-many relationship
- Pagination for course/content pages
- Only the author of the course/content or Admin can change course content.
- Search for course/content on admin Django Admin panel via content/title.

### Users & Authentication
- Login/Signup View for users
- Integrated django-admin panel that allows Admin to escalate priveleges for any user by assigning teacherGroup.
- User Groups: Teacher
    - Teacher can edit/add/delete course and content
    - Cascade on courses and users
        - When a course is deleted, the subsequent content is deleted
        - When a user is deleted, all his/her content is deleted (can be changed with a DB migration by removing cascade option)
    - Edit Profile page (some fixes needed but shows I can easily made those changes working full-time)
- Enhanced User model for additional profile attributes: DOB, Country, first_name & last_name.
- Search for a user by name.
- Search by profile details.

### Views
- Home view: Gives recent posts by reverse-chronological sorted order, Content by tag, Course list.
- Author View: View all courses and subsequent content by a particular Author, for all Authors (with edit/delete button if you're the author).
- Login/Signup/forgot password/edit profile/ dashboard by the top-right dropdown menu.
- Course-View: See all content of a course (with edit/delete button if you're the author)
- Tag View: - View all courses and subsequent content by tag (Eg: Python is tagged in Computer-Science) and Content.

### Front-End
- Simplistic, yet elegant UI via bootstrap framework (Although not a requirement, I couldn't do the development justice without a UI to show potential)
- Custom made templates that are very generic to be used in multiple pages.
- Edit/Delete button beside author's own posts. Allows for easy updates or deletions.

### Deployment and Documentation
- Heroku Deployment Instructions, procfile, etc to allow extremely fast hosting (I've done it previously for my blog)
- Comments in code are breakdown by CRUD functionalities.


## Decisions and Tradeoffs
- I started off with creating model for content and setting up the homepage. 
    - Allowing Markdown-rendering in the model itself is extremely powerful! Although users must be familiar with the syntax, it's not hard to catch. 
    - The tradeoff is: **Syntax for flexibility**. Markdown allows for embedding photos, videos, tables, hyperlinks, presentations (github/gnab/remark), & CODE!
    - I wanted to make something unique & Flexible. Markdown in my opinion is perfect for flexibility and the intergration is sure to be unique!
- Then a custom User Model -> Country, DOB, user name
    - Allows for later features to filter users
- one-to-many Course-to-Content. Allows very fast lookup for content for a course.
- PostGreSQL (read tech-stack section)


## Sample Workflow to test features
- Log in as Admin
    - test if the admin,admin credentials work or create new superuser
- Register several users: A,B,C,D
- Log in to django admin panel
    - Go to usergroups
        - Assign A,B as teachers
    - (Don't assign C,D in teacherGroup)
- Now dashboard accessible from top-right menu for A,B (but not for C,D)
- You can now add content and courses for C,D along with Tags 

Verification
- Tags show up as categories on the sidebar
- Courses show up on homepage and courseView
- Content Show up on the assigned Courses
- Edit/Delete buttons are only available for authenticated teachers on their own content and dashboard is invisible for students.  

Bug Alert!
- You've to add atleast one content in a course to allow django to display its attributes on the course page
    - Easily fixable by passing course context data in a context dictionary as done in the homepage
    - Left bug for time constraints


    

## Areas for Improvement
#### Front-End
- Revamp on React.js
- Images support for the content

### Back-End
- Filter Users by their profile attributes (Eg. Country)
- Questions integration! Let's make a integration for questions and quizzes in addition to content in a course! 
    - I've made an extensive Testing system for Java supporting: Multiple choice, True/False, Matches, Multiple-correct, short and long answer based questions
    - Repo: 
    - Converting to python or having an adapter to translate requests would be perfect!
- Extended user Profile: 
    - Twitter/Youtube integration to allow quick linking
    - Current Level, University/School 
- Course Recommendation Algorithm: Based on the courses user is interested in, we can suggest similar to user and link similar courses on a course-detail view page
- Discus integration for comments.
- Ratings for courses and Content.
    - I've made a commenting system for [Versa](https:www.versa.vercel.app)
- Subscription functionalities & Payment integration via Strips
- End to End unit tests 

### Infrastructure
- Docker containerization. 
    - I have experience in this
- ECS deployment rather than heroku for the application
- Separate PostGreSQL instance on AWS with consistent backups

### Follow up & Important links
1. https://blog.usejournal.com/deploying-django-to-heroku-connecting-heroku-postgres-fcc960d290d1
2. https://devcenter.heroku.com/articles/django-app-configuration


##Technical Questions:
#### What libraries did you add to the frontend? What are they used for?

###### Tech Stack
- I used Django for Back-end for the following reasons:
    - Allows integrated admin panel to save development time
    - Very friendly support for user management
    - In built view rendering forms which I used liberally
    - Very easy-to-frame query inspection by manage.py dbshell
    - In-build user groups.
    - Django uses MVC, which is very powerful pattern. You call the Controller the “view”, and the View the “template”
        - In mvt, a request to a URL is dispatched to a View. This View calls into the Model, performs manipulations and prepares data for output. The data is passed to a Template that is rendered an emitted as a response. ideally in web frameworks, the controller is hidden from view.
- And I used Bootstrap Framework for the front-end. I'm proficient in React which could have been used to improve performance and code readability. However, Bootstrap is very dev-friendly and quick to use and create.
    - Allows for Responsive UI which is VERY nice to have.
    - Amazing documentation and community.
    - Traded off performance for development speed. 

- Heroku for Deployment: Very nice support for PostGreSQL and very easy deployment.
- PostGreSQL - object-relational database, table inheritance and function overloading which although not used much, are amazing for later stages of the product and allow more flexibility & relational features.

#### What's the command to start the application locally?
After cloning the repo,
```bash
cd courseMatter
python manage.py runserver
```

#### How long did you spend on the coding project? What would you add to your solution if you had more time? If you didn't spend much time on the coding project, then use this as an opportunity to explain what you would add.
I had an incredibly busy last 10 days with Capstone project [Versa](http://www.cci.drexel.edu/SeniorDesign/2020_2021/Versa/index.html) so my availability has been very tight. I managed to devote around 8 hours for this project.


I'd do parts of the backend (everything but payment integration and recommendation algorithm) if I had more time. I'd finish the Infrastructure improvements for sure within extra couple hours.

#### What was the most useful feature that was added to the latest version ofyour chosen language? Please include a snippet of code that shows howyou've used it.
I'm a huge python fan! I'm enjoying the latest dictionary updates in python 3.9.0

```python

pycon = {2016: "Portland", 2018: "Cleveland"}
europython = {2017: "Rimini", 2018: "Edinburgh", 2019: "Basel"}

{**pycon, **europython}
{2016: 'Portland', 2018: 'Edinburgh', 2017: 'Rimini', 2019: 'Basel'}

merged = pycon.copy()
for key, value in europython.items():
     merged[key] = value

merged
{2016: 'Portland', 2018: 'Edinburgh', 2017: 'Rimini', 2019: 'Basel'}
```
#### How would you track down a performance issue in production? Have you ever had to do this?
I had to work with production issues in my coop at SIG. I'd host my code on AWS and check the logs about the requests which were accepted/denied/served and check if there's a pending issue or discrepancies on the metrics.
Usually, CI/CD infrastructure catches code issues before they are merged. I'd add test cases for concurrency & performance so sub-par code isn't committed.

### Work in Progress
- N/A


