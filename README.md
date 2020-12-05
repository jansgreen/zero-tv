# ZeroTv Store

[Open in Heroku](https://zero-tv.herokuapp.com/catalog/)

Store online "ZeroTv" website written in Django.

we are using the API from themoviedb [themoviedb](https://api.themoviedb.org/).

## Overview

This web project is complemented by several applications that are structured as an online store;.

the main page the user will have the following characteristics without logging in:

* The user can see all movies in the stores.
* Users can select a movie and see detail, can add a movie in the cart.
* The main page has a search and filter area, the user will be able to search for the preferred movie, they will be able to search by genre, by year and by title.
* 
1. Open tab to `http://127.0.0.1:8000` to see the main site, with your new objects.
## Apps of the project
 * Catalog: this show all movies we have in database.
 * Bag: this app allows: see details of a movie and get movie for proccess payment.
 * checkout: all projecto of store need a checkout, this help proccess all payment with stripe.
 * profiles: It is the typical user application that allows you to save information about the user and related to your order.  
## Site Map

1. [Home](https://zero-tv.herokuapp.com/catalog/)
-In the home it shows us a list of movies with two columns maximum where you can navigate and see the various movies that we have in sales, you can use the side arrows to jump from one page to another, it is made up of approximately 385 pages; more than 7700 movies.

2. [Navbar](https://zero-tv.herokuapp.com/catalog/)
    - At the top right you will find the following options:
        - [Login](http://127.0.0.1:8000/accounts/login/?next=/catalog/): Clicking on this will redirect you to the login area of our application.
        - [Register](https://zero-tv.herokuapp.com/accounts/signup/?next=/catalog/): A simple area to register in our application.
        - Search: We have a local movie search engine, if you know the title of the movie, or the ID number or the date the movie was released.

    - Sub Drop Down Menu: It is composed of a series of user menu options.
        - [My_Profile](https://zero-tv.herokuapp.com/accounts/signup/?next=/catalog/): here the user can update his personal address.
        - [add_Movie](https://zero-tv.herokuapp.com/catalog/add/): The user can market his content, he can add a home movie and / or Professional, to sell it through this platform.

        - [Updata Manual ]():only used by the superuser, to update the all list of movie straight from [themoviedb](https://api.themoviedb.org).

        - [Purchase History](https://zero-tv.herokuapp.com/profiles/order_history): displays a list of the user's purchase history, with the purchase details.

        - [Logout] (https://zero-tv.herokuapp.com/accounts/logout/?next=/catalog/): It is the typical link that helps us to leave the platform.

3. [Menu Veltical o Setting Menu ](https://zero-tv.herokuapp.com/accounts/logout/?next=/catalog/):In this menu, display a series of options concerning the user.

    - [Set Password](https://zero-tv.herokuapp.com/accounts/password/change/): We offer you this very common option on all platforms, so that you can have total control of the security of your account, you can change periodically at your pleasure; the password of your account on our platform.

4. Frameworks, Libraries & Programs Used
    - Django 3.0.7 : We use Django to manage and create the content according to the application we want.

    - Bootstrap 4.5.0: was used to assist with the responsiveness and styling of the website.
    - asgiref 3.2.10: We use this standard measure for Python web applications and asynchronous servers to communicate with each other.
    - certifi 2020.6.20 : Certifi This helps us validate the trustworthiness of SSL certificates while verifying the identity of TLS hosts.
    - django-allauth 0.42.0: Integrated set of Django applications addressing authentication, registration, account management as well as 3rd party (social) account authentication.
    - django-countries 6.1.3:  it is a list of countries in United State.
    - django-crispy-forms 1.9.2: we use crispy to render the forms in a clean way.
    - django-heroku 0.3.1 : This is a Django library for Heroku applications that ensures a seamless deployment and development experience.
    - gunicorn 20.0.4: Server is widely compatible with various web frameworks, implemented simply, light on server resource usage, and quite fast.
    - stripe 2.51.0: we use stripe to make the payment process possible.
    - jQuery: came with Bootstrap to make the navbar responsive but was also used for the smooth scroll function in JavaScript.
    - Git: was used for version control by utilizing the Gitpod terminal to commit to Git and Push to GitHub.
    - GitHub: is used to store the projects code after being pushed from Git.
    - Stripe: used with javascripts language, to proccess all payment of the zero-tv.

5. Languages Used
    - HTML5
    - CSS3
    - Python
    - Javascripts

## Unit Test

**Django**

    I did apply a test to each of the applications in this project, from django.test import TestCase, from django.test import TestCase, Client 
from django.urls import reverse and from .models import UserProfile in the file.py I readed the test, running python manage.py test; each of these tests corresponds to each application of this project.

    Also I did copy and paste all file view.py for each app of the project in http://pep8online.com/ to check the code.

**styles.css**
- The file styles.css located in staticfiles/css I loaded in http://jigsaw.w3.org in the option css-validator and clicked in check.
    <p>
    <a href="http://jigsaw.w3.org/css-validator/check/referer">
        <img style="border:0;width:88px;height:31px"
            src="http://jigsaw.w3.org/css-validator/images/vcss-blue"
            alt="¡CSS Válido!" />
        </a>
    </p>

**data.js**
- In https://jshint.com/ I copy my javascripts code and tested all code in the file located staticfiles/js/data.js; my code is jqury code.

## git and github

**Github**
I created a github repository in github
I get a name "zero-tv"
I keep public repository

**Git**
Before start the app, I created the directory zero-tv, in the directory I did my virtual enviroment django-venv and activate (source django-venv/Scripts/activate), and I did admin-start zerotv to create my project in Django; after configure all password and sensitive data, I did a admin-start catalog.
I did git init.
I created my file readme.md
I did git remote add origin https://github.com/jansgreen/zero-tv.git to add the repository remote.
Afther my app is ready I make a git push origin master. to save in github repository.

## Heroku
I created a user on heroku at https://www.heroku.com/, create the application and assign it a name "zero-tv"; Once my application is ready, create the variables
These are the variables in the heroku settings:
Access_key: This is the variable that stores the access key that we use for mongodb connection.

- API_KEY: This variable has the API key of the website that extracts the data from the movies.

- DATABASE_URL:This variable has the link that connects to the postgress database that we use to save the movies

- DEFAULT_FROM_EMAIL:This variable saves the email that is set as the default for the django project.

- DEVELOPMENT: This is a boolean that returns false so django knows how to handle the data when in heroku.

- DJANGO_SECRET_KEY: This variable stores the secret key that django offers us to work with said framenetwork

- EMAIL_HOST_PASS: This variable saves the password of applications that gmail offers us, in gmail configuration, security, two-step verification, register the application that will access the mail, in my case I put django as the tutorial.

- EMAIL_HOST_USER: This variable saves the sender's gmail email in order to validate their account at the time of registration.

- STRIPE_PUBLIC_KEY: This variable saves the public key that the stripe API offers us to access the stripe platform.

- STRIPE_SECRET_KEY: These variables have the secret key that stripe offers us, without this each process will return a 503 that is access denied.

- STRIPE_WEBHOOK_KEY:This variable has the WEBHOOK key, this allows us to access to see all the events that the user made in our application at stripe.com

# Buildpacks heroku / python (with this I specify to heroku that the programming language I will use is python)
After having configured the variables, I created my procfile (Procfile) file in my local application with the following web configuration: gunicorn run: app, thus telling heroku to run the gunicorn server for this application. and then download Heroku CLI. as I had already done git init in the folder of my application and within it I did the following steps to deploy in Heroku: $ heroku login $ heroku git: remote -an emergency level git add. git commit -m "implement in heroku" git push heroku master.

## Django apps

* This project has 4 applications that make this project possible in django.

**catalog**
* this application displays a list of 9354 movies that you can taste by clicking on the side arrows; It also allows us to add the movies that the user wants to our database; In the same way, this application allows the user to edit and / or delete the movie that he has created in the application.

**bag**
* After having selected the movie of your interest, and having registered correctly, the user can see the details of the selected movie, Delete or Edit the movie, also the user can select the amount of movie that can be saved in his bag; thanks to this bag application, which also shows us a list of all the movies that you have saved in your bag.

- mymovies.py, Following the instructions of the Boutique Ado tutorial, we create this file which helps us to save in the section and process the prices and quantity of the items.

- urls:


**checkout**
* As its name says, this application helps us to process the items that we have stored in our bag, this is possible to the stripe API, when processing the payment it displays a floating window of stripe, to confirm the payment that the user plows to the time to pay for the items.

**profiles**
* This application will help us to save the important information of the user such as the address among other data, this application is associated with the user library that django brings, we link it with a related field in the models file of the same application.

## Database













    



