#!/usr/bin/env python

from time import sleep
from os import environ, getenv
from argparse import ArgumentParser, RawDescriptionHelpFormatter
from flask import Flask

def main():
	from waitress import serve
	print("Starting app2 version", version)
	print("Running with config", config)
	procedure1()
	procedure2()
	procedure3()
	serve(app, host="0.0.0.0", port=config["port"])

app = Flask(__name__)

@app.route('/')
def hello_world():
    return f'Rnning app2 version {version} with config {config}\n'

version = open('VERSION').read()

config = {
	"bat": "default bat value",
	"port": 8080,
}
parser = ArgumentParser(
	description=f"""
App2 does this well-defined thing.

required environment variables:

FOO - Cloud property, example: foo
BAR - User detail, example: bar
BAZ - Important knob, example: baz

optional environment variables:

PORT - Port to listen, default: {config["port"]}
BAT - Another important knob, default: {config["bat"]}
""",
	epilog="""
All configuration is loaded using environment variables.
There are no command-line options.
""",
	formatter_class=RawDescriptionHelpFormatter,
)

def load_config_from_environment():
	try:
		config["foo"] = environ["FOO"]
		config["bar"] = environ["BAR"]
		config["baz"] = environ["BAZ"]
	except KeyError as e:
		print("Missing required environment varible", e)
		parser.print_help()
		exit(1)

	config["bat"] = getenv("BAT", config["bat"])
	config["port"] = int(getenv("PORT", config["port"]))

def path1(foo):
	return f'{foo}/path1'

def path2(bar):
	return f'{bar}/path2'

def path3(baz):
	return f'{baz}/path3'

def config_path(path):
	return f'{path}/config.json'

def procedure1():
	print("Starting procedure 1")
	print("Looking in path", path1(config["foo"]))
	print("Finished procedure 1")

def procedure2():
	print("Starting procedure 2")
	print("Looking in path", path2(config["bar"]))
	print("Finished procedure 2")

def procedure3():
	print("Starting procedure 3")
	print("Looking in path", path3(config["bar"]))
	print("Finished procedure 3")

if __name__ == "__main__":
	parser.parse_args()
	load_config_from_environment()
	main()
