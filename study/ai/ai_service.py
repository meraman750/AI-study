from openai import OpenAI
from django.conf import settings
from .prompts import SUMMARY_PROMPT, QUIZ_PROMPT, CHAT_PROMPT
import json
import re

client = OpenAIclient = OpenAI(
    base_url="https://models.github.ai/inference",
    api_key=settings.GITHUB_TOKEN,
)

MODEL_NAME = "openai/gpt-4o"

class AIService:
    def clean_markdown(text):
        text = re.sub(r'#+ ', '', text)  # remove headings
        text = re.sub(r'\*\*(.*?)\*\*', r'\1', text)  # bold
        text = re.sub(r'\\\[|\\\]', '', text)  # remove latex brackets
        return text.strip()

    @staticmethod
    def ask_ai(messages, stream=False):

        response = client.chat.completions.create(
            model=MODEL_NAME,
            messages=messages,
            temperature=0.7,
            max_tokens=1000,
            stream=stream,
        )

        if stream:
            return response

        return response.choices[0].message.content

    # SUMMARY
    @staticmethod
    def generate_summary(text):

        messages = [
            {"role": "system", "content": "You are an expert tutor."},
            {"role": "user", "content": SUMMARY_PROMPT.format(text=text)},
        ]
        summary = AIService.ask_ai(messages)
        return AIService.clean_markdown(summary)

    # QUIZ
    @staticmethod
    def generate_quiz(text, difficulty="medium"):

        messages = [
            {"role": "system", "content": "You generate structured quizzes."},
            {
                "role": "user",
                "content": QUIZ_PROMPT.format(
                    text=text,
                    difficulty=difficulty
                ),
            },
        ]

        raw_response = AIService.ask_ai(messages)

        cleaned = re.sub(r"```json|```", "", raw_response).strip()

        try:
            return json.loads(cleaned)
        except json.JSONDecodeError:
            return {"error": "Invalid JSON from AI", "raw": cleaned}

    # CHAT
    # @staticmethod
    # def chat(question, context):

    #     messages = [
    #         {"role": "system",
    #          "content": "Answer only using provided study material."},
    #         {
    #             "role": "user",
    #             "content": CHAT_PROMPT.format(
    #                 question=question,
    #                 context=context
    #             ),
    #         },
    #     ]

    #     return AIService.ask_ai(messages)