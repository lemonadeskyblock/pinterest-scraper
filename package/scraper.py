import sqlite3, os, requests, time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.edge.service import Service as EdgeService
from webdriver_manager.microsoft import EdgeChromiumDriverManager



def handle_db(table_name, new_elements, name, folder):
    # db will be created if it does not exist
    conn = sqlite3.connect(f"boards.db")
    cur = conn.cursor()
    cur.execute(f'''
    CREATE TABLE IF NOT EXISTS {table_name} (
        id INTEGER PRIMARY KEY,
        url TEXT)
    ''')
   
    exist_query = f"SELECT EXISTS(SELECT 1 FROM {table_name} WHERE url = ?)"
    add_query = f"INSERT INTO {table_name} (url) VALUES (?)"
    for element in new_elements:
        cur.execute(exist_query, (element,))
        exists = cur.fetchone()[0]
        if not exists:
            download_images(element, name, folder)
            cur.execute(add_query, (element,))
    conn.commit()
    conn.close()

def download_images(url, name, folder):
    i = len(os.listdir(folder)) + 1
    response = requests.get(url)
    image_name = f"{name}_{i}.jpg"
    file_path = os.path.join(folder, image_name)
    if response.status_code == 200:
        with open(file_path, 'wb') as file:
            file.write(response.content)
            print(f"image with the {url} was successfully stored")
    else:
        print(f"'{url}' could not be downloaded")

def get_board(board_link, folder):
    options = webdriver.EdgeOptions()
    options.add_argument('--ignore-ssl-errors=yes')
    options.add_argument('--ignore-certificate-errors')
    options.use_chromium = True

    service = EdgeService(EdgeChromiumDriverManager().install())
    driver = webdriver.Edge(service = service, options = options)
     
    driver.get(board_link)
    title = driver.title
    title = title.replace(" ","")
    print(f"title: {title}")
    npinElement = driver.find_element(By.CSS_SELECTOR, '[data-test-id="pin-count"]')
    nPins = npinElement.text.replace(' Pins', '')
    print(f"pintext: {nPins}") 
    i = len(os.listdir(folder)) + 1
    newElements = set()
     
    while len(newElements) <= int(nPins):
        time.sleep(5)
        allMediaElements = driver.find_elements(By.TAG_NAME, 'img' )
        for element in allMediaElements:
        
            src = element.get_attribute('src')
            if '236x' in src:
                 
                newElements.add(src)
    
        driver.execute_script('window.scrollTo(0, document.body.scrollHeight);')
    time.sleep(2)
    driver.quit()
    return title, newElements
     

 