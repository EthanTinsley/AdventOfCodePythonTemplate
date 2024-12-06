# AdventOfCode Project Setup Guide

Welcome to the AdventOfCode repository! This project is designed to help kickstart your development for the Advent of Code challenges by providing a structured environment with easy setup and automated generation of placeholder solutions for each day's problem.

### Project Directory After Setup

After running the `setup.py` script with the ```--create_all``` flag enabled, your project directory will look like this:

    codeAdventOfCode2024/ 
    ├── requirements.txt 
    ├── .env  
    ├── setup.py  
    ├── environment_setup.ipynb  
    ├── template.ipynb  
    ├── Events/
       ├── Year/
          ├── Day01/
             ├── example.txt
             ├── solution.ipynb # Placeholder solution for Day 1 
          ├── Day02/
             ├── example.txt
             ├── solution.ipynb # Placeholder solution for Day 2 
          ├── ...

## Project Overview

The project contains the following files and directories:

- **`setup.py`**: A Python script used to generate placeholder solutions for each day of the Advent of Code challenge.
- **`environment_setup.ipynb`**: A Jupyter notebook that helps configure the environment to work with the Advent of Code API module.
- **`template.ipynb`**: A template notebook that serves as the starting point for each day's solution.
- **`requirements.txt`**: A list of dependencies required to run the project.

## Setup Instructions

### Step 1: Create a Python Environment (Optional but Recommended)

We recommend creating a virtual environment to keep your dependencies isolated and ensure a clean setup. You can use either a Python `.venv` environment or a Conda environment, depending on your preference.

#### Using `.venv` (Python Virtual Environment)

1. Create a virtual environment:

        python -m venv .venv

2. Activate the virtual environment:
    - **On Windows**:

            python .\.venv\Scripts\activate
    - **On macOS/Linux**:

            python .venv/bin/activate

Reference:
- https://docs.python.org/3/library/venv.html

### Step 2: Install Dependencies

Once your virtual environment is set up and activated, install the necessary dependencies using `pip`.

1. Install the dependencies from the `requirements.txt` file:

        pip install -r requirements.txt

Reference:
- https://packaging.python.org/en/latest/tutorials/installing-packages/
- https://docs.jupyter.org/en/latest/running.html

### Step 3: Run the Environment Setup

Next, run the `environment_setup.ipynb` notebook. This notebook will help configure your environment to work with the Advent of Code API module. 
**Note that you can run jupter notebooks in vs code**

Follow the instructions in the notebook to set up the environment and configure the API.

References:
- https://code.visualstudio.com/docs/datascience/jupyter-notebooks

### Step 4: Run the Setup Script

Once the environment is prepared, run the `setup.py` script to generate the directory structure and create placeholders for each day's solution.

1. Run the `setup.py` script:

        python setup.py

This will create placeholders for each day's solution in the format `dayXX.py`, with a simple structure to help you get started with each day's problem.

## .env File

You should have a `.env` file in the project root directory. This file contains configuration information like your Advent of Code API key, which you can generate from the Advent of Code website.

This should get created in the environment_setup notebook.

Ensure that your `.env` file is included in the `.gitignore` to prevent your API key from being shared in version control.

reference:
- https://www.geeksforgeeks.org/how-to-create-and-use-env-files-in-python/
