import yaml

path = './'

def  load_yaml(filename):
  filename = str(path + filename)
  with open(filename, 'r') as file_descriptor:
    data = yam.load(file_descriptor)
  return data

def write_yaml(filename, data):
  filename = str(path + filename)
  with open(filename, 'w') as file_descriptor:
    yaml.dump(data, file_descriptor)
  