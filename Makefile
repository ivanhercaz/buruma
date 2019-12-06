all:
	npm run css-build
	pip3 install pelican[Markdown]
	cd demo && make html
