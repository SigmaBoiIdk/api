// File: /api/track.js

export default async function handler(req, res) {
  try {
    // Grab visitor info
    const ip =
      req.headers["x-forwarded-for"]?.split(",")[0] || req.socket.remoteAddress;
    const userAgent = req.headers["user-agent"];
    const time = new Date().toISOString();

    // Build Discord message
    const message = {
      content: `🟢 New visit:
- IP: ${ip}
- User-Agent: ${userAgent}
- Time: ${time}`,
    };

    // Direct webhook URL (hardcoded)
    await fetch("https://discord.com/api/webhooks/1412081122048741426/NWsChKO7PqLPxXKhjG0j6gyqzFQOv1Wvby8soi0UGKHkQjkF_6bMGvB3sn6iVsudusVg", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify(message),
    });

    // Redirect visitor
    res.writeHead(302, { Location: "https://vaultcord.win/silkwareverify" });
    res.end();
  } catch (err) {
    console.error("Error in /api/track:", err);
    res.status(500).send("Internal Server Error");
  }
}
