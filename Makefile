build:
		docker build -t hots .
run:
	docker run -it -v /Users/alai/Desktop/hotsstats:/app hots:latest /bin/bash
