# Py-Init FastAPI Application

A FastAPI application with PostgreSQL database, built with UV for dependency management and Docker for containerization.

## Quick Start

### Prerequisites

- Docker and Docker Compose
- Git

### Running the Application

1. **Clone the repository**

   ```bash
   git clone <repository-url>
   cd py-init
   ```

2. **Set up environment variables**

   ```bash
   cp .env.example .env
   # Edit .env file with your configuration
   ```

3. **Start the application with Docker Compose**

   ```bash
   # For development (with hot reload)
   docker compose -f docker-compose.yml -f docker-compose.dev.yml up --build

   # Alternative: Use make commands
   make docker-dev

   # For production
   docker compose up --build
   # or
   make docker-prod
   ```

4. **Run database migrations**

   ```bash
   # In a new terminal, run migrations
   docker compose exec app uv run alembic upgrade head

   # Alternative: Use make command
   make docker-migrate
   ```

5. **Access the application**
   - API: http://localhost:8000
   - API Documentation: http://localhost:8000/docs
   - Health Check: http://localhost:8000/health

## Development

### Local Development (without Docker)

1. **Install UV** (if not already installed)

   ```bash
   curl -LsSf https://astral.sh/uv/install.sh | sh
   ```

2. **Install dependencies**

   ```bash
   uv sync
   ```

3. **Start PostgreSQL** (using Docker)

   ```bash
   docker-compose up db
   ```

4. **Run migrations**

   ```bash
   make alembic-upgrade
   ```

5. **Start the application**
   ```bash
   make run
   ```

### Available Make Commands

```bash
make run                    # Run the FastAPI application
make alembic-rev m="msg"   # Create new migration
make alembic-upgrade       # Apply migrations
make alembic-downgrade     # Rollback last migration
```

### Database Migrations

```bash
# Create a new migration
make alembic-rev m="add user table"

# Apply migrations
make alembic-upgrade

# Rollback migrations
make alembic-downgrade
```

## Docker Commands

### Development

```bash
# Start services with hot reload
docker compose -f docker-compose.yml -f docker-compose.dev.yml up

# View logs
docker compose logs -f app

# Execute commands in container
docker compose exec app uv run alembic upgrade head
docker compose exec app uv run python -c "print('Hello from container')"
```

### Production

```bash
# Build and start services
docker compose up --build -d

# Scale the application
docker compose up --scale app=3

# View logs
docker compose logs -f
```

### Useful Docker Commands

```bash
# Rebuild containers
docker compose build --no-cache

# Stop and remove containers
docker compose down

# Stop and remove containers + volumes
docker compose down -v

# Access database directly
docker compose exec db psql -U postgres -d py_init
```

## Project Structure

```
py-init/
├── api/
│   └── app/
│       ├── main.py          # FastAPI application
│       ├── db/
│       │   └── session.py   # Database configuration
│       └── user/
│           └── model.py     # User model
├── alembic/                 # Database migrations
├── docker-compose.yml       # Production Docker setup
├── docker-compose.dev.yml   # Development overrides
├── Dockerfile              # Application container
├── pyproject.toml          # Python dependencies
├── Makefile               # Development commands
└── README.md              # This file
```

## Environment Variables

| Variable       | Description                  | Default                                                         |
| -------------- | ---------------------------- | --------------------------------------------------------------- |
| `DATABASE_URL` | PostgreSQL connection string | `postgresql+asyncpg://postgres:password@localhost:5432/py_init` |
| `DEBUG`        | Enable debug mode            | `false`                                                         |
| `PORT`         | Application port             | `8000`                                                          |
| `HOST`         | Application host             | `0.0.0.0`                                                       |

## API Endpoints

- `GET /` - Welcome message
- `GET /health` - Health check
- `GET /docs` - Interactive API documentation
- `GET /redoc` - Alternative API documentation

## Troubleshooting

### Common Issues

1. **Port already in use**

   ```bash
   # Change the port in docker-compose.yml or stop conflicting services
   docker compose down
   ```

2. **Database connection issues**

   ```bash
   # Check if PostgreSQL is running
   docker compose ps

   # View database logs
   docker compose logs db
   ```

3. **Migration issues**

   ```bash
   # Reset database (⚠️ will lose data)
   docker compose down -v
   docker compose up db
   docker compose exec app uv run alembic upgrade head
   ```

4. **UV cache permission errors**

   ```bash
   # If you see "Permission denied" errors with UV cache:
   docker compose down
   docker compose build --no-cache
   docker compose up
   ```

5. **PostgreSQL "trust" authentication warning**
   ```bash
   # This warning is normal and safe in Docker containers:
   # "initdb: warning: enabling "trust" authentication for local connections"
   # It only affects local connections within the container
   ```

### Development Tips

- Use `docker-compose.dev.yml` for development with hot reload
- Monitor logs with `docker-compose logs -f`
- Use `docker-compose exec app bash` to access the container shell
- Database data persists in Docker volumes between restarts

## Contributing

1. Fork the repository
2. Create a feature branch
3. Make changes and test locally
4. Submit a pull request

## License

[Your License Here]
