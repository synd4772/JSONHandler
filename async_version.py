import aiofiles
import asyncio
import json 

class DataManagment(object):
  def __init__(self, json_file_path):
    self.json_file_path = json_file_path

  async def get_data(self) -> dict:
    async with aiofiles.open(file = self.json_file_path, mode = 'r', encoding='utf-8') as jsf:
      data = await jsf.read()
      return json.loads(data)

  async def load_data(self, data:dict|list) -> dict:
    async with aiofiles.open(file = self.json_file_path, mode = 'w', encoding='utf-8') as f:
      data = await f.write(json.dumps(data, indent=4))
      return data

  async def add_data(self, some_data:dict|list) -> dict:
    current_data:dict = await self.get_data()
    new_data:dict = current_data.update(some_data)
    await self.load_data(current_data)
    return new_data
          
  async def update_data(self, key:str|list, value:any) -> dict:
    current_data:dict = await self.get_data()
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
            find_data = current_data[i] if not find_data else find_data[i]
          except KeyError:
            print("Wrong path")
            return
    await self.load_data(current_data)
    return current_data

  async def get_path(self):
    return self.json_file_path
  

config = DataManagment('config.json')

print(asyncio.run(config.get_data()))




