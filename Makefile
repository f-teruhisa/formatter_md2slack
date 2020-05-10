default:up

init:
	docker-compose build

up:
	docker-compose up

lint:
	docker-compose run app pylint main.py test_main.py

test:
	docker-compose run app pytest test_main.py