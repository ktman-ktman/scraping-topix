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
    url = "https://nikkei225jp.com"  # 実際のURLに置き換えてください
    url = "https://sekai-kabuka.com"  # 実際のURLに置き換えてください
    # url = "https://nikkei225jp.com/chart/"  # 実際のURLに置き換えてください

    # url = "https://www.yahoo.co.jp"  # 実際のURLに置き換えてください
    await page.setUserAgent(
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36",
    )
    await page.goto(url, timeout=120000)
    await page.screenshot({"path": "example.png"})

    # XPathを使って数値を抽出
    xpath_expression = '//*[@id="V112"]/p/text()'
    xpath_expression = '//*[@id="衒籌恚肆蹶恤く朿祓羯舍ﾂｪ"]/span[1]/font/text()'
    elements = await page.xpath(xpath_expression)
    xpath_expression = '//*[@id="衒籌恚肆蹶恤く朿祓羯舍ﾂｪ"]/span[1]/font/font/text()'
    elements = await page.xpath(xpath_expression)

    if elements:
        # 抽出されたテキストを取得
        value = await page.evaluate("(element) => element.textContent", elements[0])
        print(f"抽出された数値: {value}")
    else:
        print("指定されたXPathに一致する要素が見つかりませんでした")

    # ブラウザを閉じる
    await browser.close()


# asyncioでmain関数を実行
asyncio.get_event_loop().run_until_complete(main())
