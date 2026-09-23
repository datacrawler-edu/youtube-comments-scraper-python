# cURL request

This small request synchronously runs the hosted Actor and returns its default Dataset items as JSON. The token is sent in the recommended Bearer authorization header, not in the URL.

```bash
curl --request POST \
  "https://api.apify.com/v2/acts/datascraperes~youtube-comments-scraper/run-sync-get-dataset-items" \
  --header "Authorization: Bearer $APIFY_API_TOKEN" \
  --header "Content-Type: application/json" \
  --data @data/sample-input.json
```

Set APIFY_API_TOKEN in your shell before running the command. Keep requests small when using a synchronous call. For a larger extraction, start an asynchronous run through the [Apify API](https://docs.apify.com/api/v2) or an Apify client, wait for completion, then retrieve the run's default Dataset. The response contains comment rows; run status and per-video errors are in the SUMMARY key-value record.
