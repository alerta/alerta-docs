
curl -v -XPOST http://localhost:8080/alert \
    -H 'Authorization: Key demo-key' \
    -H 'Content-type: application/json' \
    -d '{
          "attributes": {
            "region": "EU"
          },
          "correlate": [
            "HttpServerError",
            "HttpServerOK"
          ],
          "environment": "Production",
          "event": "HttpServerError",
          "group": "Web",
          "origin": "curl",
          "resource": "web01",
          "service": [
            "example.com"
          ],
          "severity": "major",
          "tags": [
            "dc1"
          ],
          "text": "Site is down.",
          "type": "exceptionAlert",
          "value": "Bad Gateway (501)"
        }'
