#	WipathAI Web Viewer
###	Prerequisites
The following are development environment:
-	** Ptyhon 2.7 **
	- Flask 1.0.2
    - openslide 1.1.1

###	Environment Setting
Use **[wiconfig.json]()** file to change your local enviroment. The following are setting parameter:


Parameter|Statement
---|---
host_ip|Wipath web viewer server IP address.
host_port|Wipath web viewer server port number.
INITIAL_SLIDE|The slide file path for initial loading.
UPLOAD_FOLDER|The folder path being retrieve uploaded file.
MULTIPLE_DIR|File saved here will be read.
DEEPZOOM_FORMAT|The deepzoom format. (default: jpeg)
DEEPZOOM_TILE_SIZE|The deepzoom tile size. (default: 254)
DEEPZOOM_OVERLAP|The overlap value.(default: 1)
DEEP_LIMIT_BOUNDS|The deep limit bounds switch. (default: True)
DEEPZOOM_TILE_QUALITY|The deepzoom tile quality value. (default: 75)
SLIDE_NAME|The preload file parameter. (default: slide)


### Enable Wipath Web Server
Run the **[wipath_app.py]()** file to enable Wipath web server.
