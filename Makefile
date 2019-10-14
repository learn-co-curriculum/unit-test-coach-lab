tests:
	jupyter nbconvert --to script example_index.ipynb
	python3 -m pytest --disable-pytest-warnings -v

example1:
	jupyter nbconvert --to script example_index.ipynb
	python3 -m pytest --disable-pytest-warnings -v -m example_1

example2:
	jupyter nbconvert --to script example_index.ipynb
	python3 -m pytest --disable-pytest-warnings -v -m example_2
