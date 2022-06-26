install:
	poetry install

lint:
	poetry run flake8 gendiff

test:
	poetry run pytest -s
	poetry run pytest --cov=gendiff

test-coverage:
	poetry run pytest --cov=gendiff --cov-report xml

build:
	poetry build

publish:
	poetry publish --dry-run

package-install:
	python3 -m pip install --user dist/*.whl

package-force-reinstall:
	python3 -m pip install --user --force-reinstall dist/*.whl

fast-check:
	echo "\n\n\n ! Build process...\n"
	make build
	echo "\n\n\n ! Package-force-reinstall process...\n"
	make package-force-reinstall
	echo "\n\n\n ! Lint checkup process...\n"
	make lint
	echo "\n\n\n ! Test checkup process...\n"
	make test
