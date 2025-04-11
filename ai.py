import requests
from dotenv import load_dotenv
from typing import Optional
import json
import os

url = "http://127.0.0.1:7860/api/v1/run/22b705e0-6a0b-4b5b-91ce-1478237f16cf"
APPLICATION_TOKEN = os.getenv("LANGFLOW_TOKEN")

def ask_ai(
#files,
 	question
	):
    TWEAKS = {
	"ChatInput-boRGJ": {
		#"files": [
		#	files
		#],
	}
    }
    return run_flow(message=question, tweaks=TWEAKS, application_token=APPLICATION_TOKEN)

def run_flow(message: str,
  output_type: str = "chat",
  input_type: str = "chat",
  tweaks: Optional[dict] = None,
  application_token: Optional[str] = None) -> dict:
    payload = {
        "input_value": message,
        "output_type": output_type,
        "input_type": input_type,
    }
    headers = None
    if tweaks:
        payload["tweaks"] = tweaks
    if application_token:
        headers = {"Authorization": "Bearer " + application_token, "Content-Type": "application/json"}
    response = requests.post(url, json=payload, headers=headers)
    print(response.json())
    return (response.json()["outputs"][0]["outputs"][0]["outputs"]["message"]["message"])
