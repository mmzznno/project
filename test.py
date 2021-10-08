from.webdriver import Chrome, ChromeOptions
from  webdriver_manager.chrome import ChromeDriverManager
import pandas


    
def scraping():
       driver_path = ChromeDriverManager.install()
       driver = Chrome(driver_path)
       driver.get("https://gyoumu-kouritsuka-pro.site/")
  

scraping()
