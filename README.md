<h1 align="center">Catch Your Tea</h1>

Catch Your Tea is a (fictitious) e-commerce online shop. The store is created for lovers of drinking various teas. The user can easily navigate through all pages and choose a product from among many different kinds of teas comming from China. The store offers black, green and white teas. After reading the description and testimonials of other customers, the buyer can purchase a different amount of tea.

![responsive mockup](https://res.cloudinary.com/dguqjbr12/image/upload/v1721071254/catch%20your%20tea/Zrzut_ekranu_389_emftac.png)

[Link to live site](https://catch-your-tea-da707f1e0a72.herokuapp.com/)


## Table of Contents

- [UI/UX)](#uiux)
  - [Agile](#agile)
  - [Site Goals](#site-goals)
  - [5 Planes of UX](#5-planes-of-ux)
- [SEO and Web Marketing](#seo-and-web-marketing)
- [Features](#features)
    - [Existing Features](#existing-features)
    - [Future Features](#future-features)
    - [Custom 404 page](#custom-404-page)
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

## SEO and Web Marketing

An overview of the marketing research for this project can be found here [SEO and Web Marketing file](MARKETING.md)

## Features
### Existing Features

Navigation Bar
- Navigation bar is available on all pages and includes clickable logo and nav links.
- User can search product from Search bar
- Allows to easily navigate between pages
- Easy access to the My Account icon
- Includes Shopping Bag icon under which user can see current total cost
- Collapsible burger menu with drop-down on small to medium screens

1- navbar view
![navbar](https://res.cloudinary.com/dguqjbr12/image/upload/v1721167251/catch%20your%20tea/navbar_tvlmxi.png)

2- all products view
![all products](https://res.cloudinary.com/dguqjbr12/image/upload/v1721167254/catch%20your%20tea/all.products_x365vj.png)

3- product detail view
![product detail](https://res.cloudinary.com/dguqjbr12/image/upload/v1721167252/catch%20your%20tea/product.detail_j8rgcy.png)

4- add to bag view
![add to bag](https://res.cloudinary.com/dguqjbr12/image/upload/v1721167253/catch%20your%20tea/add.to.bag_omphkw.png)

5- shopping bag view
![shopping bag](https://res.cloudinary.com/dguqjbr12/image/upload/v1721167252/catch%20your%20tea/shopping.bag_dkugr2.png)

6- order confirmation view
![order confirmation](https://res.cloudinary.com/dguqjbr12/image/upload/v1721168901/catch%20your%20tea/order.confirmation_xhuwya.png)


My Account
- Allows user to create an account or log in and after log out
- Username, password and password confirmation are required, email (optional)
- It allows user to see ,my profile' and from there Order History and delivery information
- Site owner has Product Management site from where can add a new product for selling

![my account](https://res.cloudinary.com/dguqjbr12/image/upload/v1721167251/catch%20your%20tea/my.account_dsnxtj.png)
![register](https://res.cloudinary.com/dguqjbr12/image/upload/v1721167252/catch%20your%20tea/register_xnpkra.png)
![my profile](https://res.cloudinary.com/dguqjbr12/image/upload/v1721167251/catch%20your%20tea/my.profile_obcddm.png)
![product management](https://res.cloudinary.com/dguqjbr12/image/upload/v1721167254/catch%20your%20tea/product.management_qp1sus.png)


Login
- For registered already user
- Username and password required
- Contains "Remember me" option
- After signed in, user see confirmation
- When username or password are incorrect, user will be informed
- When user forgets password can recover it by clicking on button Forgot Password

![sign in](https://res.cloudinary.com/dguqjbr12/image/upload/v1721167252/catch%20your%20tea/sign.in_ukyfi4.png)


Logout
- After user clicks on logout link in nav bar from My Account icon, will see confirm form
- Then user will be redirected to home page with confirmation message about being signed out

![sign out](https://res.cloudinary.com/dguqjbr12/image/upload/v1721167252/catch%20your%20tea/sign.out_b6zwvx.png)
![]()


Contact
- Contact form allows user to send any question to company

![contact](https://res.cloudinary.com/dguqjbr12/image/upload/v1721167253/catch%20your%20tea/contact_qbeklo.png)


Testimonials
- Any user can add a testimonial if logged in
- Any user can delete or update own testimonials

![testimonial list](https://res.cloudinary.com/dguqjbr12/image/upload/v1721167252/catch%20your%20tea/testimonial.list_o1jbrx.png)
![add testimonial](https://res.cloudinary.com/dguqjbr12/image/upload/v1721167253/catch%20your%20tea/add.testimonial_unn6ng.png)
![edit testimonial](https://res.cloudinary.com/dguqjbr12/image/upload/v1721167254/catch%20your%20tea/edit.testimonial_exor16.png)
![delete testimonial](https://res.cloudinary.com/dguqjbr12/image/upload/v1721167254/catch%20your%20tea/delete.testimonial_hifrhl.png)


Wishlist
- For logged in user this page allows to keep product for later purchase
- There is button here which redirects user to product detail page where can amount and quantity of product be choosen

![wishlist](https://res.cloudinary.com/dguqjbr12/image/upload/v1721167252/catch%20your%20tea/my.wishlist_pffrw9.png)


Home page
- Includes welcome paragraph short introduction to website and button shop now

![home](https://res.cloudinary.com/dguqjbr12/image/upload/v1721167260/catch%20your%20tea/home_guokcq.png)


Footer
- User can find a Facebook link and follow shop on Facebook 
- There is Subscribe form so user can receive special offers
- At very bottom of page user can open Privacy Policy

![footer](https://res.cloudinary.com/dguqjbr12/image/upload/v1721167260/catch%20your%20tea/footer_wg2lco.png)

### Future Features

- Increase number of products on site
- Add videos how to prepare some teas
- Create forum for users
- The overall rating of the product should change depending on how users rate the tea
- Available product stocks visible to the user

### Custom 404 page

Custom 404 page displays when a user tries to access a URL that does not exist. Back button redirects user back to home page.

![404 page](https://res.cloudinary.com/dguqjbr12/image/upload/v1721336870/catch%20your%20tea/404page_y41ocn.png)

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

1. HTML W3C validator

- templates
![]()

- 
![]()

- 
![]()

- 
![]()

- 
![]()


2. CSS W3C validator

No errors
![css validator](https://res.cloudinary.com/dguqjbr12/image/upload/v1721404650/catch%20your%20tea/css_z4lvcl.png)


3. JavaScript JSHint

- stripe_elements.js 

Line 12 One undefined variable Stripe (variable is inherent in Stripe functionality)
Line 117 missing semicolon

- quantity_input_script.html 

No errors


4. Python CI Python Linter

All files are error-free, some had errors because the code line was too long.

- bag app

No errors in urls.py, views.py, custom_filters.py, contexts.py

- checkout app

No errors in admin.py, forms.py, models.py, views.py, urls.py, webhook_handler.py, webhooks.py

- contact app

No errors in forms.py, models.py, urls.py, views.py

- home app

No errors in urls.py, views.py

- products app

No errors in forms.py, models.py, urls.py, views.py, widgets.py

- profiles app

No errors in forms.py, urls.py, views.py, models.py

- testimonials app

No errors in forms.py, models.py, urls,py, views.py

- wishlist app

No errors in views.py, urls.py, models.py


### Lighthouse

I made a Lighthouse while being incognito. 


1. Desktop

![desktop lighthouse](https://res.cloudinary.com/dguqjbr12/image/upload/v1721404666/catch%20your%20tea/lighthouse.desktop_oj4rrz.png)

2. Mobile

![mobile lighthouse](https://res.cloudinary.com/dguqjbr12/image/upload/v1721404662/catch%20your%20tea/lighthouse.mobile_hync0z.png)

The performance score resulting from referencing external libraries and technologies such as Bootstrap, JQuery and Stripe that the project relies on, cannot be higher.


### Other browsers
I tested my website on Google Chrome, Microsoft Edge, Mozilla Firefox and Safari. All functionality works.

### Different screen sizes
Thanks to Bootstrap my project is responsive on all device sizes

### Bugs


## Used technologies

### Languages
- [Python](https://www.python.org/) was used as the main scripting language
- [HTML](https://www.w3schools.com/html/) was used to present and structure content
- [CSS](https://www.w3schools.com/css/default.asp) was used to style content
- [JavaScript](https://www.w3schools.com/js/default.asp) ( [jQuery](https://jquery.com/) ) was used to manipulate DOM

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

## Framework
- [Django](https://www.djangoproject.com/) was used as the main Python framework
- [Bootstrap](https://getbootstrap.com/) was heavily used for styling

### Payment processing
- [Stripe](https://stripe.com/) (Online payment platform)

### Emails/Newsletter
- [Gmail](https://mail.google.com/) (Real email sending)
- [Mailchimp](https://mailchimp.com/) (Automated newsletter subscription service)

### SEO/Marketing
- [XML Sitemaps](https://www.xml-sitemaps.com/) (Sitemap generator)
- [Privacy Policy Generator](https://www.privacypolicygenerator.info/)


## Deployment

My project was deployed using [Heroku](https://heroku.com/), [ElephantSQL](https://www.elephantsql.com/) and [AWS](https://aws.amazon.com/).

#### Installing libraries

The following libraries needed for successful deployment on Heroku.

- Install **pyscopg2** (connects to PostgreSQL): ``pip 3 install dj_database_url pyscopg2``
- Install **Gunicorn** (server used to run Django on Heroku): ``pip3 install django gunicorn``

#### Creating the Heroku App

- Log into Heroku and go to the Dashboard
- Click **New** and select **Create new app** from the drop-down
- Name app appropriately and choose relevant region, then click **Create App**

#### Create PostgreSQL database using ElephantSQL

This is necessary to create a database that can be accessed by Heroku. The database provided by Django can not be accessed by the deployed Heroku app.

- Log into ElephantSQL and go to Dashboard
- Click **Create New Instance**
- Set up a plan by providing a Name (project name) and select a Plan (for this project the free plan "Tiny Turtle" was chosen).
- Click **Select Region** and choose appropriate Data center
- Click **Review**, check all details and click **Create Instance**
- Return to Dashboard on click on the name of the newly created instance
- Copy the database URL from the details section

#### Hiding sensitive information

- Create ``env.py`` file and ensure it is included in the ``.gitignore`` file
- Add ``import os`` to env.py file and set environment variable **DATABASE_URL** to the URL copied from ElephantSQL  os.environ.setdefault("DATABASE_URL", "copiedURL")
- Below, set **SECRET_KEY**  os.environ.setdefault('SECRET_KEY', 'mysecretkey')

#### Update Settings

- Add the following code at the top of ``settings.py`` to connect Django project to env.py:
    ````
      from pathlib import Path
      import os
      import dj_database_url
      if os.path.exists("env.py"):
          import env
    ````
- Remove insecure secret key provide by Django in settings.py and refer to variable in env.py instead ``SECRET_KEY = os.environ.get('SECRET_KEY', '')``

- To connect to new database, replace provided **DATABASE** variable with 
    ````
    DATABASES = {
        'default': dj_database_url.parse(os.environ.get("DATABASE_URL"))
    }
    ````
- Save and migrate all changes made and load in fixtures

#### Preparing for Heroku

- Create Procfile (tells Heroku to create web dyno which will run gunicorn and serve Django app)

- Temporarily disable collectstatic (prevent Heroku from collecting static files when deploying)

- Allow Heroku as host:

    In ``settings.py`` add
        ````
        ALLOWED_HOSTS = ['app-name.herokuapp.com', 'localhost', 'URL of deployed site from heroku and Gitpod']
        ````

#### Connecting Heroku to Database

- In Heroku dashboard, go to **Settings** tab
- Add three new config vars **DATABASE_URL** , **SECRET_KEY** and **PORT** (value "8000")


#### Deyploying with Heroku

- In Heroku dashboard, go to **Deploy** tab
- Select "GitHub" as Deployment method and choose correct repo
- Enable Automatic Deploys
- Click "Deploy Branch" button


#### Hosting images and static file with AWS

- Create AWS account and go to AWS Management Console in the My Account dropdown
- Find and access S3 as a service and create a new bucket:

    Under Object Ownership, check "ACLs enabled"

    Uncheck "Block all public access" and acknowledge (required for public access to static files)

- Configur bucket settings:

    Under **Properties**, enable Static Website Hosting

    Under **Permissions**, copy the following code into CORS section:

    ```
    [
        {
            "AllowedHeaders": [
                "Authorization"
            ],
            "AllowedMethods": [
                "GET"
            ],
            "AllowedOrigins": [
                "*"
            ],
            "ExposeHeaders": []
        }
    ]
    ```
    This is required to set up the access between the Heroku app and the S3 bucket.

    Under **Bucket policy**, go to Policy generator.

    Bucket Type = S3 Bucket Policy

    Principal = * (allows all principles)

    Actions = GetObject

    Paste in ARN from bucket settings tab.

    Click Add Statement, then Generate Policy.

    Copy policy in paste into bucket policy editor. Also add ``/*`` onto the end of the resource key.

    Click Save.

    Under **Access control list (ACL)**, check "List" checkbox for "Everyone (public access)"

- Create user to access bucket with IAM (Identity and Access Management)

    In IAM, got to User Groups (sidebar left).

    There create a group for a user, create an access policy giving the group access to the S3 bucket and assign the user to the group so it can use the policy to access all files. 

- Connect Django to S3

    Install packages "boto3" and "django-storages" and add ``'storages'`` to INSTALLED_APPS  in settings.py

    Configure settings.py accordingly, including necessary AWS variables.

    Add new config vars in Heroku app settings, including user credentials from AWS.

    Create ``custom_storages.py`` file.

- Upload static files and media files to S3


#### Add Stripe keys to Heroku

From Stripe account, under Developers > API keys copy Public Key and Secret Key and set as config vars in Heroku app settings, Gitpod settings and add to env.py

Create new Webhook endpoint for deployed site and enable all events. Then add Signing Secret to Heroku app config vars, Gitpod settings and add to env.py


## Credits

### Content
1. The text for ma project comes form [Czas na Herbatę](https://czasnaherbate.net/)
2. The icons comes from [Font Awesome](https://fontawesome.com/)
3. Fonts are taken from [Google Fonts](https://fonts.google.com/)

### Media
1. Bacground image for home page is taken from [pexels.com](https://www.pexels.com)
2. Images for all teas come from [images Google](https://www.google.com/imghp?hl=en&ogbl)
2. [Responisve image](https://ui.dev/amiresponsive)