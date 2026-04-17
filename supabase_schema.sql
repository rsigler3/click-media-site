-- Create the articles table
CREATE TABLE IF NOT EXISTS public.articles (
  id uuid DEFAULT gen_random_uuid() PRIMARY KEY,
  title text NOT NULL,
  slug text NOT NULL UNIQUE,
  content text NOT NULL,
  status text NOT NULL DEFAULT 'draft' CHECK (status IN ('draft', 'published')),
  author text,
  published_date timestamp with time zone,
  seo_title text,
  seo_description text,
  schema_faq jsonb DEFAULT '[]'::jsonb,
  created_at timestamp with time zone DEFAULT now(),
  updated_at timestamp with time zone DEFAULT now()
);

-- Turn on Row Level Security
ALTER TABLE public.articles ENABLE ROW LEVEL SECURITY;

-- Drop policies if they already exist so you can safely run this script multiple times
DROP POLICY IF EXISTS "Public can view published articles" ON public.articles;
DROP POLICY IF EXISTS "Admins can manage all articles" ON public.articles;
DROP POLICY IF EXISTS "AI can insert draft articles" ON public.articles;

-- 1. Allow public read access to published articles
CREATE POLICY "Public can view published articles" 
ON public.articles 
FOR SELECT 
USING (status = 'published');

-- 2. Allow authenticated users (Admin) to manage all articles
CREATE POLICY "Admins can manage all articles" 
ON public.articles 
FOR ALL 
TO authenticated 
USING (true)
WITH CHECK (true);

-- 3. Allow AI Agent (using ANON key) to insert draft articles ONLY
-- This ensures the AI can post, but items won't go live until an Admin reviews them.
CREATE POLICY "AI can insert draft articles" 
ON public.articles 
FOR INSERT
TO anon
WITH CHECK (status = 'draft');

-- Optional: Create a storage bucket for blog images
insert into storage.buckets (id, name, public) values ('blog-images', 'blog-images', true) ON CONFLICT DO NOTHING;

-- Drop bucket policies if they exist before creating
DROP POLICY IF EXISTS "Public Access to Images" ON storage.objects;
DROP POLICY IF EXISTS "Admin Auth Insert Images" ON storage.objects;

create policy "Public Access to Images" on storage.objects for select to public using ( bucket_id = 'blog-images' );
create policy "Admin Auth Insert Images" on storage.objects for insert to authenticated with check ( bucket_id = 'blog-images' );

-- NOTE: You MUST have UPDATE and DELETE policies enabled to overwrite/sync articles.json successfully.
-- If you are getting a "Sync Error: new row violates row-level security policy", run the following two commands:
create policy "Admin Auth Update Images" on storage.objects for update to authenticated using ( bucket_id = 'blog-images' );
create policy "Admin Auth Delete Images" on storage.objects for delete to authenticated using ( bucket_id = 'blog-images' );

