from transformers import pipeline, AutoTokenizer, AutoModelForQuestionAnswering

def load_qa_model():
    """
    Loads the question answering model from HuggingFace.
    """
    # Load the tokenizer and model for question answering
    tokenizer = AutoTokenizer.from_pretrained("deepset/roberta-base-squad2")
    model = AutoModelForQuestionAnswering.from_pretrained("deepset/roberta-base-squad2")
    qa_pipeline = pipeline("question-answering", model=model, tokenizer=tokenizer)
    return qa_pipeline
