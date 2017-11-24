.PHONY: init style lint

init:
	pip install --upgrade -r requirements.txt

style:
	pycodestyle --show-source --show-pep8 .

lint:
	pylint --rcfile=.pylintrc --reports=n *.py

ci: style lint
