import yaml

def  load_yaml(filepath):
  with open(filepath, 'r') as file_descriptor:
    data = yam.load(file_descriptor)
  return data

def write_yaml(filepath, data):
  with open(filepath, 'w') as file_descriptor:
    yaml.dump(data, file_descriptor)
  