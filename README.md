## Design

For each new road, a new instance should be used, either throuth docker or a new server.
The HTTP Server (this program) can either be in the same machine as the openalpr daemon or on a seperate machine.


    +------------------+                             +------------------+
    |                  |  MJPEG               MJPEG  |                  |
    |  Network Camera  | <---+                 +---> |  Network Camera  |
    |                  |     |                 |     |                  |      
    +------------------+     |                 |     +------------------+                                                      
                             |                 |                          
                             |                 |                                 
                             |      POST       |                              
                             |      +----------|------------------------+
                             |      |          |            POST        |
                             |      |          |            +------+    |                              
                             |      |          |            |      |    |
                   +---------+------+      +---+------------+      |    |
                   |                |      |                |      |    |
                   | alprd server 1 |      | alprd server 2 |      |    |
                   |                |      |                |      |    |  
                   +-----------+----+------+------+---------+      |    |
                               |                  |           +----+----+-----+
                               |      Docker      |           |               |                      
                               |                  |           |   HTTP Server |                           
                               |                  |           |               |
                               +------+-----------+-----------+-----------+---+
                                      |                                   |
                                      |           Host Machine            |
                                      |                                   |
                                      +-----------------------------------+

## Installation:
This guide is designed for linux and mac but can easily be used on Windows.
This program is deigned for Python 3.
Install either through a virtual envirmoment or thought your normal python install.


- python 3
[Install Python 3](https://www.python.org/downloads/)

- virtualenv
```
pip install virtualenv
```

- openalpr installed
[install OpenAlpr](https://github.com/openalpr/openalpr/)

- SQLite
[Install SQLite](http://www.tutorialspoint.com/sqlite/sqlite_installation.htm)


### Section 1 - Using Virtualenv, SQLite with Tornado Web Server
Recommended installation method


download source code into avg_alpr directory
```
git clone https://gitlab.com/msemple1111/average_check.git avg_alpr
```

create the virtual environment, cd into it
```
virtualenv -p python3 avg_alpr
cd avg_alpr
```

Activate virtual enviroment
```
source bin/activate
```

Install Python Dependancys
```
pip install tornado flask
```

Populate sqlite database

```
cat create.sql | sqlite3 average_check.db
```

Start the web server (Press [ctrl] + [c] to stop)
```
python tornado_start.py
```


Open a new terminal Window and Test WebServer is working
```
python bench.py
```


2. Open alpr config

The config file for openalpr should be like this:

```
[daemon]

; country determines the training dataset used for recognising plates.  Valid values are: us, eu
; this is because different countries have different size plates
country = eu

; text name identifier for the location
; this will be your road name
; you will need a different name for each direction and road
; to do this you will need a new server or docker instance for each road
; you can use the same name for multiple lanes
site_id = bromley-w

; Declare each stream on a separate line
; each unique stream should be defined as stream = [url]

; these are the cameras placed on the road
; remember the order you put these in - they corispond to the camera number
; you will need to set the distances for these cameras later in the config
stream = http://123.45.67.89/first_video_stream.mjpeg
stream = http://98.76.54.32/second_video_stream.mjpeg


; topn is the number of possible plate character variations to report
; you could leave this at 1 or place it higher -  it will make no difference
topn = 1

; Determines whether images that contain plates should be stored to disk
; You should leave this on -  then you can receive the images later for prosecution
store_plates = 0
store_plates_location = /var/lib/openalpr/plateimages/

; upload address is the destination to POST to.
; if you have separated the HTTP server and openalpr server,
; change this from localhost to the ip of the HTTP server
upload_data = 0
upload_address = http://localhost:7000/api/camera/
```
