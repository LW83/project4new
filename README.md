https://stackoverflow.com/questions/44651760/django-db-migrations-exceptions-inconsistentmigrationhistory - Correct to allow migration of User

Bug - wasn't picking up login template - needed to put in registration folder https://stackoverflow.com/questions/6646400/does-django-ship-with-the-authentication-templates-for-use-with-the-django-contr

Getting object by id: https://stackoverflow.com/questions/73338018/how-to-get-an-object-by-id-in-django

Int Pk URL structure: https://github.com/fabricius1/DjangoFilmsCRUD/blob/master/films/urls.py
Adding extra fields in registration form: https://stackoverflow.com/questions/45708119/how-to-add-extra-fields-to-django-registration-form

Creating filter for user and certain dog profiles: https://stackoverflow.com/questions/769843/how-do-i-use-and-in-a-django-filter

For dates in create profile form TRY: date_added = forms.DateField(initial=today, widget=forms.SelectDateWidget(years=YEARS))
Add calendar to select dates: https://django-bootstrap-datepicker-plus.readthedocs.io/en/latest/Walkthrough.html

Delete button: https://stackoverflow.com/questions/60616526/how-to-add-delete-button-in-each-row-of-my-table
Delete button: https://stackoverflow.com/questions/55705666/django-tables2-with-edit-and-delete-buttons-how-to-do-it-properly

Linking the edit button to the icon: https://docs.djangoproject.com/en/4.1/intro/tutorial04/

 <!-- {% empty %}
        <div>You have no profiles in this list.</div> -->

Filtering multiple criteria: https://stackoverflow.com/questions/769843/how-do-i-use-and-in-a-django-filter

Displaying messages: https://docs.djangoproject.com/en/4.1/ref/contrib/messages/#:~:text=The%20messages%20framework%20allows%20you,%2C%20warning%20%2C%20or%20error%20).

Phone numbers: https://django-phonenumber-field.readthedocs.io/en/latest/reference.html#model-field
https://stackoverflow.com/questions/19130942/whats-the-best-way-to-store-a-phone-number-in-django-models
Default Phone Number structure: https://www.twilio.com/docs/glossary/what-e164

Amending Admin to bring in additional fields: https://stackoverflow.com/questions/48011275/custom-user-model-fields-abstractuser-not-showing-in-django-admin

Admin issue: https://stackoverflow.com/questions/70274885/insert-or-update-on-table-django-admin-log-violates-foreign-key-constraint

To create accept and reject booking functions: https://www.w3schools.com/django/django_update_record.php


POSSIBLE: 
Password reset/change; https://stackoverflow.com/questions/6646400/does-django-ship-with-the-authentication-templates-for-use-with-the-django-contr
Password reset: https://docs.djangoproject.com/en/4.1/topics/auth/default/
Adding Filter to table: https://codepen.io/smashingmag/pen/LYWBgXy


# Connector 
***
## Overview 

Welcome to Connector, a tool for connecting Pounds and Rescues to ensure dogs in the Pound can be reassigned to Rescues based on urgency and Rescue availability. This is a purely fictional sysetm created for purely for demonstrating Python & Django skills learned as part of the Code Institute's Diploma in Full Stack Software Development. 

![Responsiveness Demo](./docs/)

## Live Site

