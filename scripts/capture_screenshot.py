#!/usr/bin/env python3
"""Capture a full-page screenshot of a URL and save as PNG."""
import sys

from playwright.sync_api import sync_playwright


def main():
    if len(sys.argv) != 3:
        print("Usage: capture_screenshot.py <url> <output_path>", file=sys.stderr)
        sys.exit(1)
    url, output_path = sys.argv[1], sys.argv[2]

    with sync_playwright() as p:
        browser = p.chromium.launch(
            channel="chrome",
            headless=False,
            args=["--disable-blink-features=AutomationControlled"],
        )
        context = browser.new_context(
            viewport={"width": 1280, "height": 900},
        )
        context.add_init_script(
            "Object.defineProperty(navigator, 'webdriver', {get: () => undefined})"
        )
        page = context.new_page()
        page.goto(url, wait_until="load", timeout=45000)
        page.wait_for_timeout(4000)
        title = page.title()
        print(f"Page title: {title!r}", file=sys.stderr)
        page.screenshot(path=output_path, full_page=True)
        browser.close()
    print(f"Saved: {output_path}")


if __name__ == "__main__":
    main()
