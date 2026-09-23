# Competitor Screenshots Watch

Full-page homepage screenshots of Studocu's main competitors, for visual change monitoring. Companion to [Robots.txt-Competitors-Watch](https://github.com/zakariyausman1996/Robots.txt-Competitors-Watch) and [SEO-Elements-Competitors-Watch](https://github.com/zakariyausman1996/SEO-Elements-Competitors-Watch).

## Tracked domains
- studocu.com
- chegg.com
- quizlet.com
- coursehero.com
- scribd.com
- brainly.com

## Structure
`screenshots/<YYYY-MM-DD>/<domain>.png` — one full-page PNG per domain per capture. Browse any date's folder on GitHub to view images inline; compare two dates by opening both.

## How it's captured
On-demand only, via `scripts/capture_screenshot.py` (Playwright + Chromium), run locally when asked — not on a schedule.

## Known issues
- **chegg.com** blocks headless browser automation (PerimeterX) — its screenshot shows an "Access to this page has been denied" page rather than the real homepage. This is intentional site-side bot protection and isn't something this project tries to bypass.
