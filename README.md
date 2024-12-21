# Discord Chat Analyser
A simple commandline tool to analyse a channel in Discord.

![Figure_1](https://github.com/user-attachments/assets/53d75c23-80da-4c57-81d0-c08ffef6dab1)
Example Use

## Installation Guide
1. Clone the repository
2. Run the command `pip install -r /path/to/requirements.txt`
3. Enable Discord Developer mode as seen [here](https://www.youtube.com/watch?v=8FNYLcjBERM).
4. Get your Discord Bot Token and the channel you want to analyse. 
5. Run main.py

## Flags and Options
### Flags
-q Enables quiet mode and suppresses most messages\
-h Displays this help page\
-v Displays the current version\
          
### Options
--channel=\<id\> Fetches messages from the given channel without asking the user\
--token=\<token\> Will use the given token without asking the user
