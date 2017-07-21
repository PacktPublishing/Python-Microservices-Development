
build:
	cd ..; docker build -t runnerly/tokendealer -f docker/Dockerfile .

run:
	docker run -v /tmp/logs:/logs -p 8080:8080 -it runnerly/tokendealer
