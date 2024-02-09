""" Defines the BaseModel class.
    And Main Varables
"""
import json
from models.base_model import BaseModel
class FileStorage():
    
    """ Initizlize a an abstracted storage engine
        Attribute:
            __file_path (str) : The Name of file to save objects to
            __objects (dict) : The Empty dict, but will store all objects by <class name>.id
    """
    __file_path = 'file.json'
    __objects  = {}
    def all(self): 
        """Returns the dictionary __objects"""
        objFileStorage = FileStorage.__objects
        return objFileStorage
    
    def new(self, obj):
        """Set in __objects obj with key <obj_class_name>.id"""
        objName = obj.__class__.__name__
        FileStorage.__objects["{}.{}".format(objName, obj.id)] = obj

    def save(self):
        """Serialize __objects to the JSON file __file_path."""
        objFileStorage = FileStorage.__objects
        objDict = {obj: objFileStorage[obj].to_dict() for obj in objFileStorage.keys()}
        with open(FileStorage.__file_path, "w") as file:
            json.dump(objDict, file)
    def reload(self):
        """Deserialize JSON  file __file_path. to __objects if it exists."""
        try:
            with open(FileStorage.__file_path) as file:
                objDict = json.load(file)
                for obj in objDict.values():
                    clsName = obj["__class__"]
                    del obj["__class__"]
                    self.new(eval(clsName)(**obj))
        except FileNotFoundError:
            return