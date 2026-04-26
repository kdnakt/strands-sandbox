import json
import urllib.request

from strands import Agent, tool


@tool
def wikipedia_on_this_day(month: int, day: int) -> str:
    """Wikipedia英語版の「On this day」フィードを取得する。

    Args:
        month: 月 (1-12)
        day: 日 (1-31)

    Returns:
        その日に起きた歴史上の主要な出来事を含むJSON文字列。
    """
    url = f"https://api.wikimedia.org/feed/v1/wikipedia/en/onthisday/selected/{month:02d}/{day:02d}"
    req = urllib.request.Request(
        url,
        headers={"User-Agent": "strands-sandbox-timely"},
    )
    with urllib.request.urlopen(req, timeout=30) as resp:
        data = json.loads(resp.read())
    return json.dumps(data, ensure_ascii=False)


agent = Agent(
    model="us.amazon.nova-micro-v1:0",
    callback_handler=None,
    system_prompt="あなたはユーザーの質問に親切に答えるエージェントです。",
    tools=[wikipedia_on_this_day],
)

print(agent("今日は何日？そして今日歴史上どんな出来事があった？"))
