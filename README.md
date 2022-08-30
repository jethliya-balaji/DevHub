<img src="../../devhub/DevHub/static/images/devhub.png" alt="DevHub Homepage" />

## Welcome to the official repository of DevHub web application. 
 __Note__ : This project is an entry for the Hackathon Code-Battle-Edition organized by <a href="https://github.com/divanov11">Dennis Ivy</a> sponsored by Harper DB and Agora

<br>

## About Project
DevHub is a web application that makes finding talented developers easy for Hiring Managers. This application is aimed at solving One of the major challenges faced by Hiring Managers, which is the lack of an easy process for finding developer/tech talent. With DevHub, the need for recruiters to visit multiple websites in search of developers has been eliminated. Talented Developers can now be found in a single search. Hiring Managers can search for a developer's information and save it for subsequent review.
The primary feature of the site is that all developers' crucial information is fetched from different APIs, this is to ensure that no detail of a developer is left out. 

## Table of Contents

1. [Introduction](#introduction)
2. [Features](#features)
3. [Product Specification](#product-specialization)
4. [Technologies Used](#technologies-used)
5. [Prerequisite](#prerequisite)
6. [Setup and Instatllation](#setup-and-installation)
7.  [Usage](#usage)
8. [How To Contribute](#how-to-contribute)
9. [Acknowlodgement](#acknowledgement)
10. [Contributors](#contributors)

## Introduction

This markdown file contains all technical documentation related to the setup, deployment, update, and customization of DevHub web application.

## Features

Below are some of the major features of DevHub:

__Hiring Managers__ - An individual that is interested in hiring developers. Users registered as HRs would have access to the following pages after registration:

    - Home page, they can browse through developers on the page 
    - Visit the platform to view basic information about it
    - View and Interact with the documentation
    - No access to use until registered


__Developers__ - An individual that is interested in getting a job as a developer. Users registered as developers would have access to the following pages:

    - Home page, they can browse through developers on the page 
    - Visit the platform to view basic information about it
    - View and Interact with the documentation
    - No access to use until registered


## Start The App

- **Requirements:** Python installed in system

- **Environment Variables:** To run this project, you will need to add the following environment variables to your .env file

    `HARPERDB_URL`

    `HARPERDB_USERNAME`

    `HARPERDB_PASSWORD`

    `LINKEDIN_EMAIL`

    `LINKEDIN_PASSWORD`

    :warning: **Don't use your personal Linkedin because we are using [linkedin-api](https://pypi.org/project/linkedin-api/) module & not the official linkedin APIs**: Be very careful here!

- **Making Virtual Environment:** In the same directory as manage.py run the following command to create virtual environment

    `python -m venv env`

- **Creating Database & Database Tables:** In the same directory as manage.py run the following command to creating database & database tables.

    `python manage.py makemigrations`

    `python manage.py migrate`

- **Creating Superuser:** Now its time to create superuser so that we can create some skills which can be added by developer to their profile. To create superuser enter the following command.

    `python manage.py createsuperuser`
    
    Now fill the form to create superuser

- **Running the Project:** Now its time to run the project so that we can see it on the web.

    `python manage.py runserver`

    http://127.0.0.1:8000/admin/ now go this url in your browser and login with superuser credentials. Now in projects_skills section click on the skill and create some skills and then logout.

    now got to http://127.0.0.1:8000/ and explorer the site