# Project Emofighter
![PyPI - Python Version](https://img.shields.io/pypi/pyversions/Django.svg) 


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
python emofighter.py -t 哈哈哈哈哈哈哈
```
**Or**
```
pipenv run python emofighter.py -t 哈哈哈哈哈哈哈
```

## Using Emofighter
**pipenv run python emofighter.py [OPTIONS] ARGS...**
>**OPTIONS:**
> - -b background name
> - -f face name
> 
>**ARGS:**
> - -t the text under the emofighter
 

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
