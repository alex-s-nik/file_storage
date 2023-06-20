run:
	docker-compose up

test:
	docker-compose -rm backend pytest

migrate:
	docker-compose -rm backend alembic -c src/alembic.ini upgrade head