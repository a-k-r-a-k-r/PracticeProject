# Django REST Framework Practice


## Introduction
This practice project is about implementing CRUD operation on the User model, using Django REST Framework.


## Getting Started
Our API helps developers and users to build client applications and integrations with our blog site (This is just a practice work).
It is organized around REST. All responses will be returned in JSON format, including errors. User authentication is not taken into consideration so far.

The root endpoint is https://localhost/api/ for all resources.


## Sending a Request
Since this is just a demo project, authentication is not taken into consideration. Therefore auth parameters are not required for requesting a resource.

### Endpoints and Methods

- ```GET /api/user-list/ ``` Returns list of all the users
- ``` GET user-info/{id}/ ``` Returns the informations retaled to the user with the specified id
- ``` PUT user-update/{id}/update/ ``` Updated the user info for the user with the specified id
- ``` POST user-add/ ``` Creates a new user
- ``` POST user-delete/{id}/ ``` Deletes the user with the specified id from the database

## Error Responses
Our API uses conventional HTTP response codes to indicate success or failure of an API request. In general, codes in the 2xx range indicate success, codes in the 4xx range indicate an error that resulted from the provided information (e.g. a required parameter was missing, a charge failed, etc.), and codes in the 5xx range indicate an error with our servers.


## Reporting Bugs
Feel free to report any buys or issues at the below github profile.
Check out my Github profile [a-k-r-a-k-r](https://github.com/a-k-r-a-k-r)
