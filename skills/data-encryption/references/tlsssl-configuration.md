# TLS/SSL Configuration

## TLS/SSL Configuration

```javascript
// tls-server.js - HTTPS server with strong TLS
const https = require("https");
const fs = require("fs");

const tlsOptions = {
  key: fs.readFileSync("private-key.pem"),
  cert: fs.readFileSync("certificate.pem"),
  ca: fs.readFileSync("ca-cert.pem"), // Certificate authority

  // TLS version restrictions
  minVersion: "TLSv1.2",
  maxVersion: "TLSv1.3",

  // Strong cipher suites
  ciphers: [
    "TLS_AES_256_GCM_SHA384",
    "TLS_CHACHA20_POLY1305_SHA256",
    "TLS_AES_128_GCM_SHA256",
    "ECDHE-RSA-AES256-GCM-SHA384",
    "ECDHE-RSA-AES128-GCM-SHA256",
  ].join(":"),

  // Prefer server cipher order
  honorCipherOrder: true,

  // Require client certificate (mutual TLS)
  requestCert: true,
  rejectUnauthorized: true,
};

const server = https.createServer(tlsOptions, (req, res) => {
  // Verify client certificate
  const cert = req.socket.getPeerCertificate();

  if (req.client.authorized) {
    res.writeHead(200);
    res.end("Secure connection established");
  } else {
    res.writeHead(401);
    res.end("Unauthorized");
  }
});

server.listen(443, () => {
  console.log("Secure server running on port 443");
});
```
