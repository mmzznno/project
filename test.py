#更新
from selenium.webdriver import Chrome, ChromeOptions
from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver 
import pandas as pd
 
#driver = webdriver.Chrome(ChromeDriverManager().install()) 

def scraping():
    driver_path = ChromeDriverManager().install()
    options =ChromeOptions()
    options.add_argument = ("--headless")
      
    driver = Chrome(driver_path, options=options)


    url = 'https://gyoumu-kouritsuka-pro.site/'

      
    driver.get(url)

        
    df = pd.DataFrame()
       
    while True :
       article_elms = driver.find_elements_by_css_selector(".entry-card-wrap.a-wrap.border-element.cf")
       
       for article_elm in article_elms:
           
             #print(article_elm.text)

              title = article_elm.find_element_by_tag_name("h2").text
              post_date = article_elm.find_element_by_class_name("post-date").text
              article_link = article_elm.get_attribute("href")

              print(title, post_date, article_link)

              df  = df.append({
                     "タイトル":title,
                     "投稿日":post_date,
                     "記事":article_link
               }, ignore_index= True)

       try:
               driver.find_element_by_css_selector(".pagination-next-link.key-btn").click()

       except:
                   print("最終ページです")
             
                   break

       df.to_csv("記事一覧.csv", encoding="utf-8_sig"), 
        

scraping()

