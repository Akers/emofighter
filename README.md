# Project Emofighter
![PyPI - Python Version](https://img.shields.io/pypi/pyversions/Django.svg) ![pipenv - Version](https://img.shields.io/badge/pipenv-2018.7.1-blue.svg) ![opencv-python Version](https://img.shields.io/badge/opencv--python-3.x-green.svg) ![pillow version](https://img.shields.io/badge/Pillow-5.2.0-green.svg) ![pywin32 version](https://img.shields.io/badge/pywin32-2.2.3-green.svg) ![matplotlib version](https://img.shields.io/badge/matplotlib%20-2.2.3-green.svg)


A powerful tool that helps you enjoy more fun when fighting your friends with emoticons.

You can easily creat some emotion like this:

![Example1.1](https://github.com/Akers/emofighter/blob/master/wiki/resource/image/example/example1.1.png)

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. See deployment for notes on how to deploy the project on a live system.

### Installing

We using [pipenv](https://github.com/pypa/pipenv) for our package management. So we can install depends with pipenv
1. Install pipenv(Skips this when you aleady isntalled):
```
pip3 install pipenv
```
2. Install depended packages with pipenv:
**Init a project, the pipenv will read all depended packages from Pipfile file.**
```
pipenv install
```
> Pipenv is the package and virtual environment manage tools for these project, you can see more about it in [HERE](https://github.com/pypa/pipenv)


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
**emofigther.py [-h] [-f {smail,awkward,diss,laugth}] [-bg {default,cry,doubt,point}] -t TEXT**
>**OPTIONS:**
>>
>> **-h, --help**            show this help message and exit
>>
>> **-f FACE, --face FACE**  select the face in [awkward|diss|laugth|smail]
>>
>> **-bg BACKGROUND, --background BACKGROUND** select the background in [cry|default|doubt|point]
>>
>> **-t TEXT, --text TEXT**  the text on emoticon
 
### More configurations
All configurations is located in configs.py
#### APP_CTX
```python
APP_CTX={
    "app_root": os.getcwd(), # Configs the root path of scrpit main workspace PLEASE DO NOT MODIFIY IT NOT NECESSARY 
    "resources": "resources" # Configs the resource path
}
```
#### CONFIGS
##### emo
the emo configs the face and backgrounds of emoticon
```python
"backgrounds":[ # configs a background list for emotion creation
    {
        # it just a name
        "name":"default",
        # the image path, using get_resource("") when relatived the resources path or a absolute path as well.
        "path":get_resource("/background/pander/default.png"),
        # the command of the resource, same as the value of "-f" option like "emofigther.py -f default" etc.
        "command":"default"
    },
    # ...other backgrounds...
],
"faces":[ # configs a face list for emotion creation
    {
        # it just a name
        "name":"smail",
        # the image path, using get_resource("") when relatived the resources path or a absolute path as well.
        "path":get_resource("/face/jgz/smail.png"),
        # the command of the resource, same as the value of "-bg" option like "emofigther.py -bg smail" etc.
        "command":"smail"
    },
    # ...other faces...
]
```
##### Customizing Resources
you can create your own background image just flows these rules:
1. 250 pixel width
2. A circle like area in wite [RGB(255,255,255)]
here is an example:
![Example1.2.3.4.1](https://github.com/Akers/emofighter/blob/master/emofigther/resources/background/pander/doubt.png)

and face image just flows these rules:
1. with a wite background [RGB(255,255,255)].
2. put the face in the center as you can.
3. see the rule 1.
here is an example:
![Example1.2.3.4.2](https://github.com/Akers/emofighter/blob/master/emofigther/resources/face/jgz/diss.png)

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
