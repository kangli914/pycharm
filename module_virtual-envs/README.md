# Virtual Environments
To solve module dependency for hosting multi python applications that need different versions of module. The solution for this problem is to create a virtual environment, a self-contained directory tree that contains a Python installation for a particular version of Python, plus a number of additional packages.
Different applications can then use different virtual environments.

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. See deployment for notes on how to deploy the project on a live system.

### Current

Current environment has python 3.7.0. Pip listed current installed package

```
PS C:\Users\perfeng\python_env> python -V
Python 3.7.0
PS C:\Users\perfeng\python_env> pip list
Package    Version
---------- -------
pip        10.0.1
setuptools 39.0.1
```

### Installing (Create Virutal Environments)

Let's say I want to install a few different packages in python 2.7 (v2.7.15) instead of default python 3.7 (v3.7.0)

```
windows: (in linux: 'python3 -m venv python27')

Option 1) using 'virtualenv' to create a virtual environment:
PS C:\Users\perfeng\python_env> pip install virtualenv
Collecting virtualenv
Successfully installed virtualenv-16.0.0

# virtualenv -p allows you to specify the Python interpreter to use. The default is the interpreter that virtualenv was installed with (c:\program files\python\python37\python.exe)
C:\Users\perfeng\python_env>virtualenv -p "C:\Program Files\Python\Python27\python.exe" python27_demo
---
Option 2) running the venv module as a script with the directory path:

& 'C:\Program Files\Python\Python36\python.exe' -m venv python36_demo_option2

```

List out contents of python27_demo virtual environment

```
Directory: C:\Users\perfeng\python_env\python27_demo

Mode                LastWriteTime         Length Name
----                -------------         ------ ----
d-----       10/11/2018   2:18 PM                Include
d-----       10/12/2018  10:32 AM                Lib
d-----       10/12/2018  10:32 AM                Scripts
d-----       10/12/2018  10:31 AM                tcl
-a----       10/12/2018  10:32 AM             59 pip-selfcheck.json
```

End with an example of getting some data out of the system or using it for a little demo

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

* [Dropwizard](http://www.dropwizard.io/1.0.2/docs/) - The web framework used
* [Maven](https://maven.apache.org/) - Dependency Management
* [ROME](https://rometools.github.io/rome/) - Used to generate RSS Feeds

## Contributing

Please read [CONTRIBUTING.md](https://gist.github.com/PurpleBooth/b24679402957c63ec426) for details on our code of conduct, and the process for submitting pull requests to us.

## Versioning

We use [SemVer](http://semver.org/) for versioning. For the versions available, see the [tags on this repository](https://github.com/your/project/tags). 

## Authors

* **Billie Thompson** - *Initial work* - [PurpleBooth](https://github.com/PurpleBooth)

See also the list of [contributors](https://github.com/your/project/contributors) who participated in this project.

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details

## Acknowledgments

* Hat tip to anyone whose code was used
* Inspiration
* etc

