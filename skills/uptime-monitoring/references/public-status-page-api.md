# Public Status Page API

## Public Status Page API

```javascript
// status-page-api.js
const express = require("express");
const router = express.Router();

router.get("/api/status", async (req, res) => {
  try {
    const endpoints = await db.query(`
      SELECT DISTINCT endpoint FROM uptime_checks
    `);

    const status = {
      page: { name: "My Service Status", updated_at: new Date().toISOString() },
      components: [],
    };

    for (const { endpoint } of endpoints) {
      const [lastCheck] = await db.query(
        `
        SELECT status FROM uptime_checks
        WHERE endpoint = ? ORDER BY timestamp DESC LIMIT 1
      `,
        [endpoint],
      );

      status.components.push({
        id: endpoint,
        name: endpoint,
        status: lastCheck?.status === "up" ? "operational" : "major_outage",
      });
    }

    const allUp = status.components.every((c) => c.status === "operational");
    status.status = {
      overall: allUp ? "all_operational" : "major_outage",
    };

    res.json(status);
  } catch (error) {
    res.status(500).json({ error: "Failed to fetch status" });
  }
});

router.get("/api/status/uptime/:endpoint", async (req, res) => {
  try {
    const stats = await db.query(
      `
      SELECT
        DATE(timestamp) as date,
        COUNT(*) as total,
        SUM(CASE WHEN status = 'up' THEN 1 ELSE 0 END) as uptime
      FROM uptime_checks
      WHERE endpoint = ? AND timestamp > DATE_SUB(NOW(), INTERVAL 30 DAY)
      GROUP BY DATE(timestamp)
      ORDER BY date DESC
    `,
      [req.params.endpoint],
    );

    res.json(stats);
  } catch (error) {
    res.status(500).json({ error: "Failed to fetch statistics" });
  }
});

module.exports = router;
```
