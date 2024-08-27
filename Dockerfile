FROM rapidfort/python-chromedriver
WORKDIR /readyscript_demo
COPY . .
RUN python -m pip install --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt
CMD ["pytest", "-sv", "tests"]