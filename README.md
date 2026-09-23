Use the **YouTube Comments Scraper API** to collect public YouTube comments and replies through Apify, then work with structured Dataset records in Python, JavaScript, cURL, or a spreadsheet. This repository is an integration guide for the hosted Actor; it does not contain the Actor's implementation.

[Open the YouTube Comments Scraper on Apify](https://apify.com/datascraperes/youtube-comments-scraper?fpr=edudata)

## What this repository helps you do

- Collect public comments and replies from one or more YouTube videos.
- Compare audience feedback across videos using stable comment IDs and video metadata.
- Export results as JSON or CSV for research, reporting, and downstream workflows.
- Call the hosted Actor from Python, JavaScript, or cURL without running scraper infrastructure yourself.

## Example result

The following sanitized example shows the Dataset shape. The matching files are [data/sample-output.json](data/sample-output.json) and [data/sample-output.csv](data/sample-output.csv).

```json
{
  "videoId": "a1B2c3D4e5F",
  "videoUrl": "https://www.youtube.com/watch?v=a1B2c3D4e5F",
  "videoTitle": "Example public video",
  "channel": "Example channel",
  "commentId": "sample-comment-001",
  "commentUrl": "https://www.youtube.com/watch?v=a1B2c3D4e5F&lc=sample-comment-001",
  "text": "A clear example with useful steps.",
  "author": "Example viewer",
  "authorId": null,
  "authorUrl": null,
  "authorThumbnail": null,
  "publishedAt": "2026-01-01T12:30:00Z",
  "likeCount": 3,
  "parentId": null,
  "isReply": false,
  "isPinned": false,
  "isUploader": false,
  "isVerified": null
}
```

## Run without code

You can run the hosted Actor from Apify's web interface:

1. Open the [YouTube Comments Scraper](https://apify.com/datascraperes/youtube-comments-scraper?fpr=edudata).
2. In the **Input** tab, enter one or more YouTube video URLs or 11-character video IDs.
3. Choose whether to sort by newest or top comments, and set a maximum per video.
4. Click **Start**.
5. Open the **Dataset** tab to inspect or export the results as JSON or CSV.

For a field-by-field walkthrough, see [docs/no-code-guide.md](docs/no-code-guide.md). Start with the small [data/sample-input.json](data/sample-input.json) before increasing the per-video limit.

## Try it with Apify's free plan

Apify's Free plan currently includes **$5 in monthly prepaid usage** for the Apify Store or your own Actors, and no credit card is required to start. A small test can use that credit while it is available; the Actor itself is billed per saved comment, so this is not unlimited free usage.

Unused credit expires at the end of the billing cycle and does not roll over. Check [current Apify pricing](https://apify.com/pricing?fpr=edudata) before a larger run.

## Quick start for developers

### Python

Install the Apify API client:

```bash
pip install -r examples/python/requirements.txt
```

Set your API token in the environment:

```bash
export APIFY_API_TOKEN="your-token"
```

In Windows PowerShell:

```powershell
$env:APIFY_API_TOKEN = "your-token"
```

Run the example:

```bash
python examples/python/scrape_youtube_comments.py
```

The script reads the small sample input, starts the hosted Actor, and prints each Dataset item as JSON. Do not commit your API token.

## Input example

This small request asks for at most five comments and replies from one video:

```json
{
  "startUrls": [
    {
      "url": "https://www.youtube.com/watch?v=dQw4w9WgXcQ"
    }
  ],
  "sort": "new",
  "maxComments": 5
}
```

Each URL entry may be a supported YouTube video URL or an 11-character video ID. See [docs/input-reference.md](docs/input-reference.md) for accepted URL types, defaults, and limits.

## Request examples

### cURL

See [examples/curl-request.md](examples/curl-request.md) for a synchronous API request using a Bearer token.

### Python

See [examples/python/scrape_youtube_comments.py](examples/python/scrape_youtube_comments.py). It uses the official Apify API client for Python.

### JavaScript

See [examples/javascript/request.mjs](examples/javascript/request.mjs). It uses the official Apify API client for JavaScript.

All requests call the hosted Actor. They do not require local scraping code or a YouTube API key.

## Output fields

Each Dataset row represents one unique comment or reply. Fields describe the video, comment text, available author information, publication time, likes, and reply relationship. Some source values may be null when YouTube does not provide them.

| Field | Meaning |
| --- | --- |
| videoId, videoUrl, videoTitle | Video identifier, canonical video URL, and available title. |
| commentId, commentUrl, text | Comment identity, direct comment URL, and text when available. |
| author, authorId, authorUrl, authorThumbnail | Public author details available with the comment. |
| publishedAt, likeCount | Publication time in UTC and visible like count, when available. |
| parentId, isReply | Parent comment ID for a reply; top-level comments have a null parentId. |
| isPinned, isUploader, isVerified | Available pinned, uploader, and verification indicators. |

See [docs/output-reference.md](docs/output-reference.md) for all Dataset fields and null behavior. Run-level status and per-video errors are kept separately in the run's SUMMARY key-value record.

## Common use cases

The guide in [docs/use-cases.md](docs/use-cases.md) covers:

- Reviewing audience feedback on a public video.
- Comparing themes and engagement across several videos.
- Exporting comment threads for research or reporting.

## How to scrape YouTube comments with Python using Apify

Install the client, set APIFY_API_TOKEN, edit [data/sample-input.json](data/sample-input.json), and run [examples/python/scrape_youtube_comments.py](examples/python/scrape_youtube_comments.py). The example deliberately requests only five comments. Increase maxComments only when you need a larger result and understand the per-comment charge.

## How to export YouTube comments and replies to CSV

Run the Actor and open its Dataset in Apify to export CSV, or retrieve Dataset items through the API and convert them in your own workflow. Each row has commentId, videoId, text, publishedAt, and reply fields so you can retain the connection between a comment and its source video.

## FAQ

See [docs/faq.md](docs/faq.md) for questions about input formats, result limits, unavailable comments, and billing.

## Limits and pricing

Submit up to **10 video URLs or IDs**. The Actor can save up to **10,000 comments per video**, with a **100,000-comment cap per run**. The limit includes replies. Requested counts are maximums; YouTube may expose fewer comments.

The Actor charges one comment-result event for each unique comment or reply saved to the Dataset. Current configured prices are:

| Apify tier | Price per saved comment | Equivalent per 1,000 saved comments |
| --- | ---: | ---: |
| FREE | $0.001 | $1.00 |
| BRONZE | $0.0009 | $0.90 |
| SILVER | $0.0008 | $0.80 |
| GOLD | $0.00075 | $0.75 |
| PLATINUM | $0.00075 | $0.75 |
| DIAMOND | $0.00075 | $0.75 |

Apify calculates the charge per saved comment; the per-1,000 figures are comparison equivalents. Duplicate comments, failed video requests, and the run summary do not trigger comment-result events. The configured event pricing has no separate Actor-start event. See the [Actor page](https://apify.com/datascraperes/youtube-comments-scraper?fpr=edudata) and [current Apify pricing](https://apify.com/pricing?fpr=edudata) for the latest terms.

## Hosted version

Use the [hosted YouTube Comments Scraper](https://apify.com/datascraperes/youtube-comments-scraper?fpr=edudata) when you need web-based runs, saved results, batching, or API access without managing scraping infrastructure.

## Responsible use

Use this Actor only for public information you are allowed to collect and process. You are responsible for complying with applicable privacy requirements and YouTube's terms. Avoid collecting or retaining personal data that is not needed for your purpose.

## Support

For an issue with these integration examples, [open a GitHub issue](https://github.com/datacrawler-edu/youtube-comments-scraper-python/issues) and include a sanitized request and error message. For an Actor run problem, use the Actor's **Issues** tab and include the run ID; never include your API token.

## License

This repository is released under the MIT License.
