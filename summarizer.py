import requests

def run_llama(prompt: str, model: str = "llama3") -> str:
    """
    Runs a local LLM using Ollama and returns the response text.
    """

    url = "http://localhost:11434/api/generate"
    headers = {"Content-Type": "application/json"}
    payload = {
        "model": model,
        "prompt": prompt,
        "stream": False
    }
    try:
        response = requests.post(url, json=payload, headers=headers)
        if response.status_code == 200:
            data = response.json()
            return data.get("response", "")
        else:
            return f"❌ API Error {response.status_code}: {response.text}"
    except Exception as e:
        return f"❌ Exception: {str(e)}"
