# quick-news

## Backend
* Python 2.7
* Flask==0.10.1: API server
* pyteaser==2.0: Text summarization library
* feedparser: Fetching and parsing through feed

## Frontend
* Angular.js scaffolded using [yo angular generator](https://github.com/yeoman/generator-angular)

## [DEMO](http://quicknews.amanuppal.ca/)

## Install
* Clone this repository
* `pip install pyteaser`
* `pip install flask`
* `pip install feedparser`
* `npm install`
* `bower install`

## Development & Build

### Backend
* `cd services` to go to services directory
* `python -u news_fetcher.py | tee news_fetcher.log` to start news caching service
* `python api_server.py` to start the Flask API server

### Frontend 
* Run `grunt` for building and `grunt serve` for preview

## Testing
* Running `grunt test` will run the unit tests for Angular with karma
