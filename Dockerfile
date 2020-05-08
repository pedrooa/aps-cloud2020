#publicly available docker image "python" on docker hub will be pulled

FROM python

#creating directory helloworld in container (linux machine)

RUN mkdir \home\pyproject

#copying helloworld.py from local directory to container's helloworld folder

COPY pyproject.py /home/pyproject/pyproject.py

#running helloworld.py in container

CMD python /home/pyproject/pyproject.py