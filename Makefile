SHELL = /bin/sh

.PHONY = all

all: guard-DIR
	nodemon -w $(DIR) -e py --exec "python $(DIR)"

guard-%:
	@if [ -z '${${*}}' ]; then echo "ERROR: variable $* not set" && exit 1; fi
