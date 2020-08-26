version := $(shell cat VERSION)

all: help

help:
	@cat README.md

tag:
	git tag -a $(version) -m 'version $(version)'

build:
	docker build \
		--tag=docker.pkg.github.com/egfast/app2/app2:latest \
		.
	docker tag \
		docker.pkg.github.com/egfast/app2/app2:latest \
		docker.pkg.github.com/egfast/app2/app2:$(version)

run:
	docker run \
		-it \
		-e FOO=foo \
		-e BAR=bar \
		-e BAZ=baz \
		-e PORT=8080 \
		-p 8080:8080 \
		docker.pkg.github.com/egfast/app2/app2

push:
	docker push docker.pkg.github.com/egfast/app2/app2
