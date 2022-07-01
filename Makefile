.PHONY: run
run:
	poetry run python app.py


.PHONY: format
format:
	poetry run black .


.PHONY: docker
docker:
	docker build -t rindrics/twitter-client-py .
	docker push rindrics/twitter-client-py
	docker run -e CONSUMER_KEY=$CONSUMER_KEY \
	  -e CONSUMER_SECRET=$CONSUMER_SECRET \
	  -e ACCESS_TOKEN=$ACCESS_TOKEN \
	  -e ACCESS_TOKEN_SECRET=$ACCESS_TOKEN_SECRET \
	  -p 5000:5000 \
	  rindrics/twitter-client-py
