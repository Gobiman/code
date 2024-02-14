# screen 
[linux](linux.md) command that allows you to run multiple terminal applications 

##### basic screen commands
```bash
screen -ls # list running screens 
screen -list 
screen -S "Name_of_Screen" # create new screen session 
screen -r "Name_of_Screen" # attach to screen session 
Ctrl + A N for next screen 
Ctrl + A d # detach & return to the main screen 
ps -e | grep -i "Name_of_Screen" # shows screen process is running  
Ctrl A tab go to the next screen at the bottom
```

##### Kill screen session
```bash
Ctrl + A d
screen -list 
screen -S <name of screen session> -X quit

```





