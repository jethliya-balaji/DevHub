## Welcome to the official repository of DevHub web application. 
 __Note__ : This project is an entry for the Hackathon Code-Battle-Edition organized by <a href="https://github.com/divanov11" target="_blank" >Dennis Ivy</a> sponsored by <a target="_blank" href="https://harperdb.io/">Harper DB</a> and <a target="_blank" href="https://www.agora.io/en/">Agora</a> 

<br>

## Table of Contents

- [Welcome to the official repository of DevHub web application.](#welcome-to-the-official-repository-of-devhub-web-application)
- [Table of Contents](#table-of-contents)
- [Introduction](#introduction)
- [About Project](#about-project)
- [Project Images Preview](#project-images-preview)
  - [Homepage Preview](#homepage-preview)
  - [Search Page Preview](#search-page-preview)
  - [Profile Page Preview](#profile-page-preview)
  - [Saved Profiles Page Preview](#saved-profiles-page-preview)
  - [Account Page Preview](#account-page-preview)
  - [Edit Account Page Preview](#edit-account-page-preview)
  - [Add Project Page Preview](#add-project-page-preview)
  - [Edit Project Page Preview](#edit-project-page-preview)
  - [Add Skills Page Preview](#add-skills-page-preview)
  - [Edit Skills Page Preview](#edit-skills-page-preview)
- [Tools & Technologies Used](#tools--technologies-used)
- [Features](#features)
- [Usage](#usage)
- [Project Specification](#project-specification)
- [Prerequisite](#prerequisite)
- [Setup and Installation](#setup-and-installation)
- [Contributors](#contributors)
- [Acknowledgement](#acknowledgement)

## Introduction

This markdown file contains all technical documentation related to the setup, deployment, update, and customization of DevHub web application.

## About Project
DevHub is a web application that makes finding talented developers easy for Hiring Managers. This application is aimed at solving One of the major challenges faced by Hiring Managers, which is the lack of an easy process for finding developer/tech talent. With DevHub, the need for recruiters to visit multiple websites in search of developers has been eliminated. Talented Developers can now be found in a single search. Hiring Managers can search for a developer's information and save it for subsequent review.
The primary feature of the site is that all developers' crucial information is fetched from different APIs, this is to ensure that no detail of a developer is left out.

## Project Images Preview 

### Homepage Preview
![Homepage](devhub%20-images/homepage-for-hr.png)

### Search Page Preview
![Saved Profile Page for HRs](devhub%20-images/Searched%20Page.png)

### Profile Page Preview
**Note:** The following linkedin info is fetched from LinkedIn
![Profile Page](devhub%20-images/hr-profile-page.png)

### Saved Profiles Page Preview
**Note:** The following page is only visible to Hiring Managers
![Saved Profile Page HRs](devhub%20-images/saved-profile-pages-only-for-hrs.png)

### Account Page Preview
__Logged in as Hiring Manager__
![Account Page for HR](devhub%20-images/hr-account-page.png)

__Logged in as a Developer__
![Account Page for Developers](devhub%20-images/developers-account-page.png)

### Edit Account Page Preview
__Logged in as Hiring Manager__
![Edit Account Page for HR](devhub%20-images/edit-account-page-for-hr.png)

__Logged in as a Developer__
![Edit Account Page for Developers](devhub%20-images/edit-account-page-for-devs.png)

### Add Project Page Preview
**Note:** The following page is only visible to Developers
![Add Project Page for Devs](devhub%20-images/addproject-page.png)

### Edit Project Page Preview
**Note:** The following page is only visible to Developers
![Edit Project Page for Devs](devhub%20-images/edit-project-page.png)

### Add Skills Page Preview
**Note:** The following page is only visible to Developers
![Add Skills Page for Devs](devhub%20-images/addskills.png)

### Edit Skills Page Preview
**Note:** The following page is only visible to Developers
![Edit Skills Page for Devs](devhub%20-images/edit-skills-page.png)

## Tools & Technologies Used
This project was developed using ![Visual Studio Code](https://img.shields.io/badge/Visual%20Studio%20Code-0078d7.svg?style=for-the-badge&logo=visual-studio-code&logoColor=white) and the following technologies were used: <br/>
* __Design__<br/>
        ![Figma](https://img.shields.io/badge/figma-%23F24E1E.svg?style=for-the-badge&logo=figma&logoColor=white)

* __Frontend__<br/>
      ![HTML5](https://img.shields.io/badge/html5-%23E34F26.svg?style=for-the-badge&logo=html5&logoColor=white)
      ![tailwindCss](https://img.shields.io/badge/tailwindCss-%231572B6.svg?style=for-the-badge&logo=tailwindCss&logoColor=white)
      ![JavaScript](https://img.shields.io/badge/javascript-%23323330.svg?style=for-the-badge&logo=javascript&logoColor=%23F7DF1E)

* __Backend__<br/>
        ![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
        ![Django](https://img.shields.io/badge/django-%23092E20.svg?style=for-the-badge&logo=django&logoColor=white)

* __Databases__<br/>
        ![Harperdb](https://img.shields.io/badge/harperdb-%23F24E1E.svg?style=for-the-badge&logo=harperdb&logoColor=white)
        ![sqlite](https://img.shields.io/badge/sqlite-%2300f.svg?style=for-the-badge&logo=sqlite&logoColor=white)

<!-- * __API__<br/>
        ![DjangoREST](https://img.shields.io/badge/DJANGO-REST-ff1709?style=for-the-badge&logo=django&logoColor=white&color=ff1709&labelColor=gray) -->

* __Project Management and Version Control__<br/>
        ![GitHub](https://img.shields.io/badge/github-%23121011.svg?style=for-the-badge&logo=github&logoColor=white)

## Features

Below are some of the major features of DevHub:

__Hiring Managers__ - An individual that is interested in hiring developers. Users registered as HRs would have access to the following pages after registration:

    - Homepage, they can browse through developers on the page 
    - Profile Page, see thier profiles, can edit etc
    - Account Page
    - Edit Account Page, to update relevant informations related to their accounts
    - Saved Profiles Page, to see developers profiles that was saved for later review or for other reason
    - Searched Page, to search for developers 


__Developers__ - An individual that is interested in getting a job as a developer. Users registered as developers would have access to the following pages:

    - Profile Page, see thier profiles, can edit etc
    - Account Page
    - Searched Page, to search for developers to collaborate with
    - Add Project Page, to add their projects
    - Edit Project Page, to edit the projects on their profiles
    - Add Skills Page, to add their skills
    - skill Page, to edit the skills on their profiles
   
## Usage

 * Visit the website
 * Register as a hiring manager or developer
 * Login with your registered details
 * Explore the full features and different pages of the site
  
## Project Specification
This project is fully responsive and can be accessed / viewed on all screens/devices
* Mobile Phones
* Tablets
* Laptops & Desktop

## Prerequisite 

To run DevHub locally on your system, the following are required:
- A computer running macOS, Windows or Linux 
- Python or pip to manage packages 
- A supported version of Django 


## Setup and Installation
The following installation guides will guide you step-by-step to run this project locally.

- Clone the repository on your local machine - 
```sh
git clone https://github.com/jethliya-balaji/DevHub.git
```
- **Environment Variables:** To run this project, you will need to add the following environment variables to your .env file

    `HARPERDB_URL`

    `HARPERDB_USERNAME`

    `HARPERDB_PASSWORD`

    `LINKEDIN_EMAIL`

    `LINKEDIN_PASSWORD`

    :warning: **Don't use your personal Linkedin because we are using [linkedin-api](https://pypi.org/project/linkedin-api/) module & not the official linkedin APIs**: Be very careful here!

- **Making Virtual Environment:** In the same directory as manage.py run the following command to create virtual environment & activate it.

    `python -m venv env`

    `source env/Scripts/activate` use this to activate from git bash.
    
    `.\env\Scripts\activate` use this to activate from windows terminal.

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

## Contributors
 __Jethliya Balaji__

 [//]: contributor-faces

<a target="_blank" href="https://github.com/jethliya-balaji"><img src="https://avatars.githubusercontent.com/u/74290492?v=4" title="Balaji" width="80" height="80"></a>

[//]: contributor-faces

* Stack - Backend & Design
* Email - jethliya.balaji1@gmail.com
  
__Adebowale Omolara__

[//]: contributor-faces

<a target="_blank" href="https://github.com/omolara5861"><img src="https://avatars.githubusercontent.com/u/72765403?v=4" title="omolara" width="80" height="80"></a>

[//]: contributor-faces
* Stack - Frontend 
* Email - debbiegterra@gmail.com

__Ishika Agrawal__

[//]: contributor-faces

<a target="_blank" href="https://github.com/ishika-ag7"><img src="https://avatars.githubusercontent.com/u/80105387?v=4" title="Ishika" width="80" height="80"></a>

[//]: contributor-faces
* Stack - Frontend
* Email - ishikaagrawal0711@gmail.com

## Acknowledgement
We sincerely appreciate the organizers and the sponsors for this hackathon and for everything that was put in place to make it a success. We have been pushed to do a lot during the course of this hackathon. We are grateful for this opportunity that was given to learn, grow, and also connect with other amazing designers and developers.
