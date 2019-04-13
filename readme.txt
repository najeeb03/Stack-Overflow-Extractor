Stack-Overflow-Extractor

This is a small web-app which will simply display the ten most recent and ten most voted question  about 'android' on Stack Overflow.

It uses Stack Exchange's API to make an HTTP request and then processes the data and displays it.

The data is displayed in two columns; the left one for 10 most recent questions and thr right show the ten most voted questions. Clicking on the question text will open a new tab with the question thread on https://www.stackoverflow.com

INSTRUCTIONS:

To use this web application you will need Python 3.5 or above. Please follow these steps to run it yourself:

  1) Clone the git repository from here: https://github.com/najeeb03/Stack-Overflow-Extractor.git or simply download the files from the master branch.		

  2) Make sure Python version 3 is installed where you intend to execute this application from. Here is a link from where you can download Python: https://www.python.org/downloads/

  3) You will also need to install two Python packages, Flask and Requests:
    a) First open your cli shell, then type in the command: 'pip install flask'. (Pip comes pre-installed with Python 3) 
	   This will start installing the Flask package.
	
	b) Similar to step 3a) type in the command: 'pip install requests'. This will start installing the Requests package.
	   
	   For reference, the package websites are provided: Flask: http://flask.pocoo.org/, Requests: http://docs.python-requests.org/en/master/

  4) After the steps above are done, from your CLI shell change directory to where you have stored the files from this repository. Then type in 'python extractor.py'.
      This will cause the extractor.py file to be executed using Python and Flask web server to star running.

  5) Now open a browser and type in either 'http://127.0.0.1:5000/' or 'localhost:5000'. This will open the web application home/landing page.

Please note: Since this website uses a non-key version of Stack Exchange's API it will be limited to 300 requests daily.
Stack Exchange API documentation: https://api.stackexchange.com/docs
