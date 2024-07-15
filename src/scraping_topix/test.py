import asyncio

from pyppeteer import launch

# cmd = " ".join(Launcher(executablePath="/usr/bin/google-chrome-stable").cmd)
# print(cmd)


async def main():
    browser = await launch(
        headless=True,
        executablePath="/usr/bin/google-chrome-stable",
        args=["--no-sandbox"],
    )
    page = await browser.newPage()
    await page.goto("https://example.com")
    await page.screenshot({"path": "example.png"})
    await browser.close()


asyncio.get_event_loop().run_until_complete(main())
