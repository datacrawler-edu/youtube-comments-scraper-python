# Use cases

Use the hosted Actor to collect public comments from the specific videos you provide. Each example below is intentionally small; edit the supplied sample input before increasing the result limit.

## Review audience feedback on a video

Submit one video URL with **sort: new** and a small **maxComments**. Review **text**, **publishedAt**, and **likeCount** to understand recent public discussion. Use **commentId** to keep each comment identifiable in later analysis.

## Compare public discussions across videos

Submit up to 10 video URLs in one run. Use the same sort and per-video maximum to compare the returned comments across those videos. Group rows by **videoId** or **videoUrl**; replies are included in the per-video maximum and can be identified by **isReply** and **parentId**.

## Export comment threads for research or reporting

Open the run's Dataset and export it as CSV or JSON. Keep **commentId**, **videoId**, **parentId**, and **isReply** when you need to retain comment identity and thread relationships in a downstream workflow. Review the run's **SUMMARY** record for errors or videos that returned fewer comments than requested.
