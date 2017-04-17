#!/bin/bash

# author : John Mezzanotte 
# purpose : Shell script to add the email information as well as set debug status. 
# This is so I don't consistently have to push to git and then deploy from heroku 
# to modify settings. Just run this script in your heroku environ. 


EMAIL_USER=johnmezzportfolio@gmail.com
EMAIL_PASS=prunePortfolio22


if [ -f test.txt ]; then 

	echo "Settings file exists"

	echo "Looking for email user information..."
	USER=$(cat test.txt | grep EMAIL_HOST_USER)
	echo "current user set to $USER"
	sed -i 's/EMAIL_HOST_USER*[=a-zA-Z1-9]*/EMAIL_HOST_USER="$EMAIL_USER"/g' test.txt


	echo "Looking for email password information"
	PASS=$(cat singwithsavannah/settings.py | grep EMAIL_HOST_PASSWORD)



fi 