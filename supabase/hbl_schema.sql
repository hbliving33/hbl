-- HBLiving hit counter and monthly report.
-- Run this once in Supabase: SQL editor, New query, paste, Run.  It is safe to run again.

-- 1. Raw events: one row per ad view or tap.  Nothing about the visitor is stored.
create table if not exists public.ad_events (
  id   bigint generated always as identity primary key,
  ad   text not null check (char_length(ad) between 1 and 60),
  kind text not null check (kind in ('view', 'call', 'web', 'dir')),
  site text not null default 'hbliving' check (char_length(site) between 1 and 40),
  at   timestamptz not null default now()
);
create index if not exists ad_events_at_idx on public.ad_events (at);
alter table public.ad_events enable row level security;

-- Anyone can add an event.  Nobody can read, change or delete events through the website.
drop policy if exists "log ad events" on public.ad_events;
create policy "log ad events" on public.ad_events for insert to anon, authenticated with check (true);

-- Supabase projects created after May 30, 2026 need explicit website access.
grant usage on schema public to anon, authenticated;
grant insert on public.ad_events to anon, authenticated;

-- 2. Who may see reports.  Add your own email here (see step 4).  No policies, so the website cannot read or change it.
create table if not exists public.hbl_admins (email text primary key);
alter table public.hbl_admins enable row level security;

-- 3. Monthly totals per ad and site, only for a signed-in admin.
create or replace function public.ad_report(p_month date)
returns table (ad text, site text, views bigint, calls bigint, webs bigint, dirs bigint)
language sql stable security definer set search_path = public as $$
  select e.ad, e.site,
         count(*) filter (where e.kind = 'view'),
         count(*) filter (where e.kind = 'call'),
         count(*) filter (where e.kind = 'web'),
         count(*) filter (where e.kind = 'dir')
  from public.ad_events e
  where e.at >= date_trunc('month', p_month)
    and e.at <  date_trunc('month', p_month) + interval '1 month'
    and exists (select 1 from public.hbl_admins a where lower(a.email) = lower(auth.jwt() ->> 'email'))
  group by e.ad, e.site
  order by e.ad, e.site;
$$;
revoke all on function public.ad_report(date) from public, anon;
grant execute on function public.ad_report(date) to authenticated;

-- 4. Then run this line with your own email address in place of the example:
-- insert into public.hbl_admins (email) values ('you@example.com') on conflict do nothing;