[Connector](https://project4new.herokuapp.com/)

## Repository 

[GitHub Repository](https://github.com/LW83/project4new)
***
## Table of Contents:
* [**Connector**](#connector)
  * [**Overview**](#overview)
  * [**Concept and Planning**](#concept-and-planning)
    * [**UX**](#ux)
    * [**Logic**](#logic)
  * [**Existing Features**](#existing-features)
    * [**Landing Page**](#landing-page)
    * [**User Inputs**](#user-inputs)
    * [**Welcome Page**](#welcome-page)
  * [**Feature Enhancements**](#feature-enhancements)
  * [**Testing**](#testing)
    * [**User Story Testing**](#user-story-testing)
    * [**Features Testing**](#features-testing)
    * [**Browser Testing**](#browser-testing)
    * [**Code Validation Testing**](#code-validation-testing)
    * [**Fixed Bugs**](#fixed-bugs)
    * [**Unfixed Bugs**](#unfixed-bugs)
  * [**Deployment**](#deployment)
  * [**Languages & Libraries**](#languages-&-libraries)
    * [**Languages Used**](#languages-used)
    * [**Python Libraries & Modules Utilised**](#python-libraries--modules-utilised)
  * [**Credits**](#credits)
    * [**Media & Content**](#media-&-content)
    * [**Tools and Online Resources Utilised**](#tools-and-online-resources-utilised)
    * [**Code Utilisation**](#code-utilisation)
    * [**People**](#people)
***
## Concept and Planning 

### UX

- __Target Audience__

   - 

- __User Stories__

   - As a user, I want 
   - As a user, I want to be able to 

- __Site Aims__
 
  - The site aims to meet the above user requirements through the following: 
    -  Providing 

### Logic

- I used [Lucidchart](https://www.lucidchart.com) to set out the main logic of the site: 

![Lucidchart Diagram](./docs/)

***
## Existing Features 

### Landing Page

__Favicon__

  -  A  has been added as a favicon for the page. 
  
  ![Favicon](./docs/)

__Log In__

  - The 

### User Inputs

  - I

### Welcome Page

  - 

***
## Feature Enhancements

 - There are no current features that I believe are oustanding on the site however I would like to revisit the code in future to see if there is further opportunities for refactoring. 
       
***
## Testing 

### User Story Testing

 - All user stories identified have been tested against the final design with the outcome of this testing set out below. 

![User Story Testing](./docs/)

### Features Testing
 - All design features have been manually tested with the outcome of this testing set out below. 
 - Screenshots have also been included in the Features section above to show the validation output for the various steps completed by the user. 
 - Testing was completed in my local terminal and also in Heroku post deployment. 

![Features Testing](./docs/)

### Browser Testing
  - The site was developed and tested using Google's Chrome browser. 
  - The site has also been tested on Safari and functions as intended. 

![Browser Testing](./docs/)
 
### Code Validation Testing 

  - The site code has been passed through the following online validation tools: 

  ![Code Validations](./docs/)

__HTML Validation__
  
  - There are no errors for the site when passed through the W3C validator. 

  ![W3C validator](./docs/)

__CSS Validation__

  - There are no errors for the site when passed through the W3C validator.

  ![CSS validator](./docs/)

__Python Validation__

  - No errors were found in any of the three python files when passing through the Pep8 online validator. 
   
  Run File
  ![Run File](./docs/)
  Questions File 
  ![Questions File](./docs/)
  Logo File
  ![Logo File](./docs/)

### Fixed Bugs   
  - The following key bugs arose and were fixed during the development of the site: 

    1. XYZ: 
          - Issue: 

          - Solution: 
          - Resource:  


### Unfixed Bugs
- The bugs that remain unfixed are: 

   - 

   -  

***
## Deployment

- Prior to deployment in Heroku, to ensure the dependencies used in Gitpod were installed in Heroku, I ran the pip3 freeze > requirements.txt command in Gitpod. 

- As a python based project, the site was deployed to Heroku following the below deployment steps: 
   - Log in to Heroku (or create an account if required).
   - Click 'Create a new app'.
   - Enter a name for the app (must be unique). I selected sorting-hat-22. 
   - Select your region. For me, this is Europe being based in Ireland. 
   - Select "Create app".
   - In the new page for the app, select the Settings tab from the menu at the top of the main screen. 
   - In the Settings page, go to the 'Config Vars' section and select "Reveal Config Vars".
   - In the 'Key' field enter a name of 'CREDS' and copy and paste the contents of the creds.json file from Gipod into the 'Value' field in order to connect Heroku to the API with Google sheets. 
   - Select 'Add'; in this line enter 'PORT' in the 'Key' field and a 'Value' of 8000 to ensure compatability between teh Code Institute template being used and vaious Python libraries. 
   - Then scroll to the 'Buildpacks' section of teh Settings page and select 'Add Buildpack'.
   - Select 'Python' and save the changes. 
   - Then add 'node.js' as a further buildpack. 
   - Ensure Python is above Node.js in the buildpack order or if not, reorder.
   - Now select the 'Deplpy' section from the menu at the top of the page. 
   - Select GitHub as the deployment method and 'Connect to GitHub'.
   - Find the right repository (here sorting_hat) via the Search functionality and then select 'Connect'.
   - Scroll down to the new 'Manual Deploy' section and select 'Deploy Branch'
   - Wait until the deployment is finished running and select "View".

The live link can be found here: [Connector](https://project4new.herokuapp.com/) 

***
## Languages & Libraries

### Languages Used
  - Python
  - HTML5
  - CSS3

### Python Libraries & Modules Utilised
  - 

***
## Credits  

### Media & Content
 - 

### Tools & Online Resources Utilised
 - The following tools and resources have been utilised in the creation of this project: 
     - Code Institute & I Think Therefore I Blog Demonstration: For guidance and inspiration for this site. 
     - GitHub & Gitpod: For development of the site. 
     - [Stackoverflow](): For general guidance and research - specific examples used in final build set out below. 
     - [Slack](https://slack.com/intl/en-ie/): For general guidance and research on project considerations. 
     - [W3C HTML Validator](https://validator.w3.org/)
     - [W3C CSS Validator](https://jigsaw.w3.org/css-validator/)
     - [Pep8online Validator](http://pep8online.com/)
     - [Heroku](https://id.heroku.com/login)
     - [Lucidchart](https://www.lucidchart.com): To create a flow chart of the game logic
     - [Google](www.google.com): For spreadsheet and API to connect to Python

     Specific Online Resources utilised as references: 
      - https://stackoverflow.com/questions/23623288/print-full-ascii-art - to insert ASCII images into Python
      - https://www.codespeedy.com/check-if-user-input-is-a-string-or-number-in-python/ - to check name input for digits instead of letters
      - https://pypi.org/project/colorama/ - to add color to the ASCII images

### Code Utilisation
 - The following elements of code have specifically been inspired from the following sources: 
    - Code Institute for the deployment terminal 
    - [ABC](https://github.com/) for the folllowing: 

### People
 - In addition a big thank you to the following people for their assistance or inspiration in this project:
     - Kasia Bogucka: Our cohort facilitator for keeping us all on track and answering all and any of the many questions!
     - My cohort: For our weekly checkins and tips
     - The genius Ger in Tutor Support for helping me resolve an issue where the information from the booking model was submitting but not displaying in the booking model in Admin. 

