main:
	python main.py
	
# testes

test:
	clear
	pytest -v

coverage:
	pytest --cov=github-monitor tests/
	pytest --cov=github-monitor --cov-report html tests/

coverage-console:
	clear
	pytest --cov=github-monitor tests/

	

