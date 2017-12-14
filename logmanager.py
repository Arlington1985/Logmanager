#!/usr/bin/env python
#title           :logmanager.py
#description     :This script was written for arhiving, dowloading new log files from hosts and deleting old log files from LOGSTORE. Part of the script in Python and another part in Shell. Configuration file is storing in config.ini file.
#author          :Rovshan Musayev
#date            :20160122
#version         :0.2
#usage           :python logmanager.py or sh logmanager.sh
#notes           :
#python_version  :2.4.7


 


def is_section(config_section):
    """
       Check that config elemet is a section
    """
    try:
     config_section.keys()
    except AttributeError:
        return False
    else:
        return True

import os, sys, time, logging
from configobj import ConfigObj
from subprocess import call
config = ConfigObj('config.ini',list_values=True,interpolation=True,encoding='UTF8')
logging.basicConfig(format='%(asctime)s %(levelname)s %(message)s', level=logging.DEBUG)

logging.info("----------START OF THE PROCESS----------")

for section in config.keys() :
    if is_section(config[section]):
        logging.info("Initializing config for host: "+section)
    username = ""
    password = ""
    keep_logs_last_x_days_on_log_folder = ""
    keep_logs_last_x_days_on_archive_folder = ""
    keep_logs_last_x_days_on_logstore = ""
    target_log_folder = ""
    target_archive_folder = ""
    dest_logstore_folder = ""
        for subsection in config[section]:
            if is_section(config[section][subsection]):
                logging.info("  Target dest:"+subsection)
                
                for subsubsection in config[section][subsection]:
                    logging.info("    "+subsubsection+"= "+config[section][subsection][subsubsection])
                    
                    keep_logs_last_x_days_on_log_folder = keep_logs_last_x_days_on_log_folder_g
                    keep_logs_last_x_days_on_archive_folder = keep_logs_last_x_days_on_archive_folder_g
                    keep_logs_last_x_days_on_logstore = keep_logs_last_x_days_on_logstore_g
                    
                    if subsubsection == 'keep_logs_last_x_days_on_log_folder':
                        keep_logs_last_x_days_on_log_folder = config[section][subsection][subsubsection]
                    elif subsubsection == 'keep_logs_last_x_days_on_archive_folder':
                        keep_logs_last_x_days_on_archive_folder = config[section][subsection][subsubsection]
                    elif subsubsection == 'keep_logs_last_x_days_on_logstore':
                        keep_logs_last_x_days_on_logstore = config[section][subsection][subsubsection]
                    elif subsubsection == 'target_log_folder':
                        target_log_folder = config[section][subsection][subsubsection]
                    elif subsubsection == 'target_archive_folder':
                        target_archive_folder = config[section][subsection][subsubsection]
                    elif subsubsection == 'dest_logstore_folder':
                        dest_logstore_folder = config[section][subsection][subsubsection]
                        
                
                
                if (username and len(username)>0):
                    HOST = username+"@"+section
                    COMMAND1 = "ssh "+HOST+" 'bash -s' < arch.sh "+target_log_folder+" "+target_archive_folder+" "+keep_logs_last_x_days_on_log_folder+" "+keep_logs_last_x_days_on_archive_folder
                    COMMAND2 = "rsync -av --remove-source-files  "+HOST+":"+target_archive_folder+"/tmp/* "+dest_logstore_folder
                
                    logging.info("Archiving of files")
                    os.system(COMMAND1)
                    logging.info("Downloading of files")
                    os.system(COMMAND2)

                logging.info("Removing old archive files from LOGSTORE")
                now = time.time()
                cutoff = now - (int(keep_logs_last_x_days_on_logstore) * 86400)
                logging.info("Accessing " + dest_logstore_folder + " folder")
        r = 0
        for dirname, dirnames, filenames in os.walk(dest_logstore_folder):
            for filename in filenames:
                file = os.path.join(dirname, filename)
            #print(file)
                        t = os.stat(file)
                    c = t.st_ctime

                        # delete files older than keep_logs_last_x_days_on_logstore 
                    if c < cutoff:
                r = r + 1
                            os.remove(file)
                            logging.info(file + " was removed from LOGSTORE SUCCESFULLY")
        if r == 0:
            logging.info("Nothing to remove")

            else :
                logging.info("    "+subsection+"="+config[section][subsection])
                if subsection == 'username':
                    username = config[section][subsection]
                elif subsection == 'keep_logs_last_x_days_on_log_folder':
                    keep_logs_last_x_days_on_log_folder_g = config[section][subsection]
                elif subsection == 'keep_logs_last_x_days_on_archive_folder':
                    keep_logs_last_x_days_on_archive_folder_g = config[section][subsection]
                elif subsection == 'keep_logs_last_x_days_on_logstore':
                    keep_logs_last_x_days_on_logstore_g = config[section][subsection]


logging.info("----------END OF THE PROCESS----------")