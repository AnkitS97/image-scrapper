# Image Scrapper

This is an image scrapper project created uisng python 3.6.12. It uses selenium web driver to open an instance of chrome browser. It then fires a search query with the sepcified search term and extracts urls of image to be downloaded. It then creates an images folder, downloads these images using requests api and saves them in a folder named by the search term inside the images folder.

## How to run the project

Note: Once you clone the project make sure to replace the chrome driver with a chrome driver according to your version of chrome browser. You can download a chrome driver from [here](https://chromedriver.storage.googleapis.com/index.html)

- Open anaconda prompt

- Create a new enivironment
    `conda create -n <env name> python==3.6.12`
    
- Navigate within anaconda prompt to the directory where you have cloned this project

- To install all the dependencies
    `pip install -r requirements.txt`
    
- To run the app
    `python main.py --driver ./chromedriver.exe --search "<search something>" --max_images <Number of images>`
    
    
 ## Screenshots
 
 ### Initial folder directory
 
 ![initial folder](https://github.com/AnkitS97/image-scrapper/blob/main/Initial%20folder.png)
 
 
 ### Downloading images from browser
 
 ![downloading images](https://github.com/AnkitS97/image-scrapper/blob/main/downloading%20images.png)
 
 ### Final folder directory
 
 ![final folder](https://github.com/AnkitS97/image-scrapper/blob/main/after%20download.png)
 
 

