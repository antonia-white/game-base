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

- __Example Feature__

  - 
  - 

    >![Example](documentation/testing/example-screenshot.png)

### Features Left to Implement 

- Have consoles input field autofill with stored values when trying to edit a game 
  - With additional time I would implement this feature by migrating the consoles database to a relational DBMS or relate MongoDB ObjectID's by converting the ObjectId to a time stamp, as seen [here](https://steveridout.com/mongo-object-time/)

***

## Technologies
- [HTML](https://en.wikipedia.org/wiki/HTML) was used as the markup language
- [CSS](https://en.wikipedia.org/wiki/CSS) was used for styles
- [JavaScript](https://en.wikipedia.org/wiki/JavaScript) was used for website interactivity
- [GitPod](https://gitpod.io) was used as a cloud based iDE
- [GitHub](https://github.com/) was used to manage the Git repository
- [Heroku](https://gamebase-storage.herokuapp.com/) was used for deployment
- [Git](https://git-scm.com/) was used for version control
- [MongoDB](https://www.mongodb.com/) was used as a database management system
- [PostgreSQL](https://www.postgresql.org/) was used as a database management system
- [Jinja](https://jinja.palletsprojects.com/en/3.1.x/) was used as a web template engine for Python
<!-- TODO: - [Python]()  -->
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

The site was deployed to GitHub pages. The steps to deploy are as follows: 
  - In the [GitHub repository](https://github.com/antonia-white/space-invaders), navigate to the Settings tab.
  - From the source section drop-down menu, select the **Main** Branch, then click "Save".
  - The page will be automatically refreshed with a detailed ribbon display to indicate the successful deployment.

The live link can be found [here](https://antonia-white.github.io/space-invaders/)

### Local Deployment

In order to make a local copy of this project, you can clone it. In your IDE Terminal, type the following command to clone the repository:

- `git clone https://github.com/antonia-white/space-invaders.git`

Alternatively, if using Gitpod, you can click below to create your own workspace using this repository.

[![Open in Gitpod](https://gitpod.io/button/open-in-gitpod.svg)](https://gitpod.io/#https://github.com/antonia-white/space-invaders)

### How to Install Jest
In the terminal create a json file by running:
```
npm init
```
Click through the default configurations, set Jest as the test command by entering the string "jest" when cued.

Once this is done, to install Jest as a development dependency run:
```
npm i --save-dev jest
```
To run Jest and the built tests simply run:
```
npm test
```
in the terminal.

Note: You may need to manually install the jsdom environment. To do this simply run:
```
npm i jest-environment-jsdom
```
in the terminal when prompted after Jest installation.

You can read more about how to set up Jest using their [official documentation](https://jestjs.io/docs/getting-started).

***

## Credits 

### Content 

- All text throughout the website is self-written.
- 

### Media

- 

### Acknowledgments

- My mentor Tim
- My friends and family for testing the site and helping me identify bugs
- 

***
