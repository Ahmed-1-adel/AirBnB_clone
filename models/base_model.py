#!/usr/bin/python3
"""Defines the BaseModel class.
  And Main Varables
"""
import uuid , datetime, sys , models
dateTime = datetime.datetime
class BaseModel() :
    """This Class To Defines all Common Attribute & Methods for other classes"""
    def __init__(self, *args, **kwargs):
        """Initizlize a New BasedModel
        
        Args:
            *args (any): Unused.
            **kwargs (dict): Key/value pairs of attributes.
        """
        newData = "%Y-%m-%dT%H:%M:%S.%f"
        self.id = str(uuid.uuid4())
        self.created_at = dateTime.now()
        self.updated_at = dateTime.now()
        if len(kwargs) != 0:
            for key, value in kwargs.items():
                if key == "created_at" or value == "updated_at":
                    self.__dict__[key] = dateTime.strptime(value, newData)
                else :
                    self.__dict__[key] = value
        else:
            models.storage.new(self)
    def safe(self):
        self.updated_at = dateTime.today()
        models.storage.save()
    def to_dict(self):
        """Return the dictionary of the BaseModel instance.

        Includes the key/value pair __class__ representing
        the class name of the object.
        """
        rdict = self.__dict__.copy()
        rdict["created_at"] = self.created_at.isoformat()
        rdict["updated_at"] = self.updated_at.isoformat()
        rdict["__class__"] = self.__class__.__name__
        return rdict
    def __str__(self):
      """Return the print/str representation of the BaseModel instance."""
      clName = self.__class__.__name__
      return ("[{}] ({}) {}".format(clName, self.id, self.__dict__))
