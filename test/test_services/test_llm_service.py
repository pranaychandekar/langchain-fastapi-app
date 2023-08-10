"""
llm_service.py test cases
 
Author - Pranay Chandekar
"""
import logging

import unittest
from unittest.mock import patch, Mock

from src.services.llm_service import LLMService


class TestPredictionService(unittest.TestCase):
    logging.basicConfig(level=logging.FATAL)

    @patch("src.services.llm_service.Logger")
    @patch("src.services.llm_service.PredictionService")
    def test_response(self, mock_prediction_service, mock_logger):
        mock_prediction_service.predict_label.return_value = "knives", 86.64
        mock_logger.get_instance.return_value = logging

        text = "Don't let the knives sink :P"
        result = LLMService.get_response(text)
        self.assertEqual(type(result.get("label")), str)

    @patch("src.services.llm_service.Logger")
    @patch("src.services.llm_service.Classifier")
    def test_predict_label(self, mock_classifier, mock_logger):
        mock_classifier = Mock()

        mock_logger.get_instance.return_value = logging

        text = "Don't let the knives sink :P"
        label, confidence = LLMService.predict_label(text)

        self.assertEqual(type(label), str)
        self.assertEqual(type(confidence), float)

