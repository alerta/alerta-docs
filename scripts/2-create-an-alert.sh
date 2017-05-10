
curl -v -XPOST http://localhost:8080/alert \
    -H 'Authorization: Key demo-key' \
    -H 'Content-type: application/json' \
    -d '{
          "attributes": {
            "region": "US"
          },
          "correlate": [
            "HttpServerError",
            "HttpServerOK"
          ],
          "environment": "Production",
          "event": "HttpServerError",
          "group": "Web",
          "origin": "curl",
          "resource": "web02",
          "service": [
            "example.com"
          ],
          "severity": "critical",
          "tags": [
            "dc2"
          ],
          "text": "Site is down.",
          "type": "exceptionAlert",
          "value": "Internal Server Error (500)"
        }'
