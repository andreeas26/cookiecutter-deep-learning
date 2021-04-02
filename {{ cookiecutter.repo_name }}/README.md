{{cookiecutter.project_name}}
==============================

{{cookiecutter.description}}

Project Structure
-----------------


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
	└── run.py                  <- Simplifies the execution of one or more of the src scripts 



--------

<p><small>Project based on the <a target="_blank" href="https://github.com/andreeas26/cookiecutter-deep-learning/">cookiecutter deep learning project template</a></p>
