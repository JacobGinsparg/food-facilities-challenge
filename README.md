## Project Description

Take-home exercise involving setting up an API to query information from a dataset of food facilities. Goal was to create the API using Python and add tests as well.

## Technical Decisions

### FastAPI

I used FastAPI to set up the API layer. It's widely used (and used by RadAI), straightforward to get off the ground, and has a nice built-in interface with OpenAPI.

### Pandas

For a small exercise I opted to set up a mock database in memory using a Pandas Dataframe. Dataframes have query features built in, so I was able to set up the database file fairly close to how it would be structured if I was using something like MongoDB or PostgreSQL.

### Test data

Given the time constraint I opted to use the main dataset for the tests as well. With a larger-scale/production project I'd set up a smaller set of data to use for the tests.

## Critiques

### Things to do if I had more time

* Pick a db paradigm and set up a concrete database
* Write more tests and set up test data

### Trade-offs

The main trade-off I made was choosing to use Pandas to mock out a database rather than setting up a full relational/document db. This caused some complication with the location query since the Dataframe ended up having a weird interaction with some underlying geopy code. As a result I had to tack on the distance as a new db column and then clean it after each query, which isn't desirable.

### Scaling

As previously mentioned, using an in-memory Pandas Dataframe for a database is very much not scalable. Setting up a real database and updating the `database.py` file to match would help push toward scaling.

## Running the project

To run the main project:

1. Make sure [Poetry](https://python-poetry.org/docs/#installation) is installed.
2. Set up the Poetry environment

```
$ poetry install
$ poetry shell
```

3. Run the uvicorn server

```
$ uvicorn src.food_facilities_challenge.main:app --reload
```

4. Navigate to [`http://127.0.0.1:8000`](http://127.0.0.1:8000)

To run the tests:

1. Follow steps 1-2 from above
2. From the project root, run [Pytest](https://docs.pytest.org/en/7.4.x/)
```
$ pytest
```
