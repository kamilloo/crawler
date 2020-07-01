FROM python:3

WORKDIR /usr/src/app

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

USER 1000:1000

CMD [ "scrapy", "runspider", "quotes_spider.py", "-o", "quotes.json"]
#CMD [ "scrapy",  "shell" , "http://quotes.toscrape.com/page/1/", "response.css('title')"]
#CMD ["sleep", "360"]
