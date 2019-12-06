all:
	npm run css-build
	pip install pelican[Markdown]
	cd demo && make html
