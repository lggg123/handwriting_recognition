# Handwritten Recognition using Python and Tensorflow
### Here we are building an app that will upon drawing what it is requesting accept it as true after it recognizes it. 
## Section 1 (architecture)
### When building this app we make the template which will be the files that will house our handwriting recognition app front-end. 
### the static files are the css and jquery. 
### the app.py is the flask app file that houses the routes and encoder.
## Section 2 (backend and data)
### once you install numpy and import it in your app.py add into the post of /add-data labels = np.array(). You can go to the branch `backend-api-data-addition` and see the addition of the api compared to `static-site`
## Section 3 (how to use)
### first clone the app by navigating to a folder or directory and typing this command to build a new folder with the app in it `git clone https://github.com/lggg123/handwriting_recognition.git` then navigate to that folder by typing this command into the terminal or command line `cd handwriting_recognition`. Then install required dependencies using pip looking at the commands below. You can use python 2.7 but if you have issues and need to upgrade to python3 make sure to google configure your path so you can type the `python` or `python3` commmand into the terminal. Your PATH is the the direction your command uses when you type it in such as python3 directing to the python3 installation folder and such.
### if you have python 3 installed matplotlib, flask, and numpy installed using pip `pip install matplotlb flask numpy` to upgrade to python3 please google and refer the way you wish.
### you can start the app by running `python app.py` or `python3 app..py` depending upon your python version setup and PATH (refer to google to setup python3 by googling python3.9 setup and PATH configuration you can also refer to python3.9 docs by googling python 3.9 docs.
### Most issues when it comes to configuration and setup comes down to being a great googler.
### Once you have your app running on localhost:5000 you can add data to the model for training by clicking the add data button or you can click the practice button to actually use the Tensorflow handwriting recognition to be able to recognize the letter you are drawing in uppercase.(REMEMBER!!! you will not be able to get this app to work properly if you do not add training data by clicking add data and following the instructions)
### simply open the script data_distribution to see how the data is being distributed by simply in terminal typing `python scripts/data_distribution.py`
### if you have any questions on how to use the app email me `rails_dev@codengine.org` and make an issue in github or open a pull request.