"""
Classifier Singleton
"""
from langchain.llms import GPT4All

from src.domain.constants import MODEL_PATH
from src.configurations.app_configs import AppConfigs
from src.utils.logging_util import Logger
from src.utils.singleton import Singleton


class LLM(metaclass=Singleton):
    """
    This class is a singleton which returns the instance of the Classifier.

    :Author: Pranay Chandekar
    """

    def __init__(self):
        """
        This method initializes the instance of the Classifier.
        """
        # Step 01: Load the model path from the configurations.
        _model_path = AppConfigs().get_instance().get(MODEL_PATH)

        # Step 02: Load the model.
        self._model = GPT4All(
            model=_model_path,
            max_tokens=2048,
        )

        Logger().get_instance().info(
            "Finished loading the LLM: %s", self.get_instance()
        )

    def get_instance(self):
        """
        This method returns the Classifier instance.

        :return: Classifier instance
        """
        return self._model
