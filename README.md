<h1 align="center">Catch Your Tea</h1>

Catch Your Tea is a (fictitious) e-commerce online shop. The store is created for lovers of drinking various teas. The user can easily navigate through all pages and choose a product from among many different kinds of teas comming from China. The store offers black, green and white teas. After reading the description and testimonials of other customers, the buyer can purchase a different amount of tea.

![responsive mockup](https://res.cloudinary.com/dguqjbr12/image/upload/v1721071254/catch%20your%20tea/Zrzut_ekranu_389_emftac.png)

[Link to live site](https://catch-your-tea-da707f1e0a72.herokuapp.com/)


## Table of Contents

- [UI/UX)](#uiux)
  - [Agile](#agile)
  - [Site Goals](#site-goals)
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
   

## UI/UX

The created website is user-friendly and has a visually attractive interface. It was important to keep the interface simple and easy to understand. The website provides immediate and clear feedback on user actions.

### Agile

This project was designed and built using the agile approach. I created a [GitHub project](https://github.com/users/MarzenkaS/projects/15) and used the Kanban board method to divide project elements into user stories.
All user stories include their required acceptance criterias refer to the project linked to above. Each story has also been labeled to how important a particular feature is for the project to function well.

### Site Goals

This website is a fictitious online store selling various teas. The headquarters of this company is in Berlin.
On the website, customers can choose from black, green and white teas. The customer pays for the products by card and the parcel is sent to the recipient. The website provides high-quality products. Each customer has access to testimonials to see the opinions of other customers. They can also easily contact the company using the contact form or Facebook.

### 5 Planes of UX

#### Strategy
It meets the user's needs and product goals. A website intended for tea lovers. The scope of the website is global. The website helps the user to easily review and purchase teas. Easy contact with the company and the ability to add testimonials.

#### Scope
Defines what functions and features are included in the scope of the project.
The key to this project was the basic and necessary e-commerce functionality. The most of the available features are basic requirements. Features such as user registration and login, user profile creation, checkout functionality and secure online payments, as well as basic CRUD functionality for authorized users had to be implemented.

#### Structure
It determines how users can navigate the site and use all existing features.
The structure of the website is based on a basic e-commerce application.
The structure allows users to browse products and make purchases, as well as visit the testimonials page. Authenticated users can store their personal information in their user profile for faster order processing. They can also add products to their wishlist for later.

#### Skeleton
Inserts functions defined in the structure into navigation elements. The navigation bar and main content have a standard layout. The navigation bar contains links to the main features and functions of the site. On small and medium screens, the burger drop-down menu replaces the full navigation bar.
The cart link in the navigation bar is updated every time a user adds a product.
Products are displayed in card form. Testimonials are on separate page.
Buttons and links have appropriate names.

#### Surface
The surface of project encompasses all the visual and interactive elements that users interact with.


## Features
### Existing Features

Navigation Bar
- Navigation bar is available on all pages and includes clickable logo and nav links.
- User can search product from Search bar
- Allows to easily navigate between pages
- Easy access to the My Account icon
- Includes Shopping Bag icon under which user can see current total cost
- Collapsible burger menu with drop-down on small to medium screens

![]()
![]()
![]()
![]()

My Account
- Allows user to create an account or log in and after log out
- Username, password and password confirmation are required, email (optional)
- It allows user to see ,my profile' and from there Order History and delivery information
- Site owner has Product Management site from where can add a new product for selling

![]()

Login
- For registered already user
- Username and password required
- Contains "Remember me" option
- After signed in, user see confirmation
- When username or password are incorrect, user will be informed
- When user forgets password can recover it by clicking on button Forgot Password

![]()
![]()
![]()

Logout
- After user clicks on logout link in nav bar from My Account icon, will see confirm form
- Then user will be redirected to home page with confirmation message about being signed out

![]()
![]()

Contact
- Contact form allows user to send any question to company

![]()

Testimonials
- Any user can add a testimonial if logged in
- Any user can delete or update own testimonials

![]()
![]()
![]()

Wishlist
- For logged in user this page allows to keep product for later purchase
- There is button here which redirects user to product detail page where can amount and quantity of product be choosen

![]()
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
![]()

### Future Features

- Increase number of products on site
- Add videos how to prepare some teas

## Database Design

### Database Model

The database model diagram was designed using [draw.io](https://app.diagrams.net/) 

![ERD1](https://res.cloudinary.com/dguqjbr12/image/upload/v1721158664/catch%20your%20tea/ERD1_uhwp9v.png)
![ERD2](https://res.cloudinary.com/dguqjbr12/image/upload/v1721158665/catch%20your%20tea/ERD2_nykp1l.png)

### Custom Model

To build my models, I followed the Boutique Ado walkthrough project created by the Code Institute and adapted some Models for my project's requirements by removing or adding fields. I have changed UserProfile ( profiles app), Product ( products app), Order ( checkout app) and OrderLineItem ( checkout app) Models.

I added required Custom Models not covered in the walkthrough in 3 new added app:
- Contact Model ( Contact app)
- Wishlist Model ( Wishlist app)
- Testimonial Model and ProductTestimonial Model ( Testimonials app)

### CRUD

1- Full CRUD functionality is implemented for admin user in the Products app, Testimonials app.

2- The CRUD principle I did for my original Testimonial Model 

CRUD Testimonial Model:

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

## Used technologies

### Work Environments and Hosting

- [Lucid](https://lucid.app/) (ERD diagrams)
- [GitHub](https://github.com/) (Version control)
- [GitPod](https://gitpod.io/) (IDE)
- [Heroku](https://heroku.com/) (Site hosting)
- [AWS - Amazon Web servises (S3)](https://aws.amazon.com/) (Hosting static and media files)
- [Cloudinary](https://cloudinary.com/) (Serving static media files)


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
- [Bootstrap4.6 template pack for django-crispy-forms](https://pypi.org/project/crispy-bootstrap4.6/)

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