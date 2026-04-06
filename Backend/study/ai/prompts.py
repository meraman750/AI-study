SUMMARY_PROMPT = """
    You are an expert tutor.

    Summarize the following study material:
    - clear
    - medium text size
    - simple explanations
    - highlight key formulas or concepts

    TEXT:
    {text}
"""


QUIZ_PROMPT = """
    Create a {difficulty} level quiz.

    Return JSON format exactly like this:

    [
        {{
            "question": "",
            "options": ["A","B","C","D"],
            "answer": ""
        }}
    ]

    Material:
    {text}
"""


# CHAT_PROMPT = """
#     You are a helpful study assistant.

#     Use ONLY the provided context to answer.

#     Context:
#     {context}

#     Question:
#     {question}
# """