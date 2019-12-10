all:
	npm run css-build
	rm -rf demo/plugins
	git clone --jobs 8 --recurse-submodules=i18n_subsites --shallow-submodules https://github.com/getpelican/pelican-plugins.git demo/plugins
	cd demo && make html
