import asyncio
from random import choice, randint, uniform
import nodriver as uc

browserPath = ".\\Chrome\\chrome.exe"
number_of_browsers = 30

async def open_browser(i):
    await asyncio.sleep(1)
    proxies = open('proxies_datacenter.txt', 'r', encoding='utf-8').read().splitlines()
    proxy = choice(proxies)
    useragents = open('useragents.txt', 'r', encoding='utf-8').read().splitlines()
    useragent = choice(useragents)
    
    # Read links from the links.txt file
    links = open('links.txt', 'r', encoding='utf-8').read().splitlines()
    link = choice(links)  # Choose a random link from the list

    try:
        driver = await uc.start(
            headless=False,
            browser_executable_path=browserPath,
            user_data_dir=f".\\Users\\{i}\\",
            browser_args=[
                f"--user-agent={useragent}",
                f"--proxy-server={proxy}"
            ]
        )
        
        # Navigate to the selected link
        tab = await driver.get(link)
        await tab.set_window_state(left=randint(0, 1920), top=randint(0, 1080), width=500, height=500, state="normal")

        # Wait for 2 seconds after the page loads
        await tab.sleep(uniform(8, 12))

        # Close the browser
        driver.stop()

    except Exception as e:
        try:
            driver.stop()
        except:
            pass
        print(e)

async def browser_manager(number_of_browsers=number_of_browsers):
    current_browsers = set()

    async def worker(i):
        while True:
            # Start a new browser
            task = asyncio.create_task(open_browser(i))
            current_browsers.add(task)
            await task
            current_browsers.remove(task)

    # Start specified number of browser tasks
    tasks = [worker(i) for i in range(number_of_browsers)]
    await asyncio.gather(*tasks)

if __name__ == "__main__":
    # Start the browser management coroutine
    uc.loop().run_until_complete(browser_manager())
