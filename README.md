## URL = https://cardco.adaptable.app

## How do you implement the tasks in the checklist?

* <u>Create a new Django project</u>: 
I created a new Django project by activiting a virutal environment inside my new directory "cardco". I used the same dependencies as the tutorial and ran the command "django-admin startproject main ." As mentioned in the tutorial I used ["*"] for "ALLOWED_HOSTS" so that adaptable.io can host the application.

* <u>Create an app with the name main on that project:</u>
When creating my new Django project I named it "main" by using the command "django-admin startproject main ."

* <u>Create a URL routing configuration to access the main app:</u>
I used the the same URL routing configuration as the tutorial.

* <u>Create a model on the main app with name Item and these mandatory attributes (name, amount, description):</u>
In models.py, I simply changed the name of the class from Product to Model. Then, I set the attributes "name", "amount", "description" and their respective data types. To set an attribute's data type I used models imported from the django.db library.

* <u>Create a function in views.py that returns an HTML template containing your application name, your name, and your class:</u>
My function has the same name as the tutorial "show_main" with the specified fields.

* <u>Create a routing in urls.py to map the function in views.py to an URL:</u>
Because my function has the same name as the tutorial, I didn't have to change the code to create a routing in urls.py. "path('', show_main, name='show_main')". This command access the show_main function to create the routing.

* <u>Deploy your app to Adaptable so it can be accessed through the internet:</u>
To deploy my app I created a new app on adaptable that connected to my github repository "cardco".

## Create a diagram explaining the flow of client requests to a Django web app and its response. Also in the diagram, explain the connections between urls.py, views.py, models.py, and the HTML file(s).
![Alt text](<diagram.jpeg>)


## What is the purpose of a virtual environment?

The purpose of a virtual environment is to prevent confusions between dependencies of different applications. In our case, if we have two web applications that use different versions of Django, python doesn't know which one to use because they have the same name in the same directory. A virtual environment solves this by creating an isolated environment for a project that only uses one version or the other.

## Can we create a Django web app without a virtual environment?

We can create a Django web app without a virtual environment. However, as I mentioned above, if we have multiple applications that implement different dependencies it can cause bugs.

## What is MVC, MVT, and MVVM? Explain the differences between the three.

MVC stands for Model View Controller. In MVC, the conroller acts as the itermediary between the model and the view, where the model handles data logic and the view handles user interface changes. The controller handles request flow from the end user.

MVT stands for Model View Template. In MVT, the view acts as the intermediary between the model and the view, where the model handles data logic and the template handles the user interface.

MVVM stands for Model View ViewModel. In MVVM, the viewmodel acts as the intermediary between the model and the view, where the model handles data logic and the view handles user ....