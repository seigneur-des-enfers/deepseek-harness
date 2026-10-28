import os
import sys
import urllib.request
import json

def main():
    api_key = os.environ.get("DEEPSEEK_API_KEY")
    prompt = sys.argv[1] if len(sys.argv) > 1 else "Salutation de la Liche."
    
    if not api_key:
        print("Erreur : La clé secrète DEEPSEEK_API_KEY est introuvable.")
        sys.exit(1)

    print(f"Invocation de DeepSeek avec l'ordre : {prompt}")
    
    url = "https://api.deepseek.com/chat/completions"
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {api_key}"
    }
    
    data = {
        "model": "deepseek-chat",
        "messages": [
            {"role": "system", "content": "Tu es une Liche obéissant à ton Suzerain, le Seigneur des Enfers."},
            {"role": "user", "content": prompt}
        ],
        "stream": False
    }
    
    req = urllib.request.Request(url, data=json.dumps(data).encode('utf-8'), headers=headers, method='POST')
    
    try:
        with urllib.request.urlopen(req) as response:
            result = json.loads(response.read().decode('utf-8'))
            answer = result['choices'][0]['message']['content']
            print("\n--- RÉPONSE DE LA LICHE ---")
            print(answer)
            print("---------------------------\n")
    except Exception as e:
        print(f"Erreur lors de la communication avec le domaine de DeepSeek : {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()
