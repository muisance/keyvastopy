deps:
	python3 -m pip install --upgrade pip
	python3 -m pip install -r requirements

run_app:
	python3 src/app/storage.py -l

run_api:
	python3 src/api/api.py