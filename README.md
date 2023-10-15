## **Missing Values**

### Author: **Marlon Marin**

### Description: 
Herein, we will learn how to process and treat data with missing values.

## Requirements

- [Anaconda](https://www.anaconda.com/download/) >= 4.x
- [git](https://git-scm.com/) >= 2.x
- [Cookiecutter Python package](http://cookiecutter.readthedocs.org/en/latest/installation.html) >= 1.4.0:
    This can be installed via `pip` or `conda` depending on how you manage Python packages:

``` bash
pip install cookiecutter
```

or

``` bash
conda install -c conda-forge cookiecutter
```

## Create a new project

In the new directory where you want to save your generated project:

```bash
cookiecutter https://github.com/platzi/curso-entorno-avanzado-ds --checkout cookiecutter-personal-platzi
```


## Directory and file structure resulting

    missing_values
        ├── data
        │   ├── processed      <- The final, canonical data sets for modeling.
        │   └── raw            <- The original, immutable data dump.
        │
        ├── notebooks          <- Jupyter notebooks. Naming convention is a number (for ordering),
        │                         the creator's initials, and a short `-` delimited description, e.g.
        │                         `1.0-jvelezmagic-initial-data-exploration`.
        |
        ├── models             <- ML models
        |
        ├── .gitignore         <- Files to ignore by `git`.
        │
        ├── environment.yml    <- The requirements file for reproducing the analysis environment.
        │
        └── README.md          <- The top-level README for developers using this project.

---
# missing-values
