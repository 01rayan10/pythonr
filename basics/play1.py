from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    page = browser.new_page()

    page.goto("https://www.youtube.com")

    # 🟡 محاولة قبول الكوكيز (إذا ظهر)
    try:
        page.locator("button:has-text('Aceptar')").click(timeout=5000)
    except:
        print("No cookie popup")

    # انتظر ظهور البحث
    page.wait_for_selector("input#search")

    # اكتب وابحث
    page.fill("input#search", "ronaldo")
    page.press("input#search", "Enter")

    # انتظر النتائج
    page.wait_for_selector("ytd-video-renderer")

    print("Search done")

    input("اضغط Enter للإغلاق...")
    browser.close()