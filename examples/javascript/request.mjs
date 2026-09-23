import fs from 'node:fs/promises';
import { ApifyClient } from 'apify-client';

const token = process.env.APIFY_API_TOKEN;
if (!token) {
  throw new Error('Set APIFY_API_TOKEN before running this example.');
}

const inputPath = new URL('../../data/sample-input.json', import.meta.url);
const runInput = JSON.parse(await fs.readFile(inputPath, 'utf8'));
const actorId = 'datascraperes/youtube-comments-scraper';
const client = new ApifyClient({ token });

const run = await client.actor(actorId).call(runInput);
if (run.status !== 'SUCCEEDED') {
  throw new Error(
    'Actor run did not succeed (' + run.status + '). Check the Apify run and SUMMARY.',
  );
}

const { items } = await client.dataset(run.defaultDatasetId).listItems();
console.log(JSON.stringify(items, null, 2));
