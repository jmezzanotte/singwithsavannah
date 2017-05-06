import datetime
import logging
import time
import os


FORMAT_1 = '%(asctime)s - %(name)s - %(levelname)s - %(message)s'

## \brief Creates a logger object
#  \param logger_name name to be used when creating the logger object 
#  \param logfile_name name of the .log file to be used
#  \param logger_format format to be used in the logger.
#  \return Returns a logger logging object that can be used to log.
def create_logger(logger_name, logfile_name, logger_format):

	# Set up directory 
	directory = _create_logger_folder()
	_LOGGER = logging.getLogger(logger_name)
	_LOGGER.setLevel(logging.INFO)
	formatter = logging.Formatter(logger_format)
	
	handler = logging.FileHandler(os.path.join(directory, logfile_name))
	handler.setFormatter(formatter)
	handler.setLevel(logging.INFO)
	
	_LOGGER.addHandler(handler)

	return _LOGGER

## \brief Create a folder to hold the log files. Will use a timestamp so we can store files unique to 
#    certain runs 
#  \return Returns the name of the directory that was made   
def _create_logger_folder():

	directory_name = datetime.datetime.fromtimestamp(time.time()).strftime('%Y-%m-%d %Hhr%Mmin%Ssec')
	directory = os.path.join(os.getcwd(), directory_name)
	if not os.path.exists(directory): 
		os.mkdir(directory)

	return directory



