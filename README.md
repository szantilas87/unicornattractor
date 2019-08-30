<h1>Unicorn Attractor</h1>
The project was created to attract customers who want their bugs to be fixed and develop new features for them. Users can add a new bug for free, but to add a new feature, they have to become a premium user. Premium membership costs 50$, and the payment is made by credit card, thanks to Stripe services. After adding a new bug or feature, users can track its progress between three phasis: "To do", "In progress" and "Done". Users can add comments and likes to suggest the administration what jobs they should do first. In the About section, users can see graphs and statistics. They can learn proportions between added bugs and features, how many jobs have a particular status, and how many of them were added on the specific date.  Users can send a message to the administration from the form on the main page and sign up to a newsletter. A user who whats to get access to all the functionalities has to create an account and sign in. A registered user has access to his profile where he can change basic data and update profile picture. Users passwords are encrypted and stored in a secured database. 

   
<h2>UX</h2>
The application has a simple and clean layout to provide easy navigation between the main functionalities. Fist section of the main page contains links to the list of existing bugs and a link to a page where users can add a new bug. In the second section, we can find positive opinions from our customers. Below is a section where users can find links to the list of existing features and a link to add a new feature only available for the user who has the premium status. At the bottom of the page, we have a contact form, links to the social media, and a short description of the page with an option to sign up for the newsletter.
<ul>User stories:
<li>A user who wants to use all the functionalities of the application needs to register himself by clicking "Register" and fill the required fields.</li>
<li>A user who comes back after some time has to log in by providing the username and password used during the registration process.</li> 
<li>A user can add a new bug by clicking on the "Add a new bug" button, where he can find a form to provide all necessary information.</li> 
<li>A user who wants to see the list of the existing bugs needs to click "Bugs" tab in the navbar or the button "Bugs", next to "Add a new bug" button.</li>
<li>A user can add a new feature by clicking on the "Add a new feature" button, he will be transferred to a payment form where he can add a credit card details. After the payment is confirmed the administrator of the page can assign the premium status in the admin panel and adding new features will be available for that particular user.</li>
<li>A user who wants to see the list of the existing features needs to click "Features" tab in the navbar or the button "Features", next to "Add a new feature" button.</li>
<li>A user who wants to see all the statistics and graphs can click the "About" tab.</li>
<li>A user who wants send a message can do it by filling up a form at the bottom of the main page.</li>
</ul><br>
Pre-implementation mockups:<br>
https://www.docdroid.net/7AJFH5x/unicorn.pdf<br>

<h2>Features</h2>

The project was built to provide usability and high performance. The user interface is clear and simple not to distract the user from the main functionalities. Attached images help identify the website visually and direct users to right sections of the page.  The logo in the left top corner is visible all the time to improve the visual identification. Registration and login requirements help protect user's identity and privacy. The search feature allows a user to find keywords interesting for him. A user can sort lists of bugs and features by title alphabetically and by date. Adding a new bug/feature is straightforward and requires only the title and the description. All the information included in the "About" page is easy to find and interpret. Contact form lets keep in touch with the administrators of the website and leave valuable feedback. The cards with bugs/features include the name of the author, title, description, status, number of views and likes, and a section to leave a comment.

<h2>Technologies Used</h2>

Technologies Used:
- HTML
- JavaScript and JQuery
- SASS
- Bootstrap
- Python and Django



<h2>Testing</h2>
The application was tested on many devices and browsers. The HTML and CSS structures were validated with C3W Markup Validator and C3W CSS Validator. Unittest, Jasmine and Jasmine-Jquery were used for testing.

1. Using the main site.<br>
a) The main page displays all basic sections and buttons. Images, texts and styles are visible and loading properly.<br>
b) All link to the subpages were tested and working correctly - leading to the subpages.<br>
c) The front page was tested on a variety of devices and resolutions to make sure that the content is adjusting to the different screen sizes

2. Registering / Login<br>
a) A new user can create a new account by adding username and password to the database.<br>
b) Passwords are encrypted before sending to the database.<br>
c) A user can log in to the website using data information provided during the registration process.<br>
d) A user can update the username, email and profile picture in the "Profile" section, where he can also request a password reset.<br>


3. Browsing through the bugs/features.<br>
a) All bugs/features are displayed correctly either in specific subpages or in search results.<br>
b) All information provided by the user is visible on the bug/feature card.<br>
c) Bugs/features are grouped by eight on a single page using pagination.<br>
d) Edit function allows adding new information and modifies the existing one, only if the user is the author of the bug/feature.<br>
e) Delete functionality removes the bug/feature from the page and the database only if the user is the author of the bug/feature.<br>
f) The total number of bugs/features is displayed properly and change after adding or removing a bug/feature.<br>
g) Comments added by users are visible at the bottom of the bug/feature card.<br>
h) Total views and likes are calculated properly.<br>

4. About page<br>
a)  The page is displayed properly with all relevant pieces of information.<br>
b) All the charts are working correctly, displaying necessary information and updating after changes in the database.

5) Send message.<br>
a) The message form is working correctly.<br>
b) All required fields have to be filled before sending the message.<br>
c) A new message is received instantly on the provided email address.<br>

Jasmine and Jquery-jasmine were used for testing index.html.<br>
When you run the index.html file, visit:<br>
http://URL.com/jasmine-tests/spec-runner.html<br>
where can be http://localhost:8081/jasmine-tests/spec-runner.html<br>
<br>
All the tests conducted by Jasmine check:
- All the buttons on the main page lead to the subpages.
- The navbar contains the necessary class.
- The collapsing menu is activated by click hamburger button.
- The main page has sections with the right ids.
- The footer has all the necessary links to other subpages and social media.

Some tests were done for the backend using the unittest library in Python 3, and the results can be found in the tests folders.


<h2>Deployment</h2> 

The site was deployed on Heroku.com and can found under this address: https://unicornattractor24.herokuapp.com/. The copy of the final version and previous development version can be found on GitHub: https://github.com/szantilas87/unicornattractor A list of all necessary dependencies is in the requirements.txt file.<br> To run the project, some environment variables are needed:<br> 
SECRET_KEY - any string<br> 

For sending messages:<br>
EMAIL_HOST - SMTP server you want to use <br> 
EMAIL_PORT - port used by EMAIL_HOST<br> 
EMAIL_USE_TLS - True or False<br> 
EMAIL_HOST_USER - the email address you want to use<br> 
EMAIL_HOST_PASSWORD - password for the email address<br> 

Stripe payments:<br>
STRIPE_PUBLIC_KEY = public key provided by Stripe<br> 
STRIPE_PRIVATE_KEY = private key provided by Stripe<br> 

Storing static and media files in AWS S3:<br>
AWS_STORAGE_BUCKET_NAME = name of the bucket<br> 
AWS_S3_REGION_NAME = name of the server<br> 
AWS_ACCESS_KEY_ID = access key<br> 
AWS_SECRET_ACCESS_KEY = private access key<br> 

<h4>Content</h4>
Corey Schafer <br>
-https://www.youtube.com/watch?v=UmljXZIypDc&list=PL-osiE80TeTtoQCKZ03TU5fNfx2UY6U4p<br>
- https://www.youtube.com/watch?v=UO98lJQ3QGI&list=PL-osiE80TeTvipOqomVEeZ1HRrcEvtZB_<br><br>

Traversy Media<br>
-https://www.udemy.com/python-django-dev-to-deployment/

<h4>Media</h4>

- Google images







