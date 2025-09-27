-include .env
export

# Local development
run-old:
	python3 -m uvicorn api.app.main:app --host 0.0.0.0 --port 8000 --reload
run:
	uv run uvicorn api.app.main:app --port 8000 --reload
compose:
	docker compose -f docker-compose.yml -f docker-compose.dev.yml up --build
# Database migrations
alembic-rev:
	uv run alembic revision --autogenerate -m "$(m)"
alembic-upgrade:
	uv run alembic upgrade head
alembic-downgrade:
	uv run alembic downgrade -1

# Docker commands
docker-build:
	docker compose build
docker-dev:
	docker compose --env-file .env -f docker-compose.yml -f docker-compose.dev.yml up --build
docker-prod:
	docker compose --env-file .env up --build -d
docker-stop:
	docker compose down
docker-clean:
	docker compose down -v
docker-logs:
	docker compose logs -f
docker-shell:
	docker compose exec app bash
docker-db:
	docker compose exec db psql -U ${POSTGRES_USER} -d ${POSTGRES_DB}

# Docker migrations
docker-migrate:
	docker compose exec app uv run alembic upgrade head
docker-migrate-rev:
	docker compose exec app uv run alembic revision --autogenerate -m "$(m)"

# Redis commands
docker-redis:
	docker compose exec redis redis-cli