from typing import List
from pydantic import BaseModel


###############################################################################
# Submodels
###############################################################################


class Metadata(BaseModel):
    algorithm: str
    components: int
    params: dict
    start_datetime: str
    end_datetime: str
    seconds_elapsed: int


###############################################################################
# Models
###############################################################################


class ReductionBaseModel(BaseModel):
    id: str
    metadata: Metadata


class ReductionModel(BaseModel):
    metadata: Metadata
    reduction: List[List[float]]
    labels: List[str]
