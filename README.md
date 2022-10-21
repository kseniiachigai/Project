# Telegram bot HSE(ruz)
## What is it?
We have created a bot in Telegram which will be useful for the students of HSE University. This bot show your a timetable of lectures and seminars of every academic group for a week. It is possible to see the starting time, weekday, name of the discipline and type of the class and language on whcih the discipline is taught. The classes are numerated, corresponding with the order of sequence of all classes. If there is no classes on a particular day, the bot write about abscence of lessons and wish a nice day. All information is taken from the official site of HSE University timetable called RUZ ([Расписание Учебных Занятий](https://ruz.hse.ru/)).
## Requirements
The following should be installed to install the bot: 
- python
- pip
- request 
- telebot 
- json 

More detailed information about requirements is presented in the file [requirements.txt](https://github.com/kseniiachigai/Project/blob/main/requirements.txt).
## Installing
### To instal bot the following operations should be done:
Firstly, we must open terminal on Mac 
```
curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py
```
Then install packages
```
python3 get-pip.py
```
After that install API
```
pip install pyTelegramBotAPI
```
Install requests
```
pip install requests
```
And install jsonlib
```
pip install jsonlib
```
After all mentioned procedures, the programm should be open either in VS Code or Idle. And to turn off, the work of terminal should be cancelled.
## Usage 
To start using the bot it is needed to simply to send "/start". Then, enter the academic group in Russian (e. g. "БЦИ211"). Eventually, the timetable will be sent, where every new message represents the separate weekday with lectures and seminars.
1. Send "/start";
2. Enter academic group;
3. Get a timetable.
## Team members
- Kseniia Chigai (213)
- Polina Zhiltsova (211)
- Ekaterina Deeva (211)
- Viktoria Grishina (211)
## Link to the bot
https://t.me/RUZZ_BBot
