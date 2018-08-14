# Project Emofighter
![PyPI - Python Version](https://img.shields.io/pypi/pyversions/Django.svg) ![pipenv - Version](https://img.shields.io/badge/pipenv-2018.7.1-blue.svg) ![opencv-python Version](https://img.shields.io/badge/opencv--python-3.x-green.svg) ![pillow version](https://img.shields.io/badge/Pillow-5.2.0-green.svg) ![pywin32 version](https://img.shields.io/badge/pywin32-2.2.3-green.svg) ![matplotlib version](https://img.shields.io/badge/matplotlib%20-2.2.3-green.svg)


A powerful tool that helps you enjoy more fun when fighting your friends with emoticons.

You can easily creat some emotion like this:

![Example1.1](https://github.com/Akers/emofighter/blob/master/wiki/resource/image/example/example1.1.png)

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. See deployment for notes on how to deploy the project on a live system.

### Prerequisites

Here is the packages the project emofighter is based on:

 - pillow
 ```
 pip install pillow
 ```
 - pywin32
 ```
 pip install pywin32
 ```
 - matplotlib
 ```
 pip install matplotlib
 ```


### Installing

Pipenv is the package and virtual environment manage tools for these project, you can see more about it in [HERE](https://github.com/pypa/pipenv)

Install Pipenv

```
pip3 install pipenv
```

**Init a project, the pipenv will read all depended packages from Pipfile file.**
```
pipenv install
```
**Run the script**
```
#Enter pipenv shell
pipenv shell
#run script
python emofigther.py -f awkward -bg default -t hhhhhhhhhhhhhh
```
**Or**
```
pipenv run python emofigther.py -f diss -bg cry -t hhhhhhhhhhhhhh
```

## Using Emofighter
**usage: emofigther.py [-h] [-f FACE] [-bg BACKGROUND] [-t TEXT]**
>**OPTIONS:**
>-h, --help            show this help message and exit
>-f FACE, --face FACE  select the face in [awkward|diss|laugth|smail]
>-bg BACKGROUND, --background BACKGROUND
>                        select the background in [cry|default|doubt|point]
>-t TEXT, --text TEXT  the text on emoticon
 

## Running the tests

Explain how to run the automated tests for this system

### Break down into end to end tests

Explain what these tests test and why

```
Give an example
```

### And coding style tests

Explain what these tests test and why

```
Give an example
```

## Deployment

Add additional notes about how to deploy this on a live system

## Built With


## Contributing


## Authors


## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details

## Acknowledgments

* Hat tip to anyone whose code was used
* Inspiration
* etc
