"""
LLM Service
"""
from src.services.llm import LLM


class LLMService:
    """
    This class runs the prediction and returns the response.

    :Author: Pranay Chandekar
    """

    @staticmethod
    def get_response(text: str):
        """
        This method performs the prediction and prepares the response.

        :param text: The user query for LLM.
        :type text: str
        :return: The response from the LLM.
        :rtype: dict
        """

        response = {"response": LLM().get_instance().predict(text)}

        return response
