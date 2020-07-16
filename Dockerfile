FROM python:3

WORKDIR /usr/src/app

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

USER 1000:1000

#CMD [ "scrapy", "runspider", "quotes_spider.py", "-o", "quotes.json"]
CMD [ "python", "scrabing_mails.py", "-o", "mails.json"]
