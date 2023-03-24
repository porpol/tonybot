from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import time

from selenium.webdriver.chrome.options import Options


async def startserv(update_channel):

    attempts = 0

    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.get('https://aternos.org/go/')

    try:
        user = driver.find_element(By.ID, 'user')
        user.send_keys('airpod2')

        pas = driver.find_element(By.ID, 'password')
        pas.send_keys('SIGNIN456')

        login = driver.find_element(By.ID, 'login')
        login.click()
    except:
        await update_channel.send('Could not login')
        return

    driver.get('https://aternos.org/servers/')

    while driver.current_url != 'https://aternos.org/servers/':
        await update_channel.send('Loading servers...')
        if attempts < 5:
            attempts += 1
        else:
            await update_channel.send('Could not load servers')
            return
        time.sleep(0.1)

    attempts = 0

    try:
        mcrafter = driver.find_element(By.XPATH, '/html/body/div[1]/main/div[2]/div[2]/section/div[1]/div[2]/div/div[1]')
        mcrafter.click()
    except:
        await update_channel.send('Could not find server')
        return

    await update_channel.send(driver.current_url)

    while driver.current_url != 'https://aternos.org/server/':
        await update_channel.send('Loading server...')
        if attempts < 5:
            attempts += 1
        else:
            await update_channel.send('Could not load server')
            return
        time.sleep(0.1)

    attempts = 0

    start = driver.find_element(By.ID, 'start')

    status = driver.find_element(By.CLASS_NAME, 'statuslabel-label').text
    await update_channel.send(status)

    if status == 'Offline':
        start.click()

        while driver.find_element(By.CLASS_NAME, 'statuslabel-label').text == 'Offline':
            try:
                error = driver.find_element(By.CLASS_NAME, 'alert-body')
                await update_channel.send('Error')
                return
            except:
                print('ok')

            if attempts < 1:
                await update_channel.send('Attempting to click start button')
            if attempts < 5:
                attempts += 1
            else:
                await update_channel.send('Could not click start button')
                return
            time.sleep(2)

        await update_channel.send('Starting server!')

    elif status == 'Preparing ...' or status == 'Loading ...' or status == 'Starting ...':
        await update_channel.send('Server is already starting!')
    elif status == 'Stopping ...' or status == 'Saving ...':
        await update_channel.send('Server is currently stopping, wait a bit')
    elif status == 'Online':
        await update_channel.send('Server is already online!')
    else:
        await update_channel.send('UNKNOWN SERVER STATUS: ', status)
