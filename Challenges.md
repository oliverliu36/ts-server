Adding Selenium to Heroku ts-server:
- Helpful:
- https://romik-kelesh.medium.com/how-to-deploy-a-python-web-scraper-with-selenium-on-heroku-1459cb3ac76c
- Slight Changes to Above Procedure:
- webdriver.Chrome() is different, see:
- https://stackoverflow.com/questions/76550506/typeerror-webdriver-init-got-an-unexpected-keyword-argument-executable-p
- SPECIAL CASE:
- For some reasone, we don't need options.binary_location() ("GOOGLE_CHROME_BIN")
- This was found ACCIDENTALLY!

Setting Up Git and Github:
- Clone from public code template
- Create new repo on gitHub (ts-server)
- Unrelated Histories
- Push code template to ts-server
- Deploy was not an issue

