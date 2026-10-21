# HBLiving

The website for hbliving.com, a local guide to life in Huntington Beach, California.

- index.html: home page
- logos.html: 25 logo options (not linked from the menu, hidden from search engines)
- build/hbl_build.py rebuilds the home page, and build/logos_build.py rebuilds the logos page and the site mark.

Run `python3 build/logos_build.py` then `python3 build/hbl_build.py` after changes.

## Hit counter and monthly report

- assets/js/track.js counts ad views and taps (call, website, directions) on HBLiving and on community sites.  It stores counts in Supabase.  Nothing about the visitor is stored, and there are no cookies.
- Setup: create a Supabase project, run supabase/hbl_schema.sql in the SQL editor, add your email to hbl_admins (the last line of that file), then put the project URL and publishable key in assets/js/track.js.
- report.html (not linked, hidden from search engines) shows each ad's monthly totals after you sign in with an admin email.
