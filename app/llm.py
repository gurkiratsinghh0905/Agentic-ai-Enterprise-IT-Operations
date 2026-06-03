import os
from dotenv import load_dotenv
from huggingface_hub import InferenceClient

load_dotenv()

client = InferenceClient(api_key=os.getenv("HF_TOKEN"))

DEFAULT_SYSTEM = "You are an expert Enterprise IT support assistant. Be concise and precise."


def invoke(
    prompt: str,
    system_prompt: str = DEFAULT_SYSTEM,
    max_tokens: int = 1024
) -> str:
    messages = [
        {"role": "system", "content": system_prompt},
        {"role": "user",   "content": prompt}
    ]
    try:
        response = client.chat.completions.create(
            model="meta-llama/Llama-3.1-8B-Instruct",
            messages=messages,
            max_tokens=max_tokens,
        )
        return response.choices[0].message.content
    except Exception as e:
        return f"LLM_ERROR: {str(e)}"
