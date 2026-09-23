# Output reference

The default Dataset contains one item for each unique comment or reply successfully saved.

| Field | Type | Always present | Description |
| --- | --- | :---: | --- |
| videoId | string | Yes | YouTube video ID. |
| videoUrl | string | Yes | Canonical YouTube video URL. |
| videoTitle | string or null | Yes | Video title when available. |
| channel | string or null | Yes | Channel name when available. |
| commentId | string | Yes | Stable identity for the comment. |
| commentUrl | string | Yes | Direct URL to the comment. |
| text | string or null | Yes | Comment text when available. |
| author | string or null | Yes | Public author display name when available. |
| authorId | string or null | Yes | Public author ID when available. |
| authorUrl | string or null | Yes | Public author channel URL when available. |
| authorThumbnail | string or null | Yes | Public author thumbnail URL when available. |
| publishedAt | string or null | Yes | Publication time in UTC when available. |
| likeCount | integer or null | Yes | Visible like count when available. |
| parentId | string or null | Yes | Parent comment ID for a reply; null for top-level comments. |
| isReply | boolean | Yes | Whether the item is a reply. |
| isPinned | boolean or null | Yes | Whether YouTube marks the comment as pinned, when available. |
| isUploader | boolean or null | Yes | Whether the comment is from the video uploader, when available. |
| isVerified | boolean or null | Yes | Whether the author is verified, when available. |

Nullable fields mean the source did not provide a value. The SUMMARY key-value record describes run status and per-video errors; it is not a Dataset row.
