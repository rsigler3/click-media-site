const { createClient } = require('@supabase/supabase-js');
const SUPABASE_URL = 'https://pnuczigdeuxyextjlpva.supabase.co';
const SUPABASE_ANON_KEY = 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6InBudWN6aWdkZXV4eWV4dGpscHZhIiwicm9sZSI6ImFub24iLCJpYXQiOjE3NzM5MjU3NzksImV4cCI6MjA4OTUwMTc3OX0.JQ_r72q2v0J4JeWuhUN4W6ccadFdiOlvhcQzPeAx0L4';
const supabase = createClient(SUPABASE_URL, SUPABASE_ANON_KEY);
async function run() {
  const { data, error } = await supabase.storage.listBuckets();
  console.log(data, error);
}
run();
