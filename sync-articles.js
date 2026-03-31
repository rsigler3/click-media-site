const fs = require('fs');
const https = require('https');

const SUPABASE_URL = 'https://pnuczigdeuxyextjlpva.supabase.co';
const SUPABASE_ANON_KEY = 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6InBudWN6aWdkZXV4eWV4dGpscHZhIiwicm9sZSI6ImFub24iLCJpYXQiOjE3NzM5MjU3NzksImV4cCI6MjA4OTUwMTc3OX0.JQ_r72q2v0J4JeWuhUN4W6ccadFdiOlvhcQzPeAx0L4';

// Use the REST API instead of the Supabase JS library to keep out external dependencies.
// For all articles, including drafts/published, but we sort by published_date desc.
// 'select=*' to fetch everything.
const requestUrl = `${SUPABASE_URL}/rest/v1/articles?select=*&order=published_date.desc`;

const options = {
    headers: {
        'apikey': SUPABASE_ANON_KEY,
        'Authorization': `Bearer ${SUPABASE_ANON_KEY}`
    }
};

console.log('Fetching articles from Supabase...');
https.get(requestUrl, options, (res) => {
    let rawData = '';

    // A chunk of data has been received.
    res.on('data', (chunk) => {
        rawData += chunk;
    });

    // The whole response has been received.
    res.on('end', () => {
        try {
            if (res.statusCode !== 200) {
                console.error(`Error: Supabase responded with status ${res.statusCode}`);
                console.error(rawData);
                process.exit(1);
            }
            
            const parsedData = JSON.parse(rawData);
            
            // Write the parsed JSON exactly to articles.json
            fs.writeFileSync('articles.json', JSON.stringify(parsedData, null, 2), 'utf8');
            console.log(`Successfully synced ${parsedData.length} articles to articles.json.`);
            
        } catch (e) {
            console.error('Failed to parse articles:', e.message);
            process.exit(1);
        }
    });

}).on('error', (e) => {
    console.error(`Got error: ${e.message}`);
    process.exit(1);
});
