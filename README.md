# Cookiecutter Deep Learning

A cookiecutter template for a DL/ML project. This is just an example based primarely on [cookiecutter for data science](http://drivendata.github.io/cookiecutter-data-science/) and on my personal experience.
It was compiled from different sources. See more examples [here](https://www.jeremyjordan.me/ml-projects-guide/), [here](https://theaisummer.com/best-practices-deep-learning-code/) and [here](https://github.com/cmawer/reproducible-model).


### Requirements to use the cookiecutter template:
-----------
 - Python 2.7 or 3.5+
 - [Cookiecutter Python package](http://cookiecutter.readthedocs.org/en/latest/installation.html) >= 1.4.0: This can be installed with pip by or conda depending on how you manage your Python packages:

``` bash
$ pip install cookiecutter
```

or

``` bash
$ conda config --add channels conda-forge
$ conda install cookiecutter
```


### To start a new project, run:
------------

    cookiecutter https://github.com/andreeas26/cookiecutter-deep-learning.git


### The resulting directory structure
------------

The directory structure of your new project looks like this: 

```
├── LICENSE
│
├── README.md               <- The top-level README for developers using this project.
│
├── configs                 <- Directory for yaml configuration files for model training, scoring, etc
│   └── logging             <- Configuration of python loggers
│
├── data                    <- Provides a place to store data for your project.
│   └── DATA_README.md      <- A readme describing the data and the annotation process if needed.
│
├── docker                  <- Contains one or many Dockerfiles for the project.
│
├── docs                    <- A default Sphinx project; see sphinx-doc.org for details
│
├── experiments             <- Contains all the experiments run during development
│   └── experiment_name     <- It can be automatically set: e.g. YYYY-MM-DD-hh-mm
│       │                 
│       ├── train           <- Trained and serialized models
│       └── evaluation      <- Model predictions, or model summaries
│
├── notebooks               <- Jupyter notebooks. Naming convention is a number (for ordering),
│                               the creator's initials, and a short `-` delimited description, e.g.
│                               `1.0-jqp-initial-data-exploration`.
│
├── reports                 <- Generated analysis as HTML, PDF, LaTeX, etc.
│   └── figures             <- Generated graphics and figures to be used in reporting
│
├── project_name            <- Source code for use in this project.
│   ├── __init__.py         <- Makes src a Python module
│   ├── train.py            <- Defines the actual training loop for the model.
│   ├── evaluate.py         <- Defines the evaluation process for the models.
│   │
│   ├── data                <- Scripts to download or generate data
│   │   └── datasets.py
│   │
│   ├── models              <- Defines collection of ML models for the task unified by the interface in base.py
│   │   │                 
│   │   ├── base.py         
│   │   ├── simple_baseline.py
│   │   └── cnn.py
│   │
│   └── visualization       <- Scripts to create exploratory and results oriented visualizations
│       └── visualize.py
├── tests                   <- Files necessary for running tests.
├── run.py                  <- Simplifies the execution of one or more of the src scripts 
└── requirements.txt 		<- The requirements file for reproducing the analysis environment, e.g.
                         		generated with `pip freeze > requirements.txt`. It will be used by docker.
```

### Running the tests
------------

    py.test tests
