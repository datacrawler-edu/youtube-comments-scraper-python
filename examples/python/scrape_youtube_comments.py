"""Run the hosted YouTube Comments Scraper and print its Dataset items."""

from __future__ import annotations

import json
import os
from pathlib import Path

from apify_client import ApifyClient

ROOT = Path(__file__).resolve().parents[2]
INPUT_PATH = ROOT / "data" / "sample-input.json"
ACTOR_ID = "datascraperes/youtube-comments-scraper"


def main() -> None:
    token = os.environ.get("APIFY_API_TOKEN")
    if not token:
        raise SystemExit("Set APIFY_API_TOKEN before running this example.")

    run_input = json.loads(INPUT_PATH.read_text(encoding="utf-8"))
    client = ApifyClient(token)
    run = client.actor(ACTOR_ID).call(run_input=run_input)

    if not run or run.status != "SUCCEEDED":
        status = run.status if run else "no run result"
        raise SystemExit(
            f"Actor run did not succeed ({status}). Check the Apify run and SUMMARY."
        )

    dataset_id = run.default_dataset_id if run else None
    if not dataset_id:
        raise SystemExit("The completed run did not return a default Dataset ID.")

    for item in client.dataset(dataset_id).iterate_items():
        print(json.dumps(item, ensure_ascii=False))


if __name__ == "__main__":
    main()
