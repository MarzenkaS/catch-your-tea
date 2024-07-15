<h1 align="center">Catch Your Tea</h1>

Catch Your Tea is a (fictional) e-commerce online shop. The store is created for lovers of various teas. The user can easily navigate through all pages and choose a product from among many different kinds of teas comming from China. The store offers black, green and white teas. After reading the description and testimonials of other customers, the buyer can purchase a different amount of tea.

![responsive mockup](https://res.cloudinary.com/dguqjbr12/image/upload/v1721071254/catch%20your%20tea/Zrzut_ekranu_389_emftac.png)

[Link to live site](https://catch-your-tea-da707f1e0a72.herokuapp.com/)


## Table of Contents

- [User Experience(UX)](#user-experience(UX))
  - [Agile](#agile)
- [Features](#features)
    - [Existing Features](#existing-features)
    - [Future Features](#future-features)
- [Database Design](#database-deign)
  - [Database Model](#database-model)
  - [Custom Model](#custom-model)
  - [CRUD](#crud)
- [Testing](#testing)
  - [Validator testing](#validator-testin)
  - [Lighthouse](#lighthouse)
  - [Other browsers](#other-browsers)
  - [Different screen sizes](#different-screen-sizes)
  - [Bugs](#bugs)
- [Technologies Used](#technologies-used)
- [Deployment](#deployment)     
- [Credits](#credits)     
  - [Content](#content)     
  - [Media](#media)     
   

## User Experience(UX)
### Agile

## Features
### Existing Features
Navigation Bar
- Navigation bar is available on all pages and includes clickable logo and nav links.
- Allows to easily move between pages.
- Collapsible burger menu with drop-down on small to medium screens

![]()
![]()
![]()
![]()

My Account
- Allows user to create an account or log in
- Username, password and password confirmation are required, email (optional)

![]()

Login
- For registered already user
- Username and password required
- Contains "Remember me" option
- After signed in, user see confirmation
- When username or password are incorrect, user will be informed

![]()
![]()
![]()

Logout
- After user clicks on logout link in nav bar, will see confirm form
- Then user will be redirected to home page with confirmation message about being signed out

![]()
![]()

Contact
- An authenticated user from nav bar can navigate to add review page
- Afte adding review and clicking Submit button will see confirmation
- User can delete or edit and update own review
- Confirmation message about delete and update will be shown to a user

![]()

Testimonials

![]()

Wishlist

![]()

Home page
- Includes welcome paragraph short introduction to website and button shop now

![]()
![]()

Footer
- User can find a Facebook link and follow shop on Facebook 
- There is Subscribe form so user can receive special offers
- At very bottom of page user can open Privacy Policy

![]()


### Future Features

## Database Design
### Database Model

The database model diagram was designed using [draw.io](https://app.diagrams.net/) 

![]()

### Custom Model

To build my models, I followed the walkthrough project created by the Code Institute and adapted product Model for my project's requirements.
I added required Custom Models not covered in the walkthrough - Contact Model, Wishlist Model and Testimonials Model

### CRUD
The CRUD principle I did for my original Testimonials Model 

CRUD Testimonials Model:

Create: An authenticated user can create own testimonial

Read: A user can see and read own and other users' testimonials

Update: An authenticated user can edit and update own testimonial

Delete: An authenticated user can delete own testimonials


Features visualized here [Existing Features](#existing-features)

## Testing
### Validator testing

HTML W3C validator

- Home page

![]()

- 

![]()

- 

![]()

CSS W3C validator

No errors

![]()

JavaScript JSHint

![]()

Python CI Python Linter

- products app ????? add others app

No errors in admin.py, urls.py, models.py, views.py

- My dog project app

No errors in settings.py and urls.py


### Lighthouse
I made a Lighthouse while being incognito. Had some issues to achieve high Accessibility and SEO.
- 
- 

1. Desktop

![]()

2. Mobile

![]()

### Other browsers
I tested my website on Google Chrome, Microsoft Edge, Mozilla Firefox and Safari. All functionality works.

### Different screen sizes
Thanks to Bootstrap my project is responsive on all device sizes

### Bugs

## Technologies Used

### Work Environments and Hosting

- [Lucid](https://lucid.app/) (ERD diagrams)
- [GitHub](https://github.com/) (Version control)
- [GitPod](https://gitpod.io/) (IDE)
- [Heroku](https://heroku.com/) (Site hosting)
- [AWS - Amazon Web servises (S3)](https://aws.amazon.com/) (Hosting static and media files)


### Python Libraries

- [Gunicorn](https://pypi.org/project/gunicorn/) (Python HTTP server for WSGI applications)
- [pyscopg2](https://pypi.org/project/psycopg2/) (PostgreSQL Database adapter)
- [Pillow](https://pypi.org/project/Pillow/) (Python Imaging Library)
- [boto3](https://boto3.amazonaws.com/v1/documentation/api/latest/index.html) (integrates python libraries with AWS services)
- [django-storages](https://django-storages.readthedocs.io/en/latest/) (collection of custom storage backends for Django)
- [Flake8](https://flake8.pycqa.org/en/latest/) (Python linter used for python code validation)

### Django Libraries

- [django-allauth](https://django-allauth.readthedocs.io/en/latest/) (User authentication)
- [django-crispy-forms](https://django-crispy-forms.readthedocs.io/en/latest/) (Control rendering behaviour of Django forms)
- [Bootstrap5 template pack for django-crispy-forms](https://pypi.org/project/crispy-bootstrap4.6/)
- [django-summernote](https://github.com/summernote/django-summernote) (WYSIWYG HTML editor)

### Payment processing

- [Stripe](https://stripe.com/) (Online payment platform)

### Emails/Newsletter

- [Gmail](https://mail.google.com/) (Real email sending)
- [Mailchimp](https://mailchimp.com/) (Automated newsletter subscription service)


### SEO/Marketing

- [XML Sitemaps](https://www.xml-sitemaps.com/) (Sitemap generator)
- [Privacy Policy Generator](https://www.privacypolicygenerator.info/)

## Deployment

## Credits
### Content
### Media