FROM python:3.11-slim
MAINTAINER maksim.maslo@simbirsoft.com
COPY . /python-tests
WORKDIR /python-tests
RUN pip install --no-cache-dir -r requirements.txt
CMD pytest -m api -v --alluredir=allure-results/


#IMAGE_NAME="test-image"
#CONTAINER_NAME="test-container"
#echo "Check current working directory"
#pwd
#echo "Build docker image and run container"
#docker-compose up -d --remove-orphans
#docker build -t $IMAGE_NAME .
#docker run -d --name $CONTAINER_NAME $IMAGE_NAME
#echo "Copy result into Jenkins container"
#docker cp $CONTAINER_NAME:/python-tests/allure-results/ allure-results/
#echo "Cleanup"
#docker stop $CONTAINER_NAME
#docker rm $CONTAINER_NAME
#docker rmi $IMAGE_NAME
#docker-compose down --rmi local