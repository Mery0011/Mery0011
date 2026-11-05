"""Render one original, date-selected thought in a compact lavender banner."""

from datetime import datetime
from html import escape
from pathlib import Path
from zoneinfo import ZoneInfo


QUOTES = (
    "Small steps, taken with care, become something beautiful.",
    "Let curiosity lead, and let patience do the building.",
    "A little progress is still a lovely place to begin.",
    "Build something useful. Leave a little kindness in it.",
    "Make room for learning, even on the imperfect days.",
    "Good things grow through small, thoughtful choices.",
    "There is beauty in making something work a little better.",
    "Your next idea deserves a small first step.",
    "Keep your standards thoughtful and your curiosity wide.",
    "One clear thought can become a thousand possibilities.",
    "Create with intention. Improve with patience.",
    "The details you care about become the work you love.",
    "A quiet hour of learning can open a new door.",
    "Start where you are. Build with what you know.",
    "Leave space for wonder between the lines of code.",
    "Thoughtful work begins with a thoughtful question.",
    "Let each small experiment teach you something new.",
    "You can grow slowly and still grow beautifully.",
    "A kind mind and a curious heart can build a lot.",
    "Make the next step simple enough to take today.",
    "Every useful thing began as an unfinished idea.",
    "Progress is often quieter than we expect.",
    "Build a little. Learn a little. Begin again tomorrow.",
    "Clarity is a small gift you can leave in your work.",
    "Your care for the details is part of your craft.",
    "Let the work reflect both your skill and your care.",
    "Stay curious about what you have yet to understand.",
    "A fresh question can be the beginning of better code.",
    "Make something today that yesterday could only imagine.",
    "There is room to be both ambitious and gentle.",
    "Keep building a world you would enjoy belonging to.",
)


def render_quote(day):
    quote = escape(QUOTES[(day - datetime(2026, 11, 6).date()).days % len(QUOTES)])
    return f'''<svg xmlns="http://www.w3.org/2000/svg" width="850" height="82" viewBox="0 0 850 82" role="img" aria-labelledby="title desc">
  <title id="title">A little thought for today</title>
  <desc id="desc">{quote}</desc>
  <metadata>Asia/Seoul date: {day.isoformat()}. Original thoughts, rotating daily.</metadata>
  <defs>
    <linearGradient id="lavender" x2="1" y2="0">
      <stop stop-color="#f1e8fb"/>
      <stop offset="1" stop-color="#fbf0f5"/>
    </linearGradient>
  </defs>
  <rect width="850" height="82" rx="8" fill="url(#lavender)"/>
  <text x="425" y="26" text-anchor="middle" font-family="Arial, sans-serif" font-size="11" letter-spacing="3" fill="#8c6c9f">A LITTLE THOUGHT FOR TODAY</text>
  <text x="425" y="57" text-anchor="middle" font-family="Georgia, 'Times New Roman', serif" font-style="italic" font-size="21" fill="#715184">{quote}</text>
</svg>
'''


if __name__ == "__main__":
    today = datetime.now(ZoneInfo("Asia/Seoul")).date()
    target = Path(__file__).resolve().parents[1] / "assets" / "daily-quote.svg"
    target.write_text(render_quote(today), encoding="utf-8")
