FROM python:3.11-slim
MAINTAINER maksim.maslo@simbirsoft.com
COPY . /python-tests
WORKDIR /python-tests
RUN pip install --no-cache-dir -r requirements.txt
CMD pytest tests/ui/ --remote=http://10.73.102.102:4444 --browser_name=firefox -v --alluredir=allure-results/
