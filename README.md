# Microservice INIT

### Project Setup

#### dependencies

- Docker
- uv
- Alembic
- SQLAlchemy
- Postgres

##

### Run the app

- Create alembic revision:

```bash
make alembic-rev m="create user table"
```

### User Management

- Create a new account
- handle user login
- reset password
- get user by id
- get all users
- delete a user
