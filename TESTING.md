# Testing 

***

## Validator Testing 

- HTML
  - TODO: how to pass html validation with jinja?

    >![index.html](documentation/testing/html-validation-screenshot.png)


- CSS
  - No errors were found in the `style.css` file when passed through the official [Jigsaw validator](https://jigsaw.w3.org/css-validator/#validate_by_input) CSS validator.
  
    >![style.css](documentation/testing/jigsaw-css-validator-screenshot.png)


- JavaScript
  - No errors were found when `script.js` was passed through the official [JSHint](https://jshint.com/) JavaScript validator.

    >![script.js](documentation/testing/jshint-js-validator-screenshot.png)


- Python
  - No errors were returned and all code met PEP8 compliance when `__init__.py` file was passed through the official [pep8online](http://pep8online.com/) Python validator.

    >![__init__.py](documentation/testing/pep8online-py-__init__.py-validator-screenshot.png)


  - No errors were returned and all code met PEP8 compliance when `models.py` file was passed through the official [pep8online](http://pep8online.com/) Python validator.

    >![__init__.py](documentation/testing/pep8online-py-models.py-validator-screenshot.png)


  - No errors were returned and all code met PEP8 compliance when `routes.py` file was passed through the official [pep8online](http://pep8online.com/) Python validator.

    >![__init__.py](documentation/testing/pep8online-py-routes.py-validator-screenshot.png)


***

### Fixed Bugs

I used the built-in [GitHub Issues](https://github.com/antonia-white/game-base/issues) tracker for tracking any active bugs during development. 
![Github Issues](documentation/testing/github-issues-screenshot.png)

Here are the issues tracked that have been closed and working as intended:

- PSQL connection error [#1](https://github.com/antonia-white/game-base/issues/1)
- password value too long for type character varying(25) [#2](https://github.com/antonia-white/game-base/issues/2)
- 'is_singleplayer' is not defined [#3](https://github.com/antonia-white/game-base/issues/3)
- class 'builtins.dict' is not mapped [#4](https://github.com/antonia-white/game-base/issues/4)
- 'BaseQuery' object has no attribute 'id' [#5](https://github.com/antonia-white/game-base/issues/5)
- local variable 'Genre' referenced before assignment [#6](https://github.com/antonia-white/game-base/issues/6)
- Invalid input syntax for type integer [#7](https://github.com/antonia-white/game-base/issues/7)
- 'list' object has no attribute replace [#8](https://github.com/antonia-white/game-base/issues/8)

***

## Unfixed Bugs 

***

## Browser Compatability

- Website launched successfully on [Firefox](https://www.mozilla.org/en-GB/firefox/new/):

  >![Firefox](documentation/testing/firefox-screenshot.png)

- Website launched successfully on [Google Chrome](https://www.google.com/intl/en_uk/chrome/):

  >![Google Chrome](documentation/testing/chrome-screenshot.png)

- Website launched successfully on [Microsoft Edge](https://www.microsoft.com/en-us/edge):

  >![Microsoft Edge](documentation/testing/edge-screenshot.png)

***

## Responsiveness

- Website viewed in a mobile device:

  >![Mobile view](documentation/testing/mobile-deployment-screenshot.png)

- Website viewed in a tablet device:

  >![Tablet view](documentation/testing/tablet-deployment-screenshot.png)

- Website viewed in a laptop device:

  >![Laptop view](documentation/testing/laptop-deployment-screenshot.png)


***

## User Story Testing

A target user of the Game Base website will want to:
- [x] keep a record of games I want to play in the future
   >The Game Base website...
- [x] be able to add games to my Game Base
   >The Game Base website...
- [x] browse through the games I've added to my Game Base
   >The Game Base website...
- [x] be able to edit the games on my Game Base
   >The Game Base website...
- [x] be able to remove games from my Game Base
   >The Game Base website...
- [x] sort the games I've added to my Game Base by category
   >The Game Base website...
- [x] view basic information of the games on my Game Base 
   >The Game Base website...
- [x] log into my Game Base with my email address and password
   >The Game Base website...


***
