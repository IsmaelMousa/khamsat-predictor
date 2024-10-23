help h:
	@echo "Available Commands:"
	@sed -n "/^[a-zA-Z0-9_.]*:/s/:.*//p" < Makefile | GREP_COLOR="01;34" grep --color=always -E "^[a-zA-Z0-9_.]*"

setup:
	@echo "\e[34m=========================== Setup ===========================\e[0m"
	@pip install .

scrap:
	@echo "\e[1;32m=========================== Scraping ===========================\e[0m"
	@python3 ./data/scraper.py
	@echo "\e[1;32m=========================== Completed Successfully! ===========================\e[0m"