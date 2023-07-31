# Movie Data RESTful API Documentation

## Overview
This API provides access to a database of movies. It allows for the retrieval, creation, modification, and deletion of movie data.

## Base URL
All API endpoints are relative to this base URL:

```
http://localhost:5000
```

## Endpoints

### 1. GET /movies

Returns a list of all movies in the database.

**Request:**

```
GET /movies
```

**Response:**

A JSON array of movie objects. Each object contains the movie details:

```json
[
    {
        "index": 0,
        "budget": 237000000,
        "genres": "Action Adventure Fantasy Science Fiction",
        "homepage": "http://www.avatarmovie.com/",
        "id": 19995,
        "keywords": "culture clash future space war space colony society",
        "original_language": "en",
        "original_title": "Avatar",
        "overview": "In the 22nd century, a paraplegic Marine is dispatched...",
        "popularity": 150.437577,
        // Other fields...
    },
    // More movie objects...
]
```

### 2. POST /movies

Adds a new movie to the database.

**Request:**

```
POST /movies
Content-Type: application/json

{
    "budget": 200000000,
    "genres": "Action Adventure",
    "homepage": "http://www.example.com",
    "id": 12345,
    "keywords": "action adventure",
    "original_language": "en",
    "original_title": "Example Movie",
    "overview": "This is an example movie.",
    "popularity": 100.0,
    // Other fields...
}
```

**Response:**

A JSON object containing the details of the movie that was added:

```json
{
    "index": 0,
    "budget": 200000000,
    "genres": "Action Adventure",
    "homepage": "http://www.example.com",
    "id": 12345,
    "keywords": "action adventure",
    "original_language": "en",
    "original_title": "Example Movie",
    "overview": "This is an example movie.",
    "popularity": 100.0,
    // Other fields...
}
```

### 3. GET /movies/:id

Returns the movie with the given ID.

**Request:**

```
GET /movies/:id
```

Replace `:id` with the ID of the movie you want to retrieve.

**Response:**

A JSON object containing the details of the requested movie:

```json
{
    "index": 0,
    "budget": 237000000,
    "genres": "Action Adventure Fantasy Science Fiction",
    "homepage": "http://www.avatarmovie.com/",
    "id": 19995,
    "keywords": "culture clash future space war space colony society",
    "original_language": "en",
    "original_title": "Avatar",
    "overview": "In the 22nd century, a paraplegic Marine is dispatched...",
    "popularity": 150.437577,
    // Other fields...
}
```

### 4. PUT /movies/:id

Updates the movie with the given ID.

**Request:**

```
PUT /movies/:id
Content-Type: application/json

{
    "budget": 250000000
}
```

Replace `:id` with the ID of the movie you want to update. The request body should be a JSON object containing the fields you want to update and their new values.

**Response:**

A JSON object containing the details of the updated movie:

```json
{
    "index": 0,
    "budget": 250000000,
    "genres": "Action Adventure Fantasy Science Fiction",
    "homepage": "http://www.avatarmovie.com/",
    "id": 19995,
    "keywords": "culture clash future space war space colony society",
    "original_language": "en",
    "original_title": "Avatar",
    "overview": "In the 22nd century, a paraplegic Marine is dispatched...",
    "popularity": 150.437577,
    // Other fields...
}
```

### 5. DELETE /movies/:id

Deletes the movie with the given ID.

**Request:**

```
DELETE /movies/:id
```

Replace `:id` with the ID of the movie you want to delete.

**Response:**

HTTP status code 204 (No Content) if the deletion was successful.

### 6. GET /movies/search

Returns a list of movies that match the given search parameters.

**Request:**

```
GET /movies/search?genres=Action&original_language=en
```

You can include any of the following parameters in the query string:

- genres
- original_language
- original_title
- keywords

**Response:**

A JSON array of movie objects that match the search parameters:

```json
[
    {
        "index": 0,
        "budget": 237000000,
        "genres": "Action Adventure Fantasy Science Fiction",
        "homepage": "http://www.avatarmovie.com/",
        "id": 19995,
        "keywords": "culture clash future space war space colony society",
        "original_language": "en",
        "original_title": "Avatar",
        "overview": "In the 22nd century, a paraplegic Marine is dispatched...",
        "popularity": 150.437577,
        // Other fields...
    },
    // More movie objects...
]
```

### 7. GET /movies/popular

Returns a list of the most popular movies, up to a specified limit.

**Request:**

```
GET /movies/popular?limit=5
```

You can include the `limit` parameter in the query string to specify the maximum number of movies to return. If `limit` is not provided, it defaults to 10.

**Response:**

A JSON array of the most popular movie objects, up to the specified limit:

```json
[
    {
        "index": 0,
        "budget": 237000000,
        "genres": "Action Adventure Fantasy Science Fiction",
        "homepage": "http://www.avatarmovie.com/",
        "id": 19995,
        "keywords": "culture clash future space war space colony society",
        "original_language": "en",
        "original_title": "Avatar",
        "overview": "In the 22nd century, a paraplegic Marine is dispatched...",
        "popularity": 150.437577,
        // Other fields...
    },
    // More movie objects...
]
```

## Running the Server

To start the server, run the Python script that contains the API code:

```shell
python app.py
```

The server will start running on `localhost` port `5000`.

## Error Handling

In case of a server error, the response will be a JSON object with an `error` key, containing a description of the error:

```json
{
    "error": "Description of the error"
}
```

## Status Codes

The API returns the following status codes:

- 200 (OK): The request was successful.
- 201 (Created):

 The request was successful, and a resource was created.
- 204 (No Content): The request was successful, but there is no representation to return (i.e. the response is empty).
- 400 (Bad Request): The request could not be understood or was missing required parameters.
- 404 (Not Found): Resource could not be found.
- 500 (Internal Server Error): A problem occurred with the server.
