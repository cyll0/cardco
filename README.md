> URL = https://cardco.adaptable.app

# Assignment 2

### How do you implement the tasks in the checklist?

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

### Create a diagram explaining the flow of client requests to a Django web app and its response. Also in the diagram, explain the connections between urls.py, views.py, models.py, and the HTML file(s).
![Alt text](<diagram.jpeg>)


### What is the purpose of a virtual environment?

The purpose of a virtual environment is to prevent confusions between dependencies of different applications. In our case, if we have two web applications that use different versions of Django, python doesn't know which one to use because they have the same name in the same directory. A virtual environment solves this by creating an isolated environment for a project that only uses one version or the other.

### Can we create a Django web app without a virtual environment?

We can create a Django web app without a virtual environment. However, as I mentioned above, if we have multiple applications that implement different dependencies it can cause bugs.

### What is MVC, MVT, and MVVM? Explain the differences between the three.

MVC stands for Model View Controller. In MVC, the conroller acts as the intermediary between the model and the view, where the model handles data logic and the view handles user interface changes. The controller handles request flow from the end user.

MVT stands for Model View Template. In MVT, the view acts as the intermediary between the model and the view, where the model handles data logic and the template handles the user interface.

MVVM stands for Model View ViewModel. In MVVM, the viewmodel acts as the intermediary between the model and the view, where the model handles data and business logic and the view handles the user interface.

Apart from the difference in the seperation of concerns of these design patterns. The difference between these frameworks is apparent based on the needs of the environments they are used in. MVC is typically used in web development frameworks such as Ruby on Rails or ASP.NET; MVT is found on frameworks like Django; MVVM is found on frameworks like Microsoft WPF.

# Assignment 3

### What is the difference between POST form and GET form in Django?

The POST form is used for submitting data to the server to be processed and possibly stored. It's suitable for forms that involve sensitive data or when the data is too large to include in the URL. The GET form is primarily used for retrieving data from the server. When you submit a form using GET, the form data is appended to the URL as query parameters, which are visible in the address bar of the browser.

### What are the main differences between XML, JSON, and HTML in the context of data delivery?

XML is often used when you need a highly structured, extensible format, and human readability is a requirement.
JSON is preferred for data interchange between systems, especially in web development, due to its simplicity and ease of parsing by JavaScript.
HTML is used for rendering web content to end-users and is not typically used for data exchange but for presenting information in a visually appealing way.

### Why is JSON often used in data exchange between modern web applications?

JSON's simplicity, efficiency, and compatibility with modern web technologies make it a preferred choice for data exchange in web applications, especially in the context of RESTful APIs (Representational State Transfer) and AJAX (Asynchronous JavaScript and XML) requests, where it has become the standard for structuring and transmitting data between the client and server.

### Explain how you implemented the checklist above step-by-step (not just following the tutorial).

* __Create a form input to add a model object to the previous app.__<br>
I created a base template in a file called base.html to act as the structure of the web view's structure. Then, I included this file in the TEMPLATES section of the settings.py folder. After that, I adjusted the main.html file to extend base.html. To create the form input, I made a new file called forms.py where the class ItemForm has four fields: name, amount, description, and date added (implict). In the same file, I added a function "create_item", which creates an item with the form input. Next, I added this function to the urls.py file. A webpage with an input form was then created to add items to the application's database. In main.html, I created a table to represent the items in the database.

* __Add 5 views to view the added objects in HTML, XML, JSON, XML by ID, and JSON by ID formats.__<br>
To view the added objects in HTML, I created a table that shows the items in the database. The four other views are quite similar, the only difference is their serialized form and content types.

* __Create URL routing for each of the views added in point 2.__<br>
To craete URL routing for each of the views added in point two, I added a new path in main/urls.py specifying their route, function, and name.

### Access the five URLs in point 2 using Postman, take screenshots of the results in Postman
* __HMTL:__

![Alt text](<Screenshot 2023-09-15 at 11.11.37.png>)

* __XML:__

![Alt text](<Screenshot 2023-09-15 at 11.12.05.png>)

* __JSON:__

![Alt text](<Screenshot 2023-09-15 at 11.12.17.png>)

* __XML by ID:__

![Alt text](<Screenshot 2023-09-15 at 11.13.02.png>)

* __JSON by ID:__

![Alt text](<Screenshot 2023-09-15 at 11.13.17.png>)

# Assignment 4

