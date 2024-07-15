#!/usr/bin/env python3

import asyncio
import logging

from pyppeteer import launch


async def main():
    # Pyppeteerでブラウザを起動
    browser = await launch(
        headless=True,
        executablePath="/usr/bin/google-chrome-stable",
        args=["--no-sandbox"],
        logLevel=logging.DEBUG,
    )
    page = await browser.newPage()

    # ウェブページにアクセス
    url = "https://sekai-kabuka.com"  # 実際のURLに置き換えてください
    await page.setUserAgent(
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36",
    )
    await page.goto(url)

    # XPathを使って数値を抽出
    xpath_expression = '//*[@id="衒籌恚肆蹶恤く朿祓羯舍ﾂｪ"]/span[1]/font/text()'
    elements_head = await page.xpath(xpath_expression)
    xpath_expression = '//*[@id="衒籌恚肆蹶恤く朿祓羯舍ﾂｪ"]/span[1]/font/font/text()'
    elements_tail = await page.xpath(xpath_expression)

    if (
        elements_head
        and elements_tail
        and len(elements_head) == 1
        and len(elements_tail) == 1
    ):
        topix_head = await page.evaluate(
            "(element) => element.textContent",
            elements_head[0],
        )
        topix_tail = await page.evaluate(
            "(element) => element.textContent",
            elements_tail[0],
        )
        topix_value = float(f"{topix_head.replace(",", "")}{topix_tail}")
    else:
        raise

    # ブラウザを閉じる
    await browser.close()
    print(topix_value)


if __name__ == "__main__":
    # asyncioでmain関数を実行
    asyncio.get_event_loop().run_until_complete(main())
