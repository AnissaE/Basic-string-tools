# Software_deployement

## Introduction
This is a project given to 4 year Bio-Informatics and Modelling students of INSA of Lyon. In our Software Deployement courses, we were asked to deploye a python module.

This [git repository](https://github.com/AnissaE/Software_deployement.git) is where you can find our "Play with Words" software. We wrote for you some functions in Python3 so that you can play a little with some words (string type). 

## Coded functions

You may play with words by using a few functions we coded. They are :
- char_freq : Get the number of time each character of your string can be found, taking into account if you want so the case of the character.
- are_anagrams : Find whether or not two strings are anagrams.
- letters_only : Keep only the letters of your string.
- remove : Remove the first occurrence of a string X in a string Y.
- remove_all : Remove all occurrences of a string X in a string Y.

If you need more details, please see our [readthedocs](https://bstools.readthedocs.io/en/latest/#) page.

## Install the software

### Prerequisites

Just make sure that you do have [Python3](https://www.python.org/downloads/). You do not need any other software to have our module working. 

### Install command

First, open a shell in the folder where you want to download the module. You can then write the following instructions:

```
#On Windows
pip.exe install -i https://test.pypi.org/simple/ --no-deps bstools

#On Linux
pip install -i https://test.pypi.org/simple/ --no-deps bstools
```

## Running the tests

Explain how to run the automated tests for this system

## Tutorial



## TODO

- Upgrade remove_all so that it works with something like "lololle" (it becomes "le" when it should be "lole")
- Test all possibilities of our functions
- Create Webpage

## Authors

Everyone of us is a 4 year student at INSA of Lyon in the Bio-Informatics and Modelling Department.
* **Armande CIROT** - Passionnate about drama, she is a slow learner. Yet she is enthusiastic and brings dynamism in her working groups.
* **Anissa EL MARAHI** - A born singer, this Moroccan princess is the sunshine of our days and will regret all her life teaching us some specific arabic words.
* **Claire LEMONNIER** - Hardworking and willing to learn as much as she can, she is currently filling up her confinement days with courses and projects and learning foreign languages. We hope she doesn't forget to work her salsa and kizomba.


## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details.