### What is UserCreationForm in Django? Explain its advantages and disadvantages.
In Django, UserCreationForm is a built-in form class provided by the Django authentication system. It's useful when you need to implement user registration functionality, allowing users to sign up for your website. The advantages to this form are that it's easy to use, secure, customizable, and easy to manage user accounts. However, the disadvantages of this form are that it can only collect a username, password, and email, and the UI customization is limited to a basic appearance.

### What is the difference between authentication and authorization in Django application? Why are both important?
Authentication is the process of verifying the identity of a user, for example, by means of a username and password. Authorization is the process of determining what actions or resources a user is allowed to access or perform within your application after they have been authenticated. Both of these are important because they help protect an application from unauthorized access and misuse, user data and information from unauthorized access. Applications need to adhere to security and privacy regulations, which can be acheived through authentication and authorization.

### What are cookies in website? How does Django use cookies to manage user session data?
Cookies are small pieces of data that a web server sends to a user's web browser, which then stores the data locally on the user's device. Django uses cookies to manage user session data by enabling developers to create web applications where users can log in, interact with personalized content, and maintain their session state even when navigating between different pages or making multiple HTTP requests.

### Are cookies secure to use? Is there potential risk to be aware of?
Cookies are secure to use when it comes to session management, user prefereces, and shopping carts. However, there is potential risk to be aware of in terms of data leakage, session hijacking, Cross-Site Request Forgery, cookie theft, and cookie security settings.

### Explain how you implemented the checklist above step-by-step (not just following the tutorial).
Implement registration, login, and logout functions to allow users to access the previous application:
To implement registration, I created a registration function in views.py. Then, I created a new HTML file called register.html that loads the registration page. Finally, I added its path to urls.py. For the login and logout functions, I created one login function and another logout function. Because the logout function doesn't need its own webpage, I only had to create a new file login.html that loads the login page. Lastly, I added its path to urls.py. To ensure that users without an account are not able to use the application, I simply imported login_required from the Django library, and applied it to the show_main function in views.py.

Create two user accounts with three dummy data entries for each account using the model previously created in the application:
To create two user accounts with three dummy data entries, I created two new accounts "clay" and "clay1" with the same passwords, and add three dummy data entries.

Connect Item model with User:
To connect the Item model with User, I imported User from the Django library, and I had to modify the Item class, the create item function, and the show_main function. I created an attribute "user" to create a relation between the user and the item with a foreign key. In the create item function, I had to prevent the application from saving items immediately in the database to save the item.user into the element. This was done with "form.save(commit=False)" and "item.user = request.user". Lastly, in the show_main function, I had to set it up so that the items shown in the table, are the users items and not all of the items. This was done with "items = Item.objects.filter(user=request.user), which filters the user's iterms, and "'name': request.user.username", which displays the user's name.

Display the information of the logged-in user, such as their username, and applying cookies, such as last login, on the main application page:

# Assignment 5

### Explain the purpose of some CSS element selector and when to use it.
CSS (Cascading Style Sheets) element selectors are used to target and apply styles to specific HTML elements on a web page. Element selectors are one of the fundamental building blocks of CSS and are crucial for controlling the visual presentation of web content. For example, a type selector targets HTML elements based on their element type. We use type selectors when we want to apply a style to all instances of a specific HTML element throughout your webpage.

### Explain some of the HTML5 tags that you know.
Some HTML5 tags I know are the 'header' tag that is used for introductory content like site logos and navigation menus. The 'nav' tag is used for links to different parts of the website. The 'main' tag signifies the primary content of the document.

### What are the differences between margin and padding?
Margins are used to control the space outside an element, creating space between the element and its neighboring elements. Margins affect the distance between elements on the page. Padding is used to control the space inside an element, creating space between the element's content and its inner boundaries. Padding affects the content's position within the element.

### What are the differences between the CSS framework Tailwind and Bootstrap?
 Tailwind CSS and Bootstrap cater to different design philosophies and developer preferences. Tailwind CSS offers more flexibility and encourages custom designs, while Bootstrap provides a pre-designed component library for rapid development.

 ### When should we use Bootstrap rather than Tailwind, and vice versa?
 The choice between Bootstrap and Tailwind CSS should align with your project's goals and your team's skillset. You can also consider hybrid approaches, where you use Tailwind CSS for certain parts of your project that require customization and Bootstrap for others that benefit from its pre-designed components.

### Explain how you implemented the checklist above step-by-step (not just following the tutorial).
In summary, the assingments instructions were to customize the five different pages we have created: register, login, inventory, add item, and edit item. To do this I applied the dark theme to each page and centered the content. It's a simple design, but I like how it looks.