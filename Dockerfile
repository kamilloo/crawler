FROM python:3

WORKDIR /usr/src/app

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

USER 1000:1000

CMD [ "scrapy", "runspider", "quotes_spider.py", "-o", "quotes.json"]
#CMD [ "scrapy",  "shell" , "https://docs.scrapy.org/en/latest/_static/selectors-sample1.html"]
#CMD [ "scrapy",  "view" , "https://katalog.infoludek.pl/kategoria/gabinety_kosmetyczne/61"]
#CMD [ "sleep", "360000"]

