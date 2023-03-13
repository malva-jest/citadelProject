
# Citadel Password Manager

Similar in design to a typical blog-style application, this app allows users to store and manage their passwords, but provides a custom view for each user, concealing their sensitive data. 

## Purpose of the Project

I created this app to gain hands-on experience with the Django framework and deepen my understanding of backend web development. The project allowed me to explore and implement server-side programming concepts and best practices, including user management, login authentication, and CRUD operations in a Django application. Through building this project, I was able to apply my knowledge of database design. This app was also a great opportunity to explore Django's admin interface, for easy management and administration of data in the project. 

## Key Features

- User Management: the user can sign up and create an account with a unique username and password. They can also modify their profile information, such as their email, name, password, and profile picture.

- Login Authentication: the app requires the user to log in to access a user-specific page from which they can manage their passwords.

- User-specific View: the user-specific page allows one to view, add, edit, and delete passwords. This feature ensures that sensitive data is secure and not visible to other users.

- Profile Picture: users have the option to upload a profile picture to their profile. This feature enhances user experience by allowing for a more personalised account.

- Password Reset: the app allows users to reset their passwords if forgetten. The user receives an email notification with instructions on how to reset the password.

- Django-crispy-forms: this simplified the process of styling and formatting Django forms by providing a simple template pack that helped to customise the layout and style of forms in a consistent manner across the entire project.

## Challenges

In adapting the standard blog-style app, one of the main challenges I faced was creating a user-specific view. This feature is critical to ensure that a user's data is secure and not visible to other users. Naturally, an app that exposes sensitive data to users not authorised to view that information defeats the purpose of a password manager.

## Deployment and Next Steps

I haven't deployed the app yet, but I'm considering deploying it to a cloud-based platform such as Heroku or AWS.

To enhance the security of the passwords stored in the app, I'd like to research and implement industry-standard hashing algorithms such as bcrypt or Argon2. These algorithms are designed to be more resistant to brute-force attacks and rainbow table attacks, which can compromise the security of weaker hash functions.

# Getting Started

To get started with the app, you'll need to have Python 3 and Django installed on your machine. You can install Django by running the following command:

`pip install Django`

Next, navigate to the project directory and create a Django project by running the following command:

`django-admin startproject myproject`

This will create a new Django project with the name myproject. Navigate to the project directory by running:

`cd myproject`

Now, create a new Django app by running:

`python manage.py startapp myapp`

This will create a new Django app with the name myapp. Next, navigate to the myapp directory by running:

`cd myapp`

Now you can run the development server by running:

`python manage.py runserver`

The app should now be running on http://localhost:8000. 

To create a new superuser account that will allow you to access the admin interface, run:

`python manage.py createsuperuser`

You can access the admin interface by navigating to: 

`http://localhost:8000/admin` 

You should now have everything you need to get started with the Django Password Manager app.