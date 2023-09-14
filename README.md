## URL = https://cardco.adaptable.app

# Assignmet 2:

## How do you implement the tasks in the checklist?

* __Create a new Django project:__<br>
I created a new Django project by activiting a virutal environment inside my new directory "cardco". I used the same dependencies as the tutorial and ran the command "django-admin startproject main ." As mentioned in the tutorial I used ["*"] for "ALLOWED_HOSTS" so that adaptable.io can host the application.

* __Create an app with the name main on that project:__<br>
When creating my new Django project I named it "main" by using the command "django-admin startproject main ."

* __Create a URL routing configuration to access the main app:__<br>
I used the the same URL routing configuration as the tutorial.

* __Create a model on the main app with name Item and these mandatory attributes (name, amount, description):__<br>
In models.py, I simply changed the name of the class from Product to Model. Then, I set the attributes "name", "amount", "description" and their respective data types. To set an attribute's data type I used models imported from the django.db library.

* __Create a function in views.py that returns an HTML template containing your application name, your name, and your class:__<br>
My function has the same name as the tutorial "show_main" with the specified fields.

* __Create a routing in urls.py to map the function in views.py to an URL:__<br>
Because my function has the same name as the tutorial, I didn't have to change the code to create a routing in urls.py. "path('', show_main, name='show_main')". This command access the show_main function to create the routing.

* __Deploy your app to Adaptable so it can be accessed through the internet:__<br>
To deploy my app I created a new app on adaptable that connected to my github repository "cardco".

## Create a diagram explaining the flow of client requests to a Django web app and its response. Also in the diagram, explain the connections between urls.py, views.py, models.py, and the HTML file(s).
![Alt text](<diagram.jpeg>)


## What is the purpose of a virtual environment?

The purpose of a virtual environment is to prevent confusions between dependencies of different applications. In our case, if we have two web applications that use different versions of Django, python doesn't know which one to use because they have the same name in the same directory. A virtual environment solves this by creating an isolated environment for a project that only uses one version or the other.

## Can we create a Django web app without a virtual environment?

We can create a Django web app without a virtual environment. However, as I mentioned above, if we have multiple applications that implement different dependencies it can cause bugs.

## What is MVC, MVT, and MVVM? Explain the differences between the three.

MVC stands for Model View Controller. In MVC, the conroller acts as the intermediary between the model and the view, where the model handles data logic and the view handles user interface changes. The controller handles request flow from the end user.

MVT stands for Model View Template. In MVT, the view acts as the intermediary between the model and the view, where the model handles data logic and the template handles the user interface.

MVVM stands for Model View ViewModel. In MVVM, the viewmodel acts as the intermediary between the model and the view, where the model handles data and business logic and the view handles the user interface.

Apart from the difference in the seperation of concerns of these design patterns. The difference between these frameworks is apparent based on the needs of the environments they are used in. MVC is typically used in web development frameworks such as Ruby on Rails or ASP.NET; MVT is found on frameworks like Django; MVVM is found on frameworks like Microsoft WPF.

# Assignment 3

## What is the difference between POST form and GET form in Django?

The POST form is used for submitting data to the server to be processed and possibly stored. It's suitable for forms that involve sensitive data or when the data is too large to include in the URL. The GET form is primarily used for retrieving data from the server. When you submit a form using GET, the form data is appended to the URL as query parameters, which are visible in the address bar of the browser.

## What are the main differences between XML, JSON, and HTML in the context of data delivery?

XML is often used when you need a highly structured, extensible format, and human readability is a requirement.
JSON is preferred for data interchange between systems, especially in web development, due to its simplicity and ease of parsing by JavaScript.
HTML is used for rendering web content to end-users and is not typically used for data exchange but for presenting information in a visually appealing way.

## Why is JSON often used in data exchange between modern web applications?

JSON's simplicity, efficiency, and compatibility with modern web technologies make it a preferred choice for data exchange in web applications, especially in the context of RESTful APIs (Representational State Transfer) and AJAX (Asynchronous JavaScript and XML) requests, where it has become the standard for structuring and transmitting data between the client and server.

## Explain how you implemented the checklist above step-by-step (not just following the tutorial).

* __Create a form input to add a model object to the previous app.__<br>

* __Add 5 views to view the added objects in HTML, XML, JSON, XML by ID, and JSON by ID formats.__<br>

* __Create URL routing for each of the views added in point 2.__<br>

## Access the five URLs in point 2 using Postman, take screenshots of the results in Postman
...