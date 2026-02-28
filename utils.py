def generate_summary(text):
    sentences = text.split(".")
    return ". ".join(sentences[:2])

def extract_key_points(text):
    words = text.split()
    return list(set(words[:5]))

def generate_questions():
    return [
        "What is the main objective?",
        "What methodology is used?",
        "What are key findings?",
        "What are limitations?",
        "What is future scope?"
    ]