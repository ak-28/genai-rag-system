import ollama


MODEL_NAME = "phi3"



def generate_response(prompt: str):
    """
    Generate response using Ollama.
    """

    response = ollama.chat(
        model=MODEL_NAME,
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ]
    )

    return response["message"]["content"]