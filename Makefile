build:
		docker build -t hots .
rundev:
	docker run -it -v /Users/alai/Desktop/hotsstats:/app hots:latest /bin/bashi

run: build
	docker run -t  hots:latest python app.py --directory=Replays
