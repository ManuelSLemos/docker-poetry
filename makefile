docker-start:
	sudo service docker start

bash:
	docker run --rm \
	-v $(PWD):/app \
	-w /app \
	-it python:3.10 \
	bash

chown:
	sudo chown -R 1000:1000 .