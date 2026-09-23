# Input reference

The Actor accepts a JSON object with the following public inputs.

| Field | Type | Required | Example | Description |
| --- | --- | :---: | --- | --- |
| **startUrls** | array of URL objects or video ID objects | Yes | `[{"url":"https://www.youtube.com/watch?v=dQw4w9WgXcQ"}]` | One to ten YouTube video references. Each entry accepts a supported video URL or an 11-character ID. |
| **sort** | string | No | `"new"` | Comment order: **new** (newest first, default) or **top** (top comments). |
| **maxComments** | integer | No | `5` | Maximum saved comments and replies per unique video. Defaults to 100 for API calls that omit it; accepts 1–10,000. |

## Validation and limits

- Maximum video references: 10 unique videos per run.
- Maximum maxComments: 10,000 per video.
- Maximum total output: 100,000 comments per run.
- Supported URLs include YouTube watch, Shorts, live, embed, and youtu.be video links. An 11-character video ID is also accepted.
- Duplicate references are processed once.
- The input editor is prefilled with a small test; the API default for maxComments is 100 when omitted.
- maxComments is a ceiling. The video may have fewer comments available, and replies count toward the ceiling.
