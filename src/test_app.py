import unittest
from unittest.mock import patch
from io import StringIO
import sys
import os
sys.path.append(os.path.dirname(os.path.abspath(__file__)) + "/..") 
from utils.model_utils import load_qa_model

class TestStreamlitApp(unittest.TestCase):
    @patch('streamlit.title')
    @patch('streamlit.text_area')
    @patch('streamlit.text_input')
    @patch('streamlit.button')
    @patch('streamlit.write')
    def test_streamlit_app(self, mock_write, mock_button, mock_text_input, mock_text_area, mock_title):
        # Prepare mock inputs
        mock_title.return_value = None
        mock_text_area.return_value = "Context goes here..."
        mock_text_input.return_value = "What is the answer?"
        mock_button.return_value = True

        # Load the question answering model
        qa_pipeline = load_qa_model()

        # Simulate button click
        with patch('sys.stdout', new=StringIO()) as fake_out:
            qa_pipeline.return_value = {'answer': 'RoBERTa is a type of language model.'}
            exec(open("app.py").read())
            self.assertIn("RoBERTa is a type of language model.", fake_out.getvalue())

if __name__ == '__main__':
    unittest.main()
