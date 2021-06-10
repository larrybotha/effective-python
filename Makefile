SHELL = /bin/sh

.PHONY = all

all: guard-ITEM
	nodemon -w $(ITEM) -e py --exec "python $(ITEM)"

guard-%:
	@if [ -z '${${*}}' ]; then echo "ERROR: variable $* not set" && exit 1; fi
