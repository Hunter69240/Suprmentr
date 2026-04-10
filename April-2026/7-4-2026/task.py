import json
import os
import urllib.error
import urllib.request

API_KEY = os.getenv("OPENAI_API_KEY")
API_URL = "https://api.openai.com/v1/chat/completions"
MODEL = "gpt-4o-mini"
def call_ai(prompt: str) -> str:
	payload = {
		"model": MODEL,
		"messages": [{"role": "user", "content": prompt}],
	}
	req = urllib.request.Request(
		API_URL,
		data=json.dumps(payload).encode("utf-8"),
		headers={
			"Content-Type": "application/json",
			"Authorization": f"Bearer {API_KEY}",
		},
		method="POST",
	)
	with urllib.request.urlopen(req, timeout=30) as response:
		body = json.loads(response.read().decode("utf-8"))
		return body["choices"][0]["message"]["content"]
if __name__ == "__main__":
	if not API_KEY:
		print("Set OPENAI_API_KEY first, then run again.")
	else:
		user_prompt = input("Enter prompt: ").strip() or "Tell me one fun fact"
		try:
			result = call_ai(user_prompt)
			print("\nAI Response:\n")
			print(result)
		except urllib.error.HTTPError as e:
			print(f"HTTP error: {e.code} - {e.read().decode('utf-8', errors='ignore')}")
		except Exception as e:
			print(f"Error: {e}")