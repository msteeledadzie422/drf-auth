# LAB - Class 33
# Project: Authentication & Production Server
## Author: Mandela Steele-Dadzie

### Testing:

It is necessary to install httpie to successfully run tests on this application.

The following endpoints are available:

- GET api/v1/snacks/
- POST api/v1/snacks/
- GET api/v1/snacks/<id>/
- PUT api/v1/snacks/<id>/
- PATCH api/v1/snacks/<id>/
- DELETE api/v1/snacks/<id>/
- POST api/token/
- POST api/refresh/

An example GET request would be handled as follows:

http GET http://localhost:8000/api/v1/snacks/

and should return an example output of:

HTTP/1.1 200 OK
Allow: GET, POST, HEAD, OPTIONS
Content-Length: 19
Content-Type: application/json
Date: Mon, 09 May 2023 00:00:00 GMT

[
    {
        "id": 1,
        "name": "snack 1",
        "description": "description 1"
    },
    {
        "id": 2,
        "name": "snack 2",
        "description": "description 2"
    }
]

An example POST request would be handled as follows:

http POST http://localhost:8000/api/v1/snacks/ name="new snack" description="new snack description"

and should return an example output of:

HTTP/1.1 201 Created
Allow: GET, POST, HEAD, OPTIONS
Content-Length: 38
Content-Type: application/json
Date: Mon, 09 May 2023 00:00:00 GMT

{
    "id": 3,
    "name": "new snack",
    "description": "new snack description"
}

