# Game Base

This website allows gamers to keep a record of games that they want to play in the future. 
As a gamer, you often talk to your friends about the games that they're playing and in passing you may hear of cool games that you want to play in the future. Have you ever been in a situation where you are ready to start a new game but you can't quite remember the name of that one particular game that a friend of a friend recomended 2 months ago? Well, Game Base would be perfect for you! It's a quick and simple way of creating a 'to-play' list! Never feel uncertain of what game to play next with Game Base.

To visit the website, please visit the deployed site [here](https://gamebase-storage.herokuapp.com/).

![Responsive Mockup](documentation/testing/responsive-mockup.png)

***

## User Stories

As a user of the Game Base website, I want to:
  1. keep a record of games I want to play in the future
  2. be able to add games to my Game Base
  3. browse through the games I've added to my Game Base
  4. be able to edit the games on my Game Base
  5. be able to remove games from my Game Base
  6. sort the games I've added to my Game Base by category
  7. view basic information of the games on my Game Base 
  8. log into my Game Base with my email address and password

***

## UX

### Colour Scheme
- A calming blend of teal shades and rich blues. This gives a cool and clean look.
    >![colour palette](documentation/testing/color-palette.png)
- No accessibility issues were returned when passing the colour scheme through the official [WebAIM](https://webaim.org/resources/contrastchecker/).
    >![webaim screenshot](documentation/testing/webaim-screenshot.png)

### Typography

- Google Fonts
  Font styles were taken from the open source [Google Fonts](https://fonts.google.com/).
  - the typography for the text throughout the website is [Albert Sans](https://fonts.google.com/specimen/Albert+Sans). This font design was inspired by the type-characteristics of scandinavian architects and designers in the early 20th century. It gives a clean and fresh look to the website. 
  - The typography for the brand logo is font-family [Archivo Narrow](https://fonts.google.com/specimen/Archivo+Narrow?preview.text=Game%20Base&preview.text_type=custom#standard-styles). This font was originally designed for highlights and headlines. This family is reminiscent of late nineteenth century American typefaces. As such, it is eyecatching to the user.

***

### Wireframes

- Home wireframe

 ![Home wireframe](documentation/wireframes/gamebase-home-wireframe.png)



 - Genres wireframe

 ![Genres wireframe](documentation/wireframes/gamebase-genres.png)



 - Mobile browse wireframe

 ![Mobile browse wireframe](documentation/wireframes/gamebase-browse-mobile.png)

 

***

## Database Model
- Database schema for Game Base

 ![database schema](documentation/wireframes/gamebase-schema.png)

***

## Features 

### Existing Features 

__Login__

  - This is the page that first loads when a user visits the website. It allows users to log into their GameBase with their email address and password that they set up during registration.
  - If a user has not yet registered, there is a link to the registration page so they may do so.
  - The log in page contains the navbar, however, if a user tries to navigate to a page (e.g., the games page) without having logged in beforehand they will be uable to do so and directed to log in.
  - If a user logs in with an invalid email and/or password they will be informed and unable to login.
  - The logout button on the navbar has been hidden and disabled as the user is not logged in.

  ![Login](documentation/testing/login-screen.png)


__Register__

  - A user will navigate to this page to create their GameBase account. Once a GameBase account has been created a user will be able to login using their email and password to access the main site content.
  - The user will not be able to create an account if the email provided is already assigned to a GameBase account. If this is attempted the user will be informed.
  - The logout button on the navbar has been hidden and disabled as the user is not logged in.

  ![Register](documentation/testing/register.png)


__Navbar__

  - Once logged in, a user will be able to navigate throughout the website via the navbar.
  - The navbar consits of the website logo (left) and four buttons (right). The buttons navigate the user to the games page, genres, page, consoles page, or logout the user.

  ![Navbar](documentation/testing/navbar.png)


__Mobile Navbar__

  - Once logged in, a user will be able to navigate throughout the website via the navbar.
  - The navbar consits of the website logo (right) and an expandable burger menu (left) which contains four buttons. The buttons navigate the user to the games page, genres, page, consoles page, or logout the user.

  ![Mobile Navbar](documentation/testing/mobile-navbar.png)
  
  When burger menu is expanded:

  ![Expandable Menu](documentation/testing/expandable-menu.png)


__Games__

  - The games page displays all the games the user has saved to their GameBase (in alphabetical order).
  - The add game button navigates the user to the add game fomr (see below).
  - Each game has its own card and displays a game image (if provided by the user). If no image is provided or if a broken url is provided by the user then a default placeholder will be displayed. The game card shows the game title (truncated if the title exceeds 27 characters), an edit game button which directs the user to the edit game form (see below) and a delete game button which results in the delete game modal pop up (see below). When the user clicks on the card area or the kebab icon, the game information content will display (see below).

  ![Games](documentation/testing/games.png)


__Add Game__

  - Clicking the '+ add game' button on the games page will navigate the user to the add game form. 
  - The form requires users to input a game title, select a game genre from the dropdown and provide a release date. The user may also chose to provide details on the game's developer, what console(s) the game can be played on, if the game is singleplayer or not, and finally provide an image url - for aesthetic display.
  - The user will not be able to create a new instance of a game record if the title already exists in their collection of games i.e., a user will not be able to have duplicate entries of one game.
  - Once the user clicks 'add game' and all the required fields have been filled, the game record is added to the database and the game will be displayed on the users Games tab (above).

  ![Add Game](documentation/testing/add-game.png)


__Edit Game__

  - When the green 'edit game' button is clicked on a game's card, the user will be directed to the edit game form.
  - This form will auto-fill with the current values that are saved for that game.
  - As is the same when adding a game,  the edit form requires users to input a game title, select a game genre from the dropdown and provide a release date. The user may also chose to provide details on the game's developer, what console(s) the game can be played on, if the game is singleplayer or not, and finally provide an image url - for aesthetic display.
  - Once the user clicks 'update' the game record will be updated to the new information provided. This will then be displayed.

  ![Edit Game](documentation/testing/edit-game.png)


__Delete Game__

  - 
  - 

  ![Delete Game](documentation/testing/delete-game-modal.png)


__Game Information__

  - 
  - 

  ![Game Information](documentation/testing/game-information.png)
  

__Genres__

  - 
  - 

  ![Genres](documentation/testing/genres.png)


__Consoles__

  - 
  - 

  ![Consoles](documentation/testing/consoles.png)


### Admin Features

__Admin Genres View__

  - 
  - 

  ![Admin Genres](documentation/testing/admin-genres.png)


__Add Genre__

  - 
  - 

  ![Add Genre](documentation/testing/add-genre.png)


__Edit Genre__

  - 
  - 

  ![Edit Genre](documentation/testing/edit-genre.png)


__Delete Genre__

  - 
  - 

  ![Delete Genre](documentation/testing/delete-genre.png)


__Admin Console View__

  - 
  - 

  ![Admin Consoles](documentation/testing/admin-consoles.png)


__Add Console__

  - 
  - 

  ![Add Console](documentation/testing/add-console.png)


__Edit Console__

  - 
  - 

  ![Edit Console](documentation/testing/edit-console.png)


__Delete Console__

  - 
  - 

  ![Delete Console](documentation/testing/delete-console.png)

### Features Left to Implement 

- Have consoles input field autofill with stored values when trying to edit a game 
  - With additional time I would implement this feature by migrating the consoles database to a relational DBMS or relate MongoDB ObjectID's by converting the ObjectId to a time stamp, as seen [here](https://steveridout.com/mongo-object-time/)

***

## Technologies
- [HTML](https://en.wikipedia.org/wiki/HTML) was used as the markup language
- [CSS](https://en.wikipedia.org/wiki/CSS) was used for custom styling
- [JavaScript](https://en.wikipedia.org/wiki/JavaScript) was used for custom website interactivity
- [GitPod](https://gitpod.io) was used as a cloud based iDE
- [GitHub](https://github.com/) was used to manage the Git repository
- [Heroku](https://gamebase-storage.herokuapp.com/) was used for deployment
- [Git](https://git-scm.com/) was used for version control
- [MongoDB](https://www.mongodb.com/) was used as a database management system
- [PostgreSQL](https://www.postgresql.org/) was used as a database management system
- [Jinja](https://jinja.palletsprojects.com/en/3.1.x/) was used as a web template engine for Python
- [Flask](https://flask.palletsprojects.com/en/2.1.x/) python web framework used to create routes
- [Python](https://www.python.org/downloads/) used as a dependency for Flask
- [Psycopg2](https://www.psycopg.org/docs/) was used as a database driver to connect to the postgreSQL database
- [Pip3](https://pip.pypa.io/en/stable/) was the package manager used to install the dependencies
- [Materialize](https://materializecss.com/) was used for website layout and responsive components
- [Google Fonts](https://fonts.google.com/) was used to provide website fonts and icons
- [Am I Responsive](http://ami.responsivedesign.is/) was used to generate a mockup image
- [Dev Tools](https://en.wikipedia.org/wiki/Web_development_tools) was used for testing and responsiveness
- [Lucidspark](https://lucidspark.com/) was used for creating wireframes and schema diagrams

***

## Testing

To view all testing documentation, refer to [TESTING.md](TESTING.md).

***

## Deployment

The site was deployed to Heroku. The live link can be found [here](https://gamebase-storage.herokuapp.com/)

The steps to deploy a Heroku app are as follows: 
1.  Log in to Heroku or create an account if required.
2.  Create a Heroku app - select 'New', from the drop-down menu select Create New App. The app name provided must be unique.
3.  Select a region.
4.  Create.
5.  Navigate to the Resources tab and add a Heroku Postgres database.
6.  Access the Settings Tab and find the Config Vars. For this project you will need the following config vars:
    *   MONGO_DBNAME = the name of your mongo database.
    *   MONGO_URI = the uri for your mongo database.
    *   DATABASE_URL = the url of your heroku postgres database.
    *   SECRET_KEY = a secret key for your app.
    *   PORT = 5000
    *   DEBUG = set to 'True' during development and 'False' upon deployment.
    *   IP = Your IP address

  Please see this [official documentation](https://devcenter.heroku.com/articles/config-vars) on Heroku configuration for more details.

7.  Navigate to the Deploy tab.
8.  Select Github as the deployment method.
9.  Follow steps to link to the appropriate GitHub account.
12. If you wish, enable Automatic Deploys for automatic deployment when you push updates to Github. Or alternativley, select the correct branch for deployment from the drop-down menu and click Deploy Branch for manual deployment.

Final steps: 
1. Create a Procfile in your repository containing `web: python run.py` so that Heroku will identify the app as a Python app.
2. Create an untracked file called env.py in your repo and input the config vars you previously established in Heroku.

### Cloning

Cloning a repository makes it easier to contribute, fix merge conflicts, add or remove files, and push larger commits. To clone this repository from GitHub to a local computer use the following steps:

1.  On GitHub, navigate to the main page of the repository.

2.  Above the list of files, click Code.

3.  Click Use GitHub CLI, then the copy icon.

4.  Open Git Bash and change the current working directory to the location where you want the cloned directory.

5.  Type git clone, and then paste the URL that was copied from step 3 above.

6. Press Enter to create the local clone.

### Forking
A fork is a copy of a repository. Forking a repository allows you to freely experiment with changes without affecting the original project.

To fork this project go to the top left of the repository, where you see the Fork Icon and click Fork.  This will create a copy of the repository for you.


## Credits 

### Content 

- All text throughout the website is self-written.
- Multiple useful articles at [w3schools](https://www.w3schools.com/)
- Various snippets of code adapted from helpful posters on [Stack Overflow](https://stackoverflow.com/)
- The official doccumentation for [Jinja](https://jinja.palletsprojects.com/en/3.1.x/templates/)
- Example combined database [repository](https://github.com/Code-Institute-Solutions/CombinedTaskManager2022) provided by Code Institute was used as a guide

### Media
- The background image was taken from the open source site [Unsplash](https://unsplash.com/)
- The image placeholder when a user doesn't input a link to an image or if the url provided is broken was taken from the open source site [Placeholder.com](https://placeholder.com/)

### Acknowledgments

- My Code Institute mentor, [Tim Nelson](https://github.com/TravelTimN)
- My friends and family for manually testing the site.

***
