from pydantic import BaseModel
from typing import Optional

class Solutions(BaseModel):
    solutionId:Optional[int] = None
    solutionName:str
    solutionDescription:str
    industry_Id:int