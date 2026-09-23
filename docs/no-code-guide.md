# Run YouTube Comments Scraper without code

You can use the hosted Actor from Apify's web interface without installing a client or writing a script.

## Step-by-step

1. Open [YouTube Comments Scraper](https://apify.com/datascraperes/youtube-comments-scraper?fpr=edudata).
2. Select the **Input** tab.
3. Enter up to 10 public YouTube video URLs or 11-character video IDs in **startUrls**.
4. Choose **new** for newest comments or **top** for top comments. Set **maxComments** from 1 to 10,000 per video.
5. Click **Start**.
6. Open the **Dataset** tab to inspect the comment rows and export them as JSON or CSV.

## First test

Use [data/sample-input.json](../data/sample-input.json). It requests at most five comments from one public video so you can check the output before running a larger batch.

## Use the monthly free usage credit

Apify's Free plan currently includes **$5 in monthly prepaid usage** for Apify Store or platform services, and no credit card is required to start. The Actor charges per saved comment, so a test consumes usage while credit is available. Unused credit expires at the end of the billing cycle.

See [current Apify pricing](https://apify.com/pricing?fpr=edudata) for current plan terms.

## What to check in the output

Each Dataset row is one unique comment or reply. Check **videoId** and **commentId** to identify its source, **text** for the comment, **publishedAt** and **likeCount** for available engagement details, and **parentId** / **isReply** to understand the thread. Some author, timestamp, like, or badge values can be null.

The run's **SUMMARY** record is stored in the default key-value store. It contains run status and per-video errors. If a video cannot be processed, inspect this record as well as the Dataset; successfully saved rows remain available.

## Larger runs

Submit up to 10 unique videos, with a maximum of 10,000 comments per video and 100,000 comments per run. These are maximums, not guarantees that YouTube will provide that many. A comment or reply is billed only after a unique row is saved. For longer runs, use the asynchronous Actor API or one of the client libraries and retrieve the Dataset after the run completes.
