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
    



