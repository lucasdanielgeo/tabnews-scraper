build-image:
	sudo docker build -t tabnews-scraper .

run-container:
	sudo docker run tabnews-scraper 

install:
	pip install -r requirements.txt

run:
	python ./main.py