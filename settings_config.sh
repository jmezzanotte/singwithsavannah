#!/bin/sh

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
	#sed -i '.bak' 's/EMAIL_HOST_USER/EMAIL_HOST_USER="Dude"/g' test.txt
	sed -i -E '.bak' 's/[ =a-zA-Z0-9]$/EMAIL_HOST_USER="dude"/g' test.txt


	echo "Looking for email password information"
	PASS=$(cat singwithsavannah/settings.py | grep EMAIL_HOST_PASSWORD)



fi 