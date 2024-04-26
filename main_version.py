import json 

class JSONDataManagment(object):
  def __init__(self, json_file_path):
    self.json_file_path = json_file_path
    self.current_data = self.get_data()

  def get_data(self) -> dict:
    with open(file = self.json_file_path, mode = 'r', encoding='utf-8') as jsf:
      return json.load(jsf)

  def load_data(self, data:dict|list) -> dict:
    with open(file = self.json_file_path, mode = 'w', encoding='utf-8') as f:
      data = f.write(json.dumps(data, indent=4))
    self.current_data = self.get_data()
    return True

  def add_data(self, some_data:dict|list) -> dict:
    self.current_data.update(some_data)
    self.load_data(self.current_data)
    return self.current_data
          
  def update_data(self, key:str|list, value:any) -> dict:
    find_data = None
    if isinstance(key, list):
      for index, i in enumerate(key):
        if len(key) == index + 1:
          try:
            find_data[i] = value
          except TypeError:
            print("Wrong path")
            return
        else:
          try:
            find_data = self.current_data[i] if not find_data else find_data[i]
          except:
            print("Wrong path")
            return
    elif isinstance(key, str):
      if key in self.current_data:
        self.current_data[key] = value
    self.load_data(self.current_data)
    return self.current_data

  def get_path(self):
    return self.json_file_path

  def get_value(self, key:str|list):
    find_data = None
    if isinstance(key, list):
      for index, i in enumerate(key):
        if len(key) == index + 1:
          try:
            find_data[i]
            return find_data[i]
          except:
            print("Wrong path.")
            return None
        else:
          try:
            find_data = self.current_data[i] if not find_data else find_data[i]
          except:
            print("Wrong path.")
            return None
    elif isinstance(key, str):
      if key in self.current_data:
        return self.current_data[key]
      else:
        print(f"The \"{key}\" was not found.")
        return None

  def __len__(self):
    return len(self.current_data)

  def __add__(self, value:dict):
    if isinstance(value, dict):
      self.add_data(value)
      return self.current_data
    else:
      print(f"\"{value}\" is not the dict.")
  
  def __sub__(self, key:str|list):
    find_data = None
    if isinstance(key, str):
      if key in self.current_data:
        self.current_data.pop(key)
        self.load_data(self.current_data)
        return self.current_data
      else:
        return False
    elif isinstance(key, list):
      for index, i in enumerate(key):
        if len(key) == index + 1:
          try:
            find_data.pop(i)
            self.load_data(self.current_data)
            return self.current_data
          except:
            print("Wrong path.")
            return False
        else:
          try:
            find_data = self.current_data[i] if not find_data else find_data[i]
          except:
            print("Wrong path.")
            return False
    
config = JSONDataManagment('config.json')

print(config + ['d','dsa','dasd'])




