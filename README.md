# TabNews Scraper

![General project architecture focusing on the scraper](assets/tabnews-scraper-archtecture.png){:width="300px" height="200px"}



## Overview

TabNews Scraper is a Python project designed to scrape data from the TabNews page. The scraper periodically collects information from the page, ensuring that only new data is fetched and then sends it to a message queue.

The idea behind the TabNews project was to foster the development community in Brazil, and I found no better place to apply my studies.

You can access TabNews at https://www.tabnews.com.br/

## Features

- Scrapes data from the TabNews page.
- Periodically checks for new data to avoid duplication.
- Sends scraped data to a message queue for further processing.

## To Do:
- [ ] Create a basic scraper for the recent publications page.
- [ ] Write tests for the scraper.
- [ ] Create integration with a real message queue service.
- [ ] Implement logic to scraping at intervals (avoiding duplicates).


## Requirements

- Python 3.x
- Message queue system TBD (e.g., RabbitMQ, Apache Kafka)

## Running the Project

Make sure you have Docker installed on your system.

```bash
# Build docker image
make build-image

# Run docker container
make run-container

# Install dependencies locally
make install

# Run the project locally
make run