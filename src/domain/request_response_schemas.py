"""
Request Schemas
"""
from pydantic import BaseModel, Field


class BuildResponse(BaseModel):
    """
    Build Response Schema
    """

    service: str = Field(..., example="langchain-fastapi-app")
    version: str = Field(..., example="1.0.0")
    author: str = Field(..., example="Pranay Chandekar")
    linkedIn: str = Field(..., example="https://www.linkedin.com/in/pranaychandekar/")
    message: str = Field(..., example="The web service is up and running!")


class LLMRequest(BaseModel):
    """
    LLM Request Schema
    """

    source: str = Field(..., min_length=1, example="swagger")
    text: str = Field(..., min_length=1, example="Tell me a joke")


class LLMResponse(BaseModel):
    """
    LLM Response Schema
    """

    response: str = Field(..., example="Random Joke!'")
