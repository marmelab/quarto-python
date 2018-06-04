FROM python:3
ADD src/quarto.py /
RUN pip install pystrich
RUN pip install pep8
CMD [ "python3", "quarto.py" ]