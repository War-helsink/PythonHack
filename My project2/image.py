#/usr/bin/env python3.7
import random

def images():
    return """
   \033[5;1;3{}m_____         __                 .___.__.__      _________                                  
  /  _  \_______|  | __ _____     __| _/|__|__|    /   _____/ ____ _____    ____   ___________ 
 /  /_\  \_  __ \  |/ / \__  \   / __ | |  |  |    \_____  \_/ ___\\\\__  \  /    \_/ __ \_  __ \\
/    |    \  | \/    <   / __ \_/ /_/ | |  |  |    /        \  \___ / __ \|   |  \  ___/|  | \/
\____|__  /__|  |__|_ \ (____  /\____ | |__|__|   /_______  /\___  >____  /___|  /\___  >__|   
        \/           \/      \/      \/                   \/     \/     \/     \/     \/         \033[0m""".format(random.randint(1, 5))