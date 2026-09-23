# FAQ

## Can I run the Actor without Python or code?

Yes. Open the [hosted Actor](https://apify.com/datascraperes/youtube-comments-scraper?fpr=edudata), enter the video URLs or IDs in the **Input** tab, click **Start**, and inspect or export the Dataset. See the [no-code walkthrough](no-code-guide.md).

## Can I test with Apify's Free plan?

Apify's current Free plan includes $5 in monthly prepaid usage and does not require a credit card to start. The Actor still charges for saved comments; available platform credit can cover some usage. Unused credit expires at the end of the billing cycle. Check [current Apify pricing](https://apify.com/pricing?fpr=edudata).

## How do I call the YouTube comments scraper API with Python?

Install **apify-client**, set **APIFY_API_TOKEN**, and run [examples/python/scrape_youtube_comments.py](../examples/python/scrape_youtube_comments.py). The script reads the sample JSON input and retrieves Dataset rows from the completed run.

## Which YouTube links are accepted?

Use a YouTube watch, Shorts, live, embed, or youtu.be video URL, or an 11-character video ID. Submit up to 10 unique videos per run.

## How many comments can I request?

Set **maxComments** from 1 through 10,000 for each video. The run has a hard total cap of 100,000 comments, including replies. This is a maximum; the source may expose fewer.

## Does the Actor return replies?

Yes. Replies are included in the per-video maximum. Use **isReply** and **parentId** to distinguish them from top-level comments.

## What if a video is unavailable or has comments disabled?

YouTube may expose no comments for unavailable videos or videos with comments disabled. Check the run's **SUMMARY** record for per-video errors. Rows already saved for other videos remain in the Dataset; a failed video can cause the overall run to report a failure.

## How is pricing calculated?

The Actor charges one **comment-result** event for each unique comment or reply saved. Duplicate rows, failed video requests, and the run summary do not trigger that event. The current tier prices are listed on the [Actor page](https://apify.com/datascraperes/youtube-comments-scraper?fpr=edudata); check there before a larger run.
