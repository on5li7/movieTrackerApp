# Testing Plan and Strategies
  
  Testing the app ensures that it functions as intended and meets the user's requirements. The following testing strategies will be employed to ensure that the app performs optimally:

**Manual Testing**

  Manual testing involves a user executing test cases and validating the app's performance. Manual testing will be conducted to test the app's user interface, functionality, compatibility, and performance.

 _User Interface (UI) Testing_

  UI testing will ensure that the app's user interface is user-friendly, intuitive, and responsive. It will focus on ensuring that the app's UI elements, such as buttons, fields, and icons, are easy to understand and use. UI testing will also ensure that the app's design is consistent.

_Functional Testing_
  
  Functional testing will ensure that the app's features and functionalities work as intended. It will test each feature of the app, such as adding a movie or show, moving a movie or show to another list, rating a movie or show, commenting on a movie or show, and editing a movie or show. Functional testing will also ensure that the app's features work together and that the app performs as expected.

_Compatibility Testing_

  Compatibility testing will ensure that the app works on different platforms, devices, and screen sizes. It will test the app on various devices, such as smartphones, tablets, and laptops, and on different operating systems, such as Android and iOS. Compatibility testing will also ensure that the app works on different versions of the operating system and that it can adapt to different screen sizes and resolutions.

_Performance Testing_

  Performance testing will ensure that the app performs optimally and that it does not crash or become unresponsive. It will test the app's loading time, response time, and resource utilization. 

# Test Cases
  
  The test cases are designed to ensure that the app functions correctly and meets the user's requirements. The test cases are as follows:

**Test Case 1: Add a Movie or Show**
  1) Launch the app by running the menu_page.py file. 
  2) Select one of the three lists: Unwatched, Currently Watching, and Watched.
  3) Click the "Add Movie/Show" button on the top right.
  4) Enter the title of the movie or show.
  5) Click the "Save Input" button.
  6) Verify that the movie or show title has been added. 

**Test Case 2: Move a Movie or Show to another List**
  1) Launch the app by running the menu_page.py file.
  2) Select one of the three lists: Unwatched, Currently Watching, and Watched.
  3) Choose the movie or show you want to move to another list by clicking the green button on top left of the movie of show (Unwatched to Currently Watching or Curretnly Watching to Watched). 
  4) Verify that the movie or show has been moved to the chosen list.

**Test Case 3: Rate a Movie or Show**
  1) Launch the app by running the menu_page.py file.
  2) Select one of the three lists: Unwatched, Currently Watching, and Watched.
  3) Click the "Add Movie" button on the top right.
  4) Enter the rating out of 5 stars.
  5) Click the ""Save Input"" button.
  6) Verify that the rating has been added.

**Test Case 4: Comment on a Movie or Show**
  1) Launch the app by running the menu_page.py file.
  2) Select one of the three lists: Unwatched, Currently Watching, and Watched.
  3) Click the "Add Movie/Show" button on the top right.
  4) Enter the comment in the text box.
  5) Click the "Save Input" button.
  6) Verify that the comment has been added.

**Test Case 5: Edit a Movie or Show**
  1) Launch the app by running the menu_page.py file.
  2) Click the menu button and choose a list.
  3) Click on the movie image to pop up edit window.
  4) Make the necessary changes, if not click on cancel.
  5) Click the "Save" button.
  6) Verfity that the changes have been updated.

**Test Case 6: Add Image Path of a Movie or Show**
  1) Launch the app by running the menu_page.py file. 
  2) Select one of the three lists: Unwatched, Currently Watching, and Watched.
  3) Click the "Add Movie/Show" button on the top right.
  4) Enter enter the image URL of the movie or show.
  5) Click the "Save Input" button.
  6) Verify that the image path for movie or show has been added.
