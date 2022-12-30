# Connector 
***
## Overview 

Welcome to Connector, a tool for connecting Pounds and Rescues to ensure dogs in the Pound can be booked by Rescues based on urgency and Rescue availability. The site allows both Pound and Rescue users to create a user type specific account to either upload and manage dog profiles (Pound Users) or book and manage bookings (Rescue Users).

This is a purely fictional sysetm created for purely for demonstrating Python & Django skills learned as part of the Code Institute's Diploma in Full Stack Software Development. 

![Responsiveness Demo](./static/images/readme/mockup.png)

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
    * [**Design**](#design)
    * [**Wireframes**](#wireframes)
    * [**Database Planning**](#database-planning)
  * [**Existing Features**](#existing-features)
    * [**Landing Page**](#landing-page)
    * [**User Dashboards**](#user-dashboards)
    * [**Views**](#views)
  * [**Feature Enhancements**](#feature-enhancements)
  * [**Testing**](#testing)
    * [**User Story Testing**](#user-story-testing)
    * [**Features Testing**](#features-testing)
    * [**Permissions Testing**](#permissions-testing)
    * [**Browser Testing**](#browser-testing)
    * [**Code Validation Testing**](#code-validation-testing)
    * [**Lighthouse Performance Testing**](#lighthouse-performance-testing)
    * [**Accessibility Testing**](#accessibility-testing)
    * [**Fixed Bugs**](#fixed-bugs)
    * [**Unfixed Bugs**](#unfixed-bugs)
  * [**Deployment**](#deployment)
    * [**Workspace SetUp**](#workspace-setup)
    * [**Deployment**](#deployment-1)
  * [**Languages, Technologies & Libraries**](#languages-technologies--libraries)
    * [**Languages Used**](#languages-used)
    * [**Technologies Utilised**](#technologies-utilised)
  * [**Credits**](#credits)
    * [**Resources**](#resources)
    * [**Code Utilisation**](#code-utilisation)
    * [**People**](#people)

***
## Concept and Planning 

### UX

- __Target Audience__

   - The target audience for this application are local county council Dog Pounds and animal rescue shelters. This site is not intended for use by the general public.

- __User Stories__

   - As a Pound user, I want to be able to create a Connector account for my Pound so that I can upload dogs in my pound that need placement in a rescue.
   - As a Pound user, I want to create my own log in details so that I can keep my account information secure. 
   - As a Pound user, I want to be able to edit my user details including my password so that I can keep this information accurate and secure. 
   - As a Pound user, I want to be able to add details about that dog including breed, age, gender, neuter and microchip status as well as key dates and urgency of placement so that Rescue users can clearly see what type of dog they are booking.  
   - As a Pound user, I want to be able to view a list of all of my currently available dogs so that I know what profiles are active on the site. 
   - As a Pound user, I want to be able to edit details for dogs uploaded so that profiles accurately reflect the status of all dogs. 
   - As a Pound user, I want to be able to delete a profile if necessary so that my profiles accurately reflect dogs in my care. 
   - As a Pound user, I want to be able to see details of proposed bookings by Rescues including contact information and proposed collection date so that I can determine suitability. 
   - As a Pound user, I want to be able to accept or reject these bookings so that I can confirm the collection with the Rescue or make the dog available again. 
   - As a Pound user, I want to be able to view a list of all accepted bookings so that I can see which dogs are pending collection. 
   - As a Pound user, I want to be able to confirm when a dog has been transferred to Rescue so that I can keep the status of dogs current and accurate. 
   - As a Pound user, I want to be able to see a history of uploaded dogs and their final status so that I can use this data for any reporting requirements I have. 
   - As a Pound user, I want to be able to log out of my account so that I can keep my information secure. 

   - As a Rescue user, I want to be able to create a Connector account for my Rescue so that I can book dogs that are in the Pound that my Rescue has space to take in.
   - As a Rescue user, I want to create my own log in details so that I can keep my account information secure. 
   - As a Rescue user, I want to be able to edit my user details including my password so that I can keep this information accurate and secure. 
   - As a Rescue user, I want to be able to view details about a dog including breed, age, gender, neuter and microchip status as well as key dates and urgency of placement so that I can determine which dogs are suitable for my Rescue to take in, when they are available and which dogs are most in need of urgent placement.  
   - As a Rescue user, I want to be able to 'book' a dog to take into my Rescue from the Pound.
   - As a Rescue user, I want to be able to edit details of my bookings if the collection infomation is no longer accurate so that the Pound user has the latest information. 
   - As a Rescue user, I want to be able to delete a booking if necessary so that the dog becomes available for another Rescue to book if I can no longer take them.  
   - As a Rescue user, I want to be able to view a list of all currently proposed bookings so that I can see what is pending acceptance by a Pound user. 
   - As a Rescue user, I want to be able to view a list of all accepted bookings so that I can see which dogs are pending my collection. 
   - As a Rescue user, I want to be able to confirm when a dog has been transferred to Rescue so that I can keep the status of bookings current and accurate. 
   - As a Rescue user, I want to be able to see a history of rescued dogs so that I can use this data for any reporting requirements I have. 
   - As a Rescue user, I want to be able to log out of my account so that I can keep my information secure. 

   - As a user, I can navigate the site easily and intuitively.

   - As an Admin user, I want to be able to view all Users of Connector.
   - As an Admin user, I want to be able to manage the permissions of Users of Connector.
   - As an Admin user, I want to be able to edit the details for Users if required. 
   - As an Admin user, I want to be able to delete users as required. 
   - As an Admin user, I want to be able to edit and delete profiles created by users if required. 
   - As an Admin user, I want to be able to edit and delete bookings created by users if required. 


- __Site Aims__
 
  - The site aims to meet the above user requirements through the following: 
    - Providing a requirement to log in or register for an account (Pound or Rescue) upon reaching the landing homepage.
    - Upon sign in, the user can easily navigate to the element of the site they wish to use based on their user specific dashboard.
    - Pound users can easily create a profile for a dog in their care from their dashboard which is then added to the main dashboard and visible to other users. 
    - Users can easily view all dogs currently uploaded by Pounds, their details, location and urgency by viewing all dogs from their dashboard. For Rescue Users, this dashboard also allows the user to book a specific dog that they may have space to take in. If a proposed booking is made, this temporarily removes the profile from the main dashboard until the Pound user has either accepted or rejected the booking in order to avoid multiple booking requests. 
    - Pound users can edit and delete profiles of dogs from within their Current dogs and Previous dogs dashbaords to maintain their details and status. 
    - Pound users can easily view all proposed bookings for their dogs that they have received from Rescue users by accessed their Proposed bookings from their dashboard. From this dashboad they can accept or reject bookings. Accepted bookings move directly to their Bookings dashboard. Reject bookings move back to the Current dogs dashboard with an Available status again. 
    - From their dashboard, Rescue users can view, edit and delete their bookings if they are no longer in a position to take a dog as proposed. 
    - From their dashboard, users can see their collected or previous dogs if they wish to view historic data. 
    - Users can logout upon completion of their session in order to keep their profile and information secure. 
    - An admin dashboard and superuser rights have been created in order to enable to the management of users, profiles and bookings to ensure the management of the site. 

### Logic

- I used [Lucidchart](https://www.lucidchart.com) to set out the main logic of the site: 

![Lucidchart Diagram](./static/images/readme/lucidchart.png)

### Design

- The design of the site is simple and functional. The core site aim is provide a practical and useful functionality to Pound and Rescue users and in this context a deliberate effort was made to keep the UI clean and clutterfree and to focus on the functionality and views required by the users. 
- Google fonts Fredoka One (Brand) and Varela Round (body) have been used to soften the default font applied by Bootstrap and to add a 'friendlier' feel to the UI. 
- In addition, a simple pawprint has been added as a favicon for the page, again to add an element of warmth and friendliness and in a nod to the core purpose of the site. This icon was sourced from Font Awesome. 

### Wireframes

- High level wireframes for the site were mocked up in gSheets with a focus on the table views that the user types would require. 

Homepage: 

- From the start of planning, I intended the homepage to be a gateway to connector with a clean simple view. This has been carried through to the final design with the main changes being the addition of the header and footer styling for the page. 

![Homepage View](./static/images/readme/homepage_view.png)

All Users:

- The plan was to have a table visible to all users that sets out all of the dogs available for rescue. From this initial mock-up there were some functionality goals that were not possible to implement in the timeframe and actually never made it to the user stories including formal notifications (outside of onscreen messages). Similarly I decided not to let Pound users amend the collection date at this time but potential enable in future functionality the ability to propose an alternative date. 

![All User View](./static/images/readme/all_user_view.png)

Pound Users: 

- The final structure of the site for Pound users largely includes the same functionality as the original mock-up. The primary difference was the decision to split the various tables into their own pages for a cleaner UI and to then add a user dashboard to simplify navigation between these views. I also decided not to implement the comment field in the table again to keep the view clean however this may be something worth revisiting in the future. 

![Pound View](./static/images/readme/pound_view.png)

Rescue Users:

- Similarly, the final structure of the site for Rescue users largely includes the same functionality as the original mock-up again with the primary difference being the decision to split the various tables into their own pages for a cleaner UI and to then add a user dashboard to simplify navigation between these views.

![Rescue View](./static/images/readme/rescue_view.png)

### Database Planning

- The final model structure implemented for the site is as follows: 

![Final Models](./static/images/readme/final_model_structure.png)

***
## Existing Features 

### Landing Page

![Landing Page Screenshot](./static/images/readme/homepage.png)

 - On arrival at the page, their is a header with the site brand name (Connector) and slogan ('Giving Pound Dogs their Second Chance').

__Log In__

  - The landing page requires the user to either Log In or Register in order to proceed with using the site further. 
  - Upon selecting Login, the user is taken to the log in screen to enter their information. 
  - From this view, the user also has a Register or Login button in the top right corner of their screen as part of the header. This is in case the user easily wishes to navigate to Register instead of Login.

![LogIn](./static/images/readme/login.png)

  - If the details entered are incorrect, they will receive an error notification.

![Login Error](./static/images/readme/login_error.png)

__Register__

 - If the user opts to Register from the landing page they will be taken to the Sign Up screen to select which type of user they wish to register as; Pound or Rescue.

![Signup Page](./static/images/readme/signup_page.png)

 - If the user selects Pound they will be taken to a form to create a Pound User account. 

![Pound Register](./static/images/readme/pound_register.png)

 - If the user selects Rescue they will be taken to a form to create a Rescue User account.

![Rescue Register](./static/images/readme/rescue_register.png)

 - If the registration form is not validly completed for either type of user, the user will be notified of the errors to be corrected in order to be able to create their account.

![Registration Error](./static/images/readme/registration_error.png)

### User Dashboards

__Navigation__
  - Once logged in the user will be taken to the dashboard view specific to their user type. 
  - In addition, the navigation bar will now display that they are logged in as user (example) Joe Bloggs and display a Log Out and My Dashboard button to faciliate easy navigation of the site. 

![Rescue Navigation](./static/images/readme/rescue_nav.png)
![Pound Navigation](./static/images/readme/pound_nav.png)

__Pound Dashboard__
   - For Pound users, their dashboard will allow them to navigate to the following views: 
       - See All Dogs: displays all dogs currently uploaded to Connector and with a Hold (will be available once Hold period completed) or Available status.
       - Add a Dog: displays a form for the Pound user to create a dog profile on the site.
       - My Current Dogs: displays all dogs with Available/Hold status that are specific to that Pound user.
       - My Previous Dogs: displays all of that Pound user's dogs with a status of Transferred to Rescue, Rehomed, Reclaimed, PTS or Death Natural Causes.
       - My Booked Dogs: displays all of that Pound user's dogs with a status of Booked and the respective booking information for the Rescue.
       - My Proposed Bookings: display all of that Pound user's dogs with a proposed booking and requires acceptance or rejection by the Pound user.

![Pound Dashboard](./static/images/readme/pound_dashboard.png)

__Rescue Dashboard__
  - For Rescue users, their dashboard will allow them to navigate to the following views: 
       - See All Dogs: displays all dogs currently uploaded to Connector and with a Hold (will be available once Hold period completed) or Available status.
       - My Rescued Dogs: displays all of the dogs with a status of Transferred to Rescue for that Rescue user.
       - My Booked Dogs: displays all of the dogs with a status of Booked where the booking party is the Rescue user.
       - My Proposed Bookings: display all of the dogs with a proposed booking from that Rescue user that is pending acceptance or rejection by the Pound user.

__Logout__
  - Upon logging out, the user is returned to the landing page of the site, displaying the Login and Register buttons.

### Views

__Pound Views__

  - See All Dogs: For See All Dogs, a Pound user can view the detailed information uploaded for each dog that is looking for placement. This will include dogs from their Pound and others with a status of Hold or Available.
  - These dog profiles are sorted based on urgency with the view to tryin to get placement for the most in need dogs as a priority.
  - Pagination has been added to this view to add pages where the tables exceeds 25 entries. 

![All Dogs Pound](./static/images/readme/all_dogs_pound.png)

  - Add a Dog: From Add a Dog, a Pound user is taken to a form whereby they can create a profile for display on the site. This form includes validation if any fields are left unpopulated. 

![Add a Profile](./static/images/readme/create_a_profile.png)

  - Once a profile has been created, the Pound user will see a message to confirm that the profile has been successfully created and be taken back to the See All Dogs view so they can see the profile that has been added. 

![Profile Creation](./static/images/readme/profile_sucess.png)

  - My Current Dogs: From My Current Dogs, a Pound user can see all of their dogs that have a status of Hold or Available. From this view, they can individually edit or delete any of these profiles. 

![My Current Dogs](./static/images/readme/my_current_dogs.png)

  - Edit a Profile: If the Pound user selects to edit a profile they are taken to a form prepopulated with the information for that dog so that it can be edited. If the user deletes information without replacing, an error will be displayed and the profile update cannot be saved.

![Edit a Profile](./static/images/readme/edit_profile.png)
![Edit a Profile Error](./static/images/readme/edit_profile_error.png)

  - When the profile is successfully updated, the user will be notified and returned to the See All Dogs view of the site. 

![Edit a Profile Success](./static/images/readme/profile_edit_success.png)

  - Delete a Profile: If the Pound user selects to delete a profile they are asked to confirm this action. Once confirmed they will again receive a message to confirm successful deletion. 

![Delete Confirmation](./static/images/readme/delete_confirm_request.png)
![Delete Success](./static/images/readme/deletion_confirmation.png)

 - My Proposed Bookings: From My Proposed Bookings, a Pound user can see all of their dogs that have a booking proposed by a Rescue. From this view, they can individually accept or reject the proposed booking.

![Pound Proposed Bookings](./static/images/readme/pound_proposed_bookings.png)

 - Accept a Booking: Where a Pound accepts a booking, the profile status for the dog is updated to Booked and the profile will now display in the users My Bookings view. Upon acceptance the user receives notification of successful acceptance.

![Pound Booking Accepted](./static/images/readme/booking_accepted.png)

 - Reject a Booking: Where a Pound rejects a booking, the profile status for the dog is updated to Available and the profile will now display in the users My Current Dogs view. Upon rejection the user receives a request to confirm the rejection and notification of successful rejection upon confirmation.

![Pound Booking Reject Confirm](./static/images/readme/booking_reject_confirm.png)
![Pound Booking Reject Success](./static/images/readme/booking_reject_success.png)

 - My Booked Dogs: From My Bookings, a Pound user can see all of their dogs that have a confirmed booking by a Rescue. From this view, they can individually delete a booking or confirm the collection of a dog by the Rescue.

![My Booked Dogs](./static/images/readme/pound_my_bookings.png)

 - Where a Pound deletes a booking, the profile status for the dog is updated to Available and the profile will now display in the users My Current Dogs view. Upon deletion the user receives a request to confirm the rejection and notification of successful rejection upon confirmation.

![Pound Booking Delete Confirm](./static/images/readme/booking_delete_confirm.png)

  - Where a Pound confirms collection, the profile status for the dog is updated to Transferred to Rescue and the profile will now display in the users My Previous Dogs view.

![Pound Collection Confirmation](./static/images/readme/pound_collection_confirmed.png)

- My Previous Dogs: From My Previous Dogs, a Pound user can see all of their dogs that have a status of Reclaimed, Rehomed, PTS, Transferred to Rescue or Death Natural Causes. From this view, they can individually edit or delete any of these profiles if required.
- Pagination has been added to this view to add pages where the tables exceeds 25 entries. 

![My Previous Dogs](./static/images/readme/previous_dogs.png)

__Rescue Views__

  - See All Dogs: For See All Dogs, a Rescue User can view the detailed information uploaded for each dog that is looking for placement. This will include dogs with a status of Hold or Available. For Rescue Users, they can also see a Rescue Me button whereby they can create a booking request against any dog profile.
  - These dog profiles are sorted based on urgency with the view to tryin to get placement for the most in need dogs as a priority.
  - Pagination has been added to this view to add pages where the tables exceeds 25 entries. 

![All Dogs Rescue](./static/images/readme/all_dogs_rescue.png)

  - Booking Request: If the Rescue user selects Rescue Me from the See All Dogs dashboard, they are taken to a form to complete to create a booking for the specific dog selected. This form has validation and input guidance to ensure the user can successfully save their request. 

![Booking Request](./static/images/readme/booking_request.png)

  - Upon the booking being successfully saved, the Rescue user will receive notification of success and be returned to the See All Dogs dashboard so they can book further dogs if desired. 

![Booking Success](./static/images/readme/booking_success.png)

- My Proposed Bookings: From My Proposed Bookings, a Rescue User can see all of the dogs that they have proposed a booking for. From this view, they can individually edit or delete a submitted booking request if required.

![Rescue Proposed Bookings](./static/images/readme/rescue_my_proposed.png)

 - Edit a Booking: Where a Rescue decides to edit a booking, they are taken to a booking form prepopulated with the previous booking information. 

![Edit Rescue Booking](./static/images/readme/edit_booking_form.png)

 - When successfully completed and saved, the Rescue user will be notified of their successful update and returned to their dashboard to select their next action. The form will display an error to the user if the fields are not correctly populated. 

 ![Edit Rescue Booking Success](./static/images/readme/rescue_booking_edit_success.png)

 - Delete a Booking: Where a Rescue decides to delete a booking, the profile status for the dog is updated to Available again. Upon deletion the user receives a request to confirm the deletion and notification of successful deletion upon confirmation.

![Rescue Booking Delete Confirm](./static/images/readme/rescue_delete_confirm.png)

![Rescue Booking Delete Success](./static/images/readme/rescue_delete_success.png)

  - My Booked Dogs: This view displays all of the dogs with a status of Booked where the booking party is the Rescue user. From this view the user can again edit or delete the booking if required or confirm collection of the dog by their Rescue.

![Rescue My Bookings](./static/images/readme/rescue_my_bookings.png)

 - Where a confirmed booking is edited, the status of the dog will revert to Booking Proposed again so that the Pound user can reaccept this revised booking. As above, all successful edits and deletions to bookings are notified to the user. 

![Rescue Booking Update](./static/images/readme/rescue_booking_update.png)

  - Where a Rescue user selects to confirm collection, the status of the dog is updated to Transferred To Rescue and will be visible to the Rescue user from their My Rescued Dogs view. Again, the user receives confirmation of this update when selected. 

![Rescue Collection Confirmation](./static/images/readme/rescue_collection_confirmation.png)

  - My Rescued Dogs: My Rescued Dogs shows the specific Rescue user all of the dogs with a status of Transferred to Rescue for that Rescue user.
  - Pagination has been added to this view to add pages where the tables exceeds 25 entries. 

![Rescued Dogs](./static/images/readme/my_rescued_dogs.png)

  - For all dashboards and users, where there is no information to be displayed this is explicitly stated to the user to avoid any confusion that the information may not be loading.

![Blank Dashboard](./static/images/readme/blank_dashboard.png)

***
## Feature Enhancements

 - There are a number of feature enhancements that I believe would be beneficial to the site and further enhancement its usefulness to the user but which I was time constrained to try and incorporate prior to the submission deadline for this project. These include: 

     - Optimising the site display for viewing on mobile devices. Currently due to the tables and level of detail required this is not optimal for mobile and the site really needs to be used on a laptop or desktop device. It would have possible to exclude information from the tables to more easily suit a mobile view but this would have been compromising functionality just for visual purposes which I think would have undermined the usefulness of the site.
     - Adding conditional formatting to the Current Dogs Available for Placement dashboard to color code the urgency cell of the table and to easily enable a Rescue user to identify profiles of dogs most in need of placement. 
     - Adding filters to the dashboards to better allow the User to narrow the information down for their specific need e.g. Rescue users to be able to filter based on location of pounds in their county.
     - Adding a notification functionality so that users receive a notification for updates to profiles that they are a a booking party of e.g. if a Rescue user updates a booking that a notification is sent to the Pound to explicitly state this change and notify them of the need to accept or reject the update
     - Removing status options of Booked/Booking Proposed from the create a dog profile form so that this status can only be rendered by using the booking functionality of the site.
     - Enabling a propose alternative date functionality for the proposed bookings whereby instead of a straight accept or reject booking, a Pound user could propose an alternative collection date if required. 
     - Enabling a password reminder/reset functionality within the site and the ability for the user to manage their own details. 
     - Enabling dynamic additional fields for the Pound user based on the final status of the dog e.g. if a dog was reclaimed, details of the date and individual reclaiming. 
     - Ability for the user to export data to excel or Google sheets.
     - Enhance form population controls for date population e.g. error warning if collection date is prior to current hold date, or collection date is prior to current date.
       
***
## Testing 

### User Story Testing

 - All user stories identified have been tested against the final design with the outcome of this testing set out below. 

![User Story Testing](./static/images/readme/user_story_testing.png)

### Features Testing

 - All design features have been manually tested with the outcome of this testing set out below. 
 - Screenshots have also been included in the Features section above to show the validation output for the various steps completed by the user. 
 - Testing was completed in my local terminal and also in Heroku post deployment. 

![Features Testing](./static/images/readme/functionality_feature_testing.png)

### Permissions Testing

 - All urls have been tested to ensure that only the correct user profiles can access the functionality available to them. The outcome of this testing is set out below. 

![Permissions Testing](./static/images/readme/permissions_testing.png)

### Browser Testing
  - The site was developed and tested using Google's Chrome browser. 
  - The site has also been tested on Safari and functions as intended. 

![Browser Testing](./static/images/readme/browser.png)

  - The site is designed (due to the heavy use of data and tables) for user on a laptop or desktop device and for this reason is sub-optimal on smaller screen sizes. 

![Responsiveness](./static/images/readme/responsiveness.png)
 
### Code Validation Testing 

  - The site code has been passed through the following online validation tools: 

  ![Code Validations](./static/images/readme/validators.png)

__HTML Validation__
  
  - There are no errors for the site when passed through the W3C validator. The information warning regarding the trailing slash in the meta tag has been corrected.

  ![W3C validator](./static/images/readme/html_validation.png)

__CSS Validation__

  - There are no errors for the site when passed through the W3C validator. Warnings were found in relation to the links for Bootstrap and Font Awesome. These were left as is. 

  ![CSS validator](./static/images/readme/css_validator.png)

__Python Validation__

  - The only issues found in any of the python files when passing through the Pep8CI online validator related to line length and some of these were deliberately left as is mostly to avoid impacting the functionality of the code and in a few instances due to the code being easier to read when left as is. 

### Lighthouse Performance Testing

  - Lighthouse testing was performed on the site with perfomance and accessibility scores consistently in the 90%+ range.

  ![Homepage Lighthouse](./static/images/readme/homepage_lighthouse.png)
  ![Login Lighthouse](./static/images/readme/login_lighthouse.png)
  ![Sign Up Options Lighthouse](./static/images/readme/signup_options_lighthouse.png)
  ![Registration Lighthouse](./static/images/readme/registration_lighthouse.png)
  ![Dashboard Lighthouse](./static/images/readme/dashboard_lighthouse.png)
  ![Current Dogs Lighthouse](./static/images/readme/current_dogs_lighthouse.png)
  ![Add a Profile Lighthouse](./static/images/readme/add_a_profile_lighthouse.png)
  ![Edit a Profile Lighthouse](./static/images/readme/edit_a_profile_lighthouse.png)
  ![My Current Dogs Lighthouse](./static/images/readme/my_current_dogs_lighthouse.png)
  ![My Bookings Lighthouse](./static/images/readme/my_bookings_lighthouse.png)
  ![My Proposed Bookings Lighthouse](./static/images/readme/my_proposed_bookings_lighthouse.png)
  ![My Previous Dogs Lighthouse](./static/images/readme/my_previous_dogs_lighthouse.png)

### Accesibility Testing

  - In addition to the lighthouse reports, site accessibility was also tested via [Accessibility Test](https://accessibilitytest.org/) with a score of 98%.

  ![Accessibility](./static/images/readme/accessibility.png)

### Fixed Bugs   
  - The following key bugs arose and were fixed during the development of the site: 

    1. Login Template not being identified: 
          - Issue: When the login functionality was created, the site was not routing to the login.html template. 
          - Solution: Django was looking for a template in a registrations folder. This was created and the routing to the template resolved.
          - Resource:  [StackOverFlow](https://stackoverflow.com/questions/6646400/does-django-ship-with-the-authentication-templates-for-use-with-the-django-contr)

    2. Posting Bookings to Display in Admin View:
          - Issue: When the Rescue user created a booking, this appeared to be created successfully but was not displaying in the admin view. Original code: 
                def post(self, request, id):
                    profile_to_book = get_object_or_404(Profile, id=id)
                    booking_form = BookingForm(request.POST, request.FILES, instance=profile_to_book)
                    if booking_form.is_valid():
                        create_booking = booking_form.save(commit=False)
                        create_booking.rescue = request.user
                        profile_to_book.status = 8
                        create_booking.save()
                        messages.success(request, 'Booking requested successfully.')
                        return redirect('profiles')
                    else:
                        messages.error(request, 'Booking not saved, please try again.')
                        booking_form = BookingForm()

                    return render(
                        request,
                        "create_booking.html",
                        {
                            "booking_form": booking_form,
                        }
                    )
          - Solution: The instance needed to be removed from the booking_form line and added to a create_booking.profile line before create_booking.save().
            ![Solution](./static/images/readme/tutor_support.png)
      
          - Resource: This was resolved with help from Ger in Tutor Support as I had been unable to resolve through Slack or Stack OverFlow research.
    
    3. Admin User Functionality:
          - Issue: Admin superuser view was set up and functioning but if an object was edited or deleted an Integrity Error was displayed and the change could not be saved. 
          - Solution: All migrations had to be deleted and the SQL database reset to then remigrate all models and reenter data. 
          - Resource: Research on [StackOverFlow](https://stackoverflow.com/questions/70274885/insert-or-update-on-table-django-admin-log-violates-foreign-key-constraint) but ultimately Tutor Support to ensure I did not press self-destruct on my project!

    4. Adding Calendar to Date Picker:
          - Issue: Added DatePickerPlus to improve the UI for selecting dates as part of the Profile and Booking forms but was not displaying. 
          - Solution: After adding the {{ form.media }} tag in the template, this was still not working so after further research I realised I need to specify the form name and add jQuery to my files to display the calendar correctly. 
          - Resource: [DatePickerPlus](https://django-bootstrap-datepicker-plus.readthedocs.io/en/latest/Walkthrough.html) guidance plus [StackOverFlow](https://stackoverflow.com/questions/21381096/form-media-not-being-injected-into-a-template) research

    5. Abstract User: 
          - Issue: I had started my initial build and created models for the Profile and Bookings and then worked on creating updates to the User Model. I was having significant issues migrating the changes.  
          - Solution: After some research I discovered that customising the User model mid-build is very challenging to do, so I restarted my project from scratch beginning with the User model and then recreating the other models in the new repo. I was still then having issues with migrating my User so I then had Tutor Support to implement the second solution (see second StackOverFlow link)
          - Resource:  [StackOverFlow](https://stackoverflow.com/questions/6646400/does-django-ship-with-the-authentication-templates-for-use-with-the-django-contr)
          [StackOverFlow](https://stackoverflow.com/questions/44651760/django-db-migrations-exceptions-inconsistentmigrationhistory)

    6. Iteration to display profiles and related booking data in table: 
          - Issue: Items from object list were not displaying in table in HTML template. Then profile information was displaying but not related booking information. 
          - Solution: Typo in for loop; profile instead of Profile corrected the display of profile information and creating nested for loop with dog_booking.x instead of Profile.dog_booking.x to display related Booking data. 
          - Resource: Assistance from Slack community to identify typo in profiles. Support from Oisin in Tutor Support to correct structure of nested loop to display related booking data correctly. 

    7. Display info specific to rescue user:
          - Issue: Information was displaying in the views for the user but was not specific the logged in user and I needed to be able to extract a subset of profile information (based on status) and the related booking information for that profile based on the user logged in. 
          - Solution: After multiple attempts to resolve, including trying to user a serializer to combine both the profile and booking information and then extract the relevant information, I finally utilised the select_related functionality to get the booking information for a user and extend it to include the related profile information which could then be displayed in the relevant template. 
          - Resource: General research including [StackOverflow](https://stackoverflow.com/questions/72765208/how-to-combine-multiple-models-into-one-view-template-in-django) and Django documentation on select_related and making queries.

    8. Pound Deleting Bookings: 
          - Issue: From the tables, the user has the ability to delete bookings however this functionality was throwing an error. I wanted the ability to delete a specific booking and for that profile update the status to Available. 
          - Solution: I identified that the code was trying to select the id for the profile and not the specific booking 
          identifying the booking id not the profile id but changing the code to get the profile object and then get the related booking object through booking_to_delete = profile_to_update.dog_booking.all() I was able to delete the specific booking entry and update the status of the profile based on the deleted booking.
          - Resource: Self-resolved through general research on StackOverFlow and trial and error.

    9. Rescue Deleting/Editing/Confirming Status: 
          - Issue: The deleting/editing/confirming collection functions were not working for Rescue users as I could not get the function to confirm the rescue as the logged in user. This was working fine for Pounds by drilling into the Profile.pound attribute and confirming against a logged in Pound user. 
          - Solution: I flipped the logic of the view to get the Booking information first and use the rescue attribute of that object to compare to the logged in user. I then used select_related again to the get the related profile information for that booking so that the status of the profile could still be updated. 
          - Resource: Self-resolved (eventually!) through general research on [StackOverFlow](https://stackoverflow.com/questions/41252033/django-filter-using-select-related) and trial and error.
      
### Unfixed Bugs
- The are no existing bugs that remain unfixed in the site however there are feature enhancements as noted above that I would like to incorporate into the functionality of the site but was time constrained in completing these items prior to submission.   

***

## Deployment

### Workspace SetUp

Steps to Set up Workspace and Install Django:

 - In your repository install Django and gunicorn with the following command: pip install 'django<4' gunicorn
 - Install supporting libraries:
          pip install dj_database_url psycopg2
          pip install dj3-cloudinary-storage
- Create a requirements.txt file:
          pip freeze --local > requirements.txt
- Create a project via the following command:
          django-admin startproject PROJECT_NAME . (in the case of this project, the project name was "project4")
- Create an app within the project:
          python manage.py startapp APP_NAME (in the case of this project, the app name was "connector")
- Add your new app to the list of installed apps in setting.py
- Migrate these changes via:
          python manage.py migrate
- Test the server works locally:
          python manage.py runserver (Should display Django success page) 

### Deployment

- Prior to deployment in Heroku a database was set up with ElephantSQL, the site was then deployed to Heroku following the below deployment steps: 
  
  Heroku:
   - Log in to Heroku (or create an account if required).
   - Click 'Create a new app'.
   - Enter a name for the app (must be unique). I selected project4new. 
   - Select your region. For me, this is Europe being based in Ireland. 
   - Select "Create app".
   - In the new page for the app, select the Settings tab from the menu at the top of the main screen. 
   - In the Heroku Settings page, go to the 'Config Vars' section and select "Reveal Config Vars".
   - Select 'Add' in the Settings tab of Heroku; in this line enter 'PORT' in the 'Key' field and a 'Value' of 8000. 
   - In these Settings all relevant secret keys and database URLs are also added. 
   
  Gitpod:

    Env.py file
    - These database and secret key URLs are also added to your env.py file in gitHub and this file is included in the gitignore file to ensure config vars are not publically available on Github.
    - In env.py import os
    - Add os.environ["DATABASE_URL"] = "Paste in ElephantSQL database URL"
    - os.environ["SECRET_KEY"] = "Paste in your randomSecretKey"

    Settings.py file
    - Under from pathlib import Path add:
        import os
        import dj_database_url
        if os.path.isfile("env.py"):
          import env
    - Replace the secret key: SECRET_KEY = os.environ.get('SECRET_KEY')
    - Update the Databases value to: 
          DATABASES = {
            'default': 
          dj_database_url.parse(os.environ.get("DATABASE_URL"))
          }
    - Migrate these changes
    - Link file to the templates directory in Heroku (Place under the BASE_DIR line) via: 
          TEMPLATES_DIR = os.path.join(BASE_DIR, 'templates')
    - Change the templates directory to TEMPLATES_DIR. Place within the TEMPLATES array
    - Add Heroku Hostname to ALLOWED_HOSTS; 
          ALLOWED_HOSTS = ["PROJ_NAME.herokuapp.com", "localhost"]
    - Create a procfile at the top level directory and add: web: gunicorn PROJ_NAME.wsgi
    - Add, commit and push the changes in the terminal

  Heroku:
   - In Heroku, select the 'Deploy' section from the menu at the top of the page. 
   - Select GitHub as the deployment method and 'Connect to GitHub'.
   - Find the right repository (here project4new) via the Search functionality and then select 'Connect'.
   - Scroll down to the new 'Manual Deploy' section and select 'Deploy Branch'
   - Wait until the deployment is finished running and select "View".

The live link can be found here: [Connector](https://project4new.herokuapp.com/) 

***

## Languages, Technologies & Libraries

### Languages Used
  - Python
  - HTML5
  - CSS3
  - Javascript

### Technologies Utilised
  - The following tools and resources have been utilised in the creation of this project: 
     - [GitHub](https://github.com/) & [Gitpod](https://gitpod.io/): For development of the site. 
     - [Stackoverflow](): For general guidance and research - specific examples used in final build set out below. 
     - [Slack](https://slack.com/intl/en-ie/): For general guidance and research on project considerations. 
     - [W3C HTML Validator](https://validator.w3.org/)
     - [W3C CSS Validator](https://jigsaw.w3.org/css-validator/)
     - [Pep8CI Validator](https://pep8ci.herokuapp.com/#)
     - [Heroku](https://id.heroku.com/login): To deploy the site
     - [Lucidchart](https://www.lucidchart.com): To create a flow chart of the site logic
     - [Elephant SQL](https://www.elephantsql.com/): For the database
     - [Django](https://www.djangoproject.com/): For site build framework
     - [Boostrap](https://getbootstrap.com/docs/4.0/getting-started/introduction/): For site styling
     - [Bootstrap DatePickerPlus](https://django-bootstrap-datepicker-plus.readthedocs.io/en/latest/index.html): To add calendar widget to forms for better UI
     - [Cloudinary](https://cloudinary.com): Cloudinary has been installed in the app but currently I did not feel that their would be a significant use case for uploading images in the app itself.
     - [Crispy Forms](https://django-crispy-forms.readthedocs.io/en/latest/): For use in profile, booking creation and edit forms.
     - [Django Phonenumber Field](https://django-phonenumber-field.readthedocs.io/en/latest/)
     - [Font Awesome](https://fontawesome.com/): For paw icon
     - [Google Fonts](https://fonts.google.com/): For site fonts

***
## Credits   

### Resources
 - The following resources were key to helping me build functionality critical to the working of the site: 
   - For getting object by id: https://stackoverflow.com/questions/73338018/how-to-get-an-object-by-id-in-django
   - For Int Pk URL structure: https://github.com/fabricius1/DjangoFilmsCRUD/blob/master/films/urls.py
   - For adding delete button to table rows: https://stackoverflow.com/questions/60616526/how-to-add-delete-button-in-each-row-of-my-table
   - Delete buttons: https://stackoverflow.com/questions/55705666/django-tables2-with-edit-and-delete-buttons-how-to-do-it-properly
   - For adding extra fields in registration form: https://stackoverflow.com/questions/45708119/how-to-add-extra-fields-to-django-registration-form
   - For creating an AND Django filter: https://stackoverflow.com/questions/769843/how-to-use-and-in-a-django-filter
   - For adding calendars to dates in forms through DatePicker Plus: https://django-bootstrap-datepicker-plus.readthedocs.io/en/latest/Walkthrough.html
   - Amending Admin view to bring in additional fields: https://stackoverflow.com/questions/48011275/custom-user-model-fields-abstractuser-not-showing-in-django-admin
   - For linking the edit button to the icon: https://docs.djangoproject.com/en/4.1/intro/tutorial04/
   - To add deletion confirmation to deletion actions: https://stackoverflow.com/questions/64070378/how-can-i-use-django-deleteview-in-my-template
   - For displaying messages: https://docs.djangoproject.com/en/4.1/ref/contrib/messages/#:~:text=The%20messages%20framework%20allows%20you,%2C%20warning%20%2C%20or%20error%20).
   - To create accept and reject booking functions: https://www.w3schools.com/django/django_update_record.php
   - To store phone number field in form: https://django-phonenumber-field.readthedocs.io/en/latest/reference.html#model-field https://stackoverflow.com/questions/19130942/whats-the-best-way-to-store-a-phone-number-in-django-models
   - Default Phone Number structure: https://www.twilio.com/docs/glossary/what-e164
   - For adding if empty to the table views: https://stackoverflow.com/questions/56604833/django-if-table-in-template-is-empty-display-something-else
   - Bootstrap documentation
   - Django documentation

### Code Utilisation
 - The following elements of code have specifically been inspired from the following sources: 
    - Code Institute, Hello Django & I Think Therefore I Blog Demonstrations: For guidance and inspiration for this site, including guidance on deployment, messages, querysets, admin functionality, model creation and structure, url structure, form creation, pagination.  
    - As noted in the code, I also took inspiration from Elyse Horan (keelback-code) and her [Out and Proud](https://github.com/keelback-code/out-proud/blob/main/README.md) project particularly in relation to the code for Creating and Editing Profiles.
    - For guidance on user types & permission decorators: https://simpleisbetterthancomplex.com/tutorial/2018/01/18/how-to-implement-multiple-user-types-with-django.html. In the end I decided on a different permssion structure for the page than using decorators but still utilised a lot of the user registration sign up from this tutorial in creating the sign up templates and views. 

### People
 - In addition a big thank you to the following people for their assistance or inspiration in this project:
     - Kasia Bogucka: Our cohort facilitator for keeping us all on track and answering all and any of the many questions!
     - My cohort: For our weekly checkins and tips
     - The Tutor Support team for their assistance in resolving some bugs and in particular, Ger in Tutor Support for helping me resolve an issue where the information from the booking model was submitting but not displaying in the booking model in Admin. There were definitely instances in this build where there support was greatly appreciated in overcoming a hurdle and being able to move forward.

