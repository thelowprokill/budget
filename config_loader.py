###################################################
#                                                 #
# Program: config_loader                          #
#                                                 #
# Purpose: Loads config file                      #
#                                                 #
# Input:                                          #
#      none:                                      #
#                                                 #
# Output:                                         #
#      none:                                      #
#                                                 #
# Author: Jonathan Hull         Date: 16 Nov 2020 #
#                                                 #
###################################################

from os import path

CONFIG_FILE = ".config"

############################################
#                                          #
# class: config_storage                    #
#                                          #
# Purpose: data storage instance           #
#                                          #
############################################
class config_storage:
    def __init__(self):
        self.mysql_host  = '192.168.0.134'
        self.mysql_port  = '3306'
        self.mysql_user  = 'root'
        self.mysql_pass  = 'pass'
        self.mysql_data  = 'db_name'
        self.win_title   = 'Family Budget'
        self.win_width   = '1920'
        self.win_height  = '1080'
        self.cell_width  = '300'
        self.cell_height = '500'
        self.font_size   = '10'

############################################
#                                          #
# class: config_loader                     #
#                                          #
# Purpose: load a configuration file       #
#                                          #
############################################
class config_loader:
    ############################################
    #                                          #
    # Function: __init__                       #
    #                                          #
    # Purpose: constructor for config_loader   #
    #          class                           #
    #                                          #
    # args:                                    #
    #   self:                                  #
    #   message: function callback to writ to  #
    #            program log file              #
    #                                          #
    # outputs:                                 #
    #   none:                                  #
    #                                          #
    ############################################
    def __init__(self, message):
        self.message = message
        # init default values
        self.defaults = config_storage()
        self.val      = config_storage()
        self.read()

    ############################################
    #                                          #
    # Function: write                          #
    #                                          #
    # Purpose: create a new config file based  #
    #          on default values               #
    #                                          #
    # args:                                    #
    #   self:                                  #
    #                                          #
    # outputs:                                 #
    #   none:                                  #
    #                                          #
    ############################################
    def write(self):
        self.message(0, "config file failed to load. Making new one.")
        config = open(CONFIG_FILE, "w+")
        # write new file
        # make form for new file
        config.write("mysql_host  =" + self.defaults.mysql_host  + "\n")
        config.write("mysql_port  =" + self.defaults.mysql_port  + "\n")
        config.write("mysql_user  =" + self.defaults.mysql_user  + "\n")
        config.write("mysql_pass  =" + self.defaults.mysql_pass  + "\n")
        config.write("mysql_data  =" + self.defaults.mysql_data  + "\n")
        config.write("win_title   =" + self.defautls.win_title   + "\n")
        config.write("win_width   =" + self.defautls.win_width   + "\n")
        config.write("win_height  =" + self.defautls.win_height  + "\n")
        config.write("cell_width  =" + self.defautls.cell_width  + "\n")
        config.write("cell_height =" + self.defautls.cell_height + "\n")
        config.write("font_size   =" + self.defautls.font_size   + "\n")
        config.close()
        self.message(0, "Successfully created new config file.")
        self.read()

    ############################################
    #                                          #
    # Function: read                           #
    #                                          #
    # Purpose: read config file                #
    #                                          #
    # args:                                    #
    #   self:                                  #
    #                                          #
    # outputs:                                 #
    #   none:                                  #
    #                                          #
    ############################################
    def read(self):
        try:
            self.message(1, "Reading config file.")
            config = open(CONFIG_FILE, "r")
            # read all lines of config file
            mysql_host  = self.read_config_line(config)
            mysql_port  = self.read_config_line(config)
            mysql_user  = self.read_config_line(config)
            mysql_pass  = self.read_config_line(config)
            mysql_data  = self.read_config_line(config)
            win_title   = self.read_config_line(config)
            win_width   = self.read_config_line(config)
            win_height  = self.read_config_line(config)
            cell_width  = self.read_config_line(config)
            cell_height = self.read_config_line(config)
            font_size   = self.read_config_line(config)
            config.close()

            # update stored data
            self.val.mysql_host  = mysql_host
            self.val.mysql_port  = mysql_port
            self.val.mysql_user  = mysql_user
            self.val.mysql_pass  = mysql_pass
            self.val.mysql_data  = mysql_data
            self.val.win_title   = win_title
            self.val.win_widht   = win_width
            self.val.win_height  = win_height
            self.val.cell_widht  = cell_width
            self.val.cell_height = cell_height
            self.val.font_size   = font_size
            self.message(1, "Successfully read config file.")
        except:
            try:
                config.close()
            except:
                pass
            self.write()


    ############################################
    #                                          #
    # Function: read_config_line               #
    #                                          #
    # Purpose: read after '=' in line          #
    #                                          #
    # args:                                    #
    #   fp = file pointer                      #
    #                                          #
    # outputs:                                 #
    #   line                                   #
    #                                          #
    ############################################
    def read_config_line(self, fp):
        line = fp.readline()
        return line[line.rfind("=") + 1:].replace('\n','')
