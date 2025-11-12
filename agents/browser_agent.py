import requests

def search_web(query):
    try:
        url = f"https://api.duckduckgo.com/?q={query}&format=json&no_redirect=1"
        headers = {"User-Agent": "Mozilla/5.0"}
        res = requests.get(url, headers=headers).json()

        results = []

        # Add Abstract if available
        if res.get("AbstractText"):
            results.append(f"- {res['AbstractText']}")

        # Add related topics
        if "RelatedTopics" in res:
            for item in res["RelatedTopics"][:5]:
                if isinstance(item, dict) and "Text" in item and "FirstURL" in item:
                    results.append(f"- [{item['Text']}]({item['FirstURL']})")

        if not results:
            return f"❌ No results found for '{query}'."

        return f"🔎 Top results for '{query}':\n" + "\n".join(results)

    except Exception as e:
        return f"❌ Web search failed: {e}"
