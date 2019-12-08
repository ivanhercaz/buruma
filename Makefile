help:
	@echo "Makefile to ease the translation process"
	@echo "Usage:"
	@echo "      make extract			Extract message strings."
	@echo "      make init lang=LANG_CODE		Create catalog (po file)."
	@echo "      make update			Extract and update po files."
	@echo "      make compile			Compile po files to mo files."

extract:
	pybabel extract --mapping babel.cfg --output translations/messages.pot ./

init:
	pybabel init --input-file translations/messages.pot --output-dir translations/ --locale $(lang) --domain messages

update:
	pybabel update --input-file translations/messages.pot --output-dir translations/ --domain messages

compile:
	pybabel compile --directory translations/ --domain messages

deploy:
	npm run css-build
	rm -rf docs/plugins
	git clone --jobs 8 --recurse-submodules=i18n_subsites --shallow-submodules https://github.com/getpelican/pelican-plugins.git docs/plugins
	cd docs && make html
