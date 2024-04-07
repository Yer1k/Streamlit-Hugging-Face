import unittest
from utils.model_utils import load_qa_model

class TestModelUtils(unittest.TestCase):
    def test_load_qa_model(self):
        # Test if the model is loaded successfully
        qa_pipeline = load_qa_model()
        self.assertIsNotNone(qa_pipeline)
        
        # Test if the loaded model is of the correct type
        self.assertTrue(hasattr(qa_pipeline, '__call__'))
        
        # Test if the loaded model can answer a basic question
        context = "Streamlit is a Python library that allows you to create web apps using only Python scripts."
        question = "What is Streamlit?"
        answer = qa_pipeline(question=question, context=context)
        self.assertEqual(answer['answer'], "a Python library that allows you to create web apps using only Python scripts")

        # Test if the loaded model can handle longer contexts
        context_long = "Streamlit is a Python library that allows you to create web apps using only Python scripts. It is designed to make the process of building and sharing data-driven web applications quick and easy. With Streamlit, you can create interactive dashboards, visualize data, and prototype machine learning models without needing to write HTML, CSS, or JavaScript."
        question_long = "What can you do with Streamlit?"
        answer_long = qa_pipeline(question=question_long, context=context_long)
        self.assertIn(answer_long['answer'], ["create interactive dashboards, visualize data, and prototype machine learning models"])

if __name__ == '__main__':
    unittest.main()
