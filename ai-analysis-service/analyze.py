from openai import OpenAI
from dotenv import load_dotenv
import os
import psutil

load_dotenv()

client = OpenAI(
    base_url="https://openrouter.ai/api/v1",
    api_key=os.getenv("OPENROUTER_API_KEY")
)

# REAL live metrics
cpu = psutil.cpu_percent(interval=1)
memory = psutil.virtual_memory().percent
disk = psutil.disk_usage('/').percent

prompt = f"""
You are an AI infrastructure monitoring assistant.

Analyze these live system metrics:

CPU Usage: {cpu}%
Memory Usage: {memory}%
Disk Usage: {disk}%

Return:
1. Severity
2. Possible issue
3. Recommended action
"""

response = client.chat.completions.create(
    model="openai/gpt-3.5-turbo",
    messages=[
        {"role": "user", "content": prompt}
    ]
)

analysis = response.choices[0].message.content
with open("logs/ai_analysis.log", "w", encoding="utf-8") as log:
    log.write(analysis)

print("\nAI Infrastructure Analysis")
print("----------------------------")
print(analysis)