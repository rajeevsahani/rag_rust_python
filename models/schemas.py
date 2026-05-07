from pydantic import BaseModel
from typing import List, Union
from logs import logger

class TextInput(BaseModel):
    text: Union[str, List[str]]