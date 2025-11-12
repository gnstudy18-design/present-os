import requests
from bs4 import BeautifulSoup

def search_web(query):
    if not query:
        return "Please specify what to search."
    url = f"https://www.google.com/search?q={query}"
    try:
        headers = {"User-Agent": "Mozilla/5.0"}
        res = requests.get(url, headers=headers)
        soup = BeautifulSoup(res.text, "html.parser")
        results = [a.text for a in soup.select("h3")[:5]]
        return "🔎 Top results:\n" + "\n".join(f"• {r}" for r in results)
    except Exception as e:
        return f"❌ Error fetching results: {e}"
