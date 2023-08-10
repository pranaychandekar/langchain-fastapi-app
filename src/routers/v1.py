"""
LLM Service End Point
"""
from fastapi.routing import APIRouter

from src.utils.logging_util import Logger, log_execution_time
from src.domain.request_response_schemas import (
    LLMRequest,
    LLMResponse,
)
from src.services.llm_service import LLMService

router = APIRouter()


@router.post("/predict", tags=["LLM Service"], response_model=LLMResponse)
@log_execution_time
async def get_response(request: LLMRequest):
    """
    This end point generates the response of an LLM for the user query.

    :param request: The request for the API.

    :return: The LLM response.
    """
    Logger().get_instance().info("Request: %s", request.json())
    return LLMService.get_response(request.text)
