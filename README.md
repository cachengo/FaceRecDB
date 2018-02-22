# FaceRecDB

To reproduce the MWC demo, clone this repository to /root/FaceRecDB. It contains the database services that manage /db, which also needs to be downloaded. FaceRecDB does utilize sqlite for the actual database engine, though this shouldn't be an issue if you wish to use a different one. All of this has been tested on 64-bit ARM architecture only, though there should be no problem with running on others. 

While the demo runs this service as root, we have run it as other users too. To manage the start/stop of this service, you should utilize the startservices.sh script in the FaceRecCaffe repository. It will take care of starting and stopping all services.

You should note that the database service has to be restarted in order to properly index newly added images to the database. For this function, we are using the inotify capabilities in Ubuntu 16.04. If you wish to automate the blipping of this service, then perform the following:

1. apt-get install inotify-tools
2. apt-get install incron
3. vi /etc/incron.allow and add "root" as an allowed user
4. Type "incrontab -e" to create an monitoring instance and add "/db/facerec.db IN_MODIFY /usr/bin/startservices.sh restart" to it.

Whenever a new image is added or removed from /db/facerec.db, the incron daemon will detect a change to the modified timestamp and restart the services. 
