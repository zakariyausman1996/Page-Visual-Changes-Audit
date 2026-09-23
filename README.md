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
On-demand only, via `scripts/capture_screenshot.py` (Playwright driving the real installed Chrome browser, headed mode), run locally when asked — not on a schedule.
