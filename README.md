# twitter-client-py

Experimental project for building Twitter client

## Requirements

- Docker

## Quickstart

Set following sensitive values issued by Twitter to your environment:
- `CONSUMER_KEY` (API key)
- `CONSUMER_SECRET` (API secret)
- `ACCESS_TOKEN` (Access token)
- `ACCESS_TOKEN_SECRET` (Access token secret)

Then run Docker container:
```bash
ocker run -e CONSUMER_KEY=$CONSUMER_KEY -e CONSUMER_SECRET=$CONSUMER_SECRET -e ACCESS_TOKEN=$ACCESS_TOKEN -e ACCESS_TOKEN_SECRET=$ACCESS_TOKEN_SECRET -p 5000:5000 rindrics/twitter-client-py
```


## For developers

Requirements:
- [Poetry](https://python-poetry.org)

