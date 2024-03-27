import time
import mysql.connector
from selenium import webdriver

mydb = mysql.connector.connect(
    host = "localhost",
    user = "ivan",
    password = "password",
    database = "metric_tracker"
    )
    
mycursor = mydb.cursor()
#mycursor.execute("CREATE TABLE customers(name VARCHAR(255), address VARCHAR(255))")

# Initialize browser
driver = webdriver.Chrome()

# Navigate to your website 
driver.get("http://localhost:3000/")

metrics = []
# Track presence time 
start_time = time.time()
presence_time = start_time
while True:#presence_time < 50: # seconds
    current_time = time.time()
    presence_time = current_time - start_time
    print(f"Presence time: {presence_time} seconds")
    
    # Track scrolling
    scroll_height = driver.execute_script("return document.body.scrollHeight")  
    current_scroll = driver.execute_script("return window.pageYOffset")
   # scrolled_pixels = current_scroll/scroll_height
    print(f"Scrolled {current_scroll}/{scroll_height} pixels")
    sql = "INSERT INTO metrics (presence_time, scrolled_pixels) VALUES (%s, %s)"
    val = (presence_time, current_scroll)
    mycursor.execute(sql, val)
    mydb.commit()
    time.sleep(2) 

    # Track clicks   
    # buttons = driver.find_elements_by_tag_name("button")
    # num_clicks = 0

    # for button in buttons:
    #     button.click()
    #     num_clicks += 1
        
    # print(f"Number of clicks: {num_clicks}")
        
driver.quit()
