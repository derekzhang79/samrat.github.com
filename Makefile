build:
	pelican -s settings.py raw
upload:
	build
	git push origin master
