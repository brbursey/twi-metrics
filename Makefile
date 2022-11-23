.PHONY: shell test rebuild

rebuild:
	@echo "Rebuilding local docker-compose images..."
	docker-compose kill
	docker-compose rm -f web
	docker-compose build --no-cache --force-rm web

run:
	make rebuild
	docker compose up

shell:
	docker-compose run --rm web bash

test:
	docker-compose run --rm web pytest