# Django REST Framework Practice


## Introduction
This practice project is about implementing CRUD operation on the User model, using Django REST Framework.



## Endpoints
```
https://localhost/api/user-list/
```

```
https://localhost/api/user-list/
```

After satisfying all the requirements for the project, Open the terminal in the project folder and run
```
python checklist.py
```
or
 
```
python3 checklist.py
```
depending upon the python version. Make sure that you are running the command from the same virtual environment in which the required modules are installed.


![Demo pic of Checklist by akr](resources/images/akr_demo.jpg)

Now you are all set to explore the Checklist. Happy Hacking!!!!!!


## Reporting Bugs
Feel free to report any buys or issues at the below github profile.
Check out my Github profile [a-k-r-a-k-r](https://github.com/a-k-r-a-k-r)






## Getting Started
Our API helps developers and users to build client applications and integrations with our blog site (This is just a practice work).
It is organized around REST. All responses will be returned in JSON format, including errors. User authentication is not taken into consideration so far.

The root endpoint is https://localhost/api/ for all resources.


## Sending a Request
Since this is just a demo project, authentication is not taken into consideration. Therefore auth parameters are not required for requesting a resource.

### Endpoints and Methods

- ```GET /api/user-list/```
Returns list of course reviews
- GET user-info/{id}/
- PUT user-update/{id}/update/
- POST user-add/
- POST user-delete/{id}/

## Error Responses
Our API uses conventional HTTP response codes to indicate success or failure of an API request. In general, codes in the 2xx range indicate success, codes in the 4xx range indicate an error that resulted from the provided information (e.g. a required parameter was missing, a charge failed, etc.), and codes in the 5xx range indicate an error with our servers.







Models

Course
Fields
Name	Description	List
archive_time	When the course was archived by the request sender	@all
avg_rating	Average course rating	@all
completion_ratio	How much of the course the request sender completed	@all
created	When the course was created	@all
