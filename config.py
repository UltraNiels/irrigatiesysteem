import yaml

def load():
	with open('config.yaml', 'r') as cf:
		return yaml.load(cf, Loader=yaml.FullLoader)

def write(c):
	with open('config.yaml', 'w') as cf:
		return yaml.dump(c, cf)

def loaddata():
	with open('data.yaml', 'r') as df:
		return yaml.load(df, Loader=yaml.FullLoader)

def writedata(d):
	with open('config.yaml', 'w') as df:
		return yaml.dump(d, df)