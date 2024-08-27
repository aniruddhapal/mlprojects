# Student Performance Predictor

## Overview

The **Student Performance Predictor** is a machine learning project designed to predict student test scores based on various demographic and educational factors. The application uses data such as gender, ethnicity, parental level of education, lunch type, and test preparation course to build predictive models that estimate student performance. This project is built with scalability and automation in mind, using AWS Elastic Beanstalk for deployment and GitHub Actions for CI/CD (Continuous Integration and Continuous Deployment).

## Project Structure

The project is organized into several key directories and files, each serving a specific purpose:

### 1. `.ebextensions/`
This directory contains configuration files for deploying the application on AWS Elastic Beanstalk. It includes environment settings and other necessary configurations to ensure smooth deployment.

- **python.config**: Configuration settings for the Python environment in Elastic Beanstalk.

### 2. `.github/workflows/`
This folder contains YAML files for GitHub Actions workflows, which automate various tasks such as testing, building, and deploying the application.

- **main_predictstudentscore.yml**: The workflow file that defines the CI/CD pipeline, automating the process of testing and deploying the project.

### 3. `src/`
This is the core directory of the project, containing the main application code. It is divided into two subfolders:

#### a. `components/`
Contains modules responsible for the essential steps in the machine learning pipeline:

- **data_ingestion.py**: Handles the collection and loading of data from various sources.
- **data_transformation.py**: Manages data cleaning, transformation, and preparation for model training.
- **model_trainer.py**: Contains the code for training machine learning models using the processed data.

#### b. `pipeline/`
Contains scripts for managing the prediction and training pipelines, along with utility and logging functions:

- **predict_pipeline.py**: Manages the process of making predictions with the trained model.
- **train_pipeline.py**: Coordinates the training process, including data loading, transformation, and model training.
- **logger.py**: Handles logging for the application, capturing important events and errors.
- **exception.py**: Defines custom exception handling to improve error management.
- **utils.py**: Contains utility functions used throughout the project.

### 4. `template/`
This folder contains the HTML templates used to create the web interface of the application.

- **home.html**: The homepage of the web application.
- **index.html**: The main page where users can interact with the prediction model.

### 5. Other Important Files

- **requirements.txt**: Lists all the Python libraries and dependencies required to run the project.
- **README.md**: Provides an overview and detailed explanation of the project (this file).
- **.gitignore**: Specifies files and directories that should be ignored by Git to avoid cluttering the repository with unnecessary files.
- **wsgi.py**: The entry point for the WSGI application, used to serve the web application in a production environment.

## How It Works

1. **Data Collection**: The project starts with gathering data from the source, which is then ingested and stored for processing.

2. **Data Preprocessing**: The raw data undergoes a series of transformations, including cleaning, normalization, and feature engineering, to make it suitable for model training.

3. **Model Training**: Using the preprocessed data, machine learning models are trained to predict student performance based on the input features.

4. **Prediction Pipeline**: Once trained, the model can be used to make predictions on new data through a user-friendly web interface.

5. **Deployment**: The application is deployed using AWS Elastic Beanstalk, with GitHub Actions automating the testing, building, and deployment processes.

## Conclusion

This project is a comprehensive machine learning solution that not only focuses on building predictive models but also ensures a smooth deployment process with robust CI/CD practices. The well-organized project structure makes it easy to navigate and extend, whether you're a developer looking to contribute or a user interested in using the application.
