# A-V-S-C
This python program lets you calculate the area of many 2-D shapes and volume &amp; surface of 3-d shapes.

[Just, in case you haven't figured out the full-form of the title, its : **Area Volume &amp; Surface Area Calculator**. Lol]

<h2>Libraries required to run:</h2>

1. PyQT5 
2. math
3. sys
4. pandas

<h2>How to run?</h2>

Just run the Window.py file to use the program after making sure that the libaries are installed.

<h2>Description :</h2> 

Of course, this program is not meant to be taken seriously. I always wanted to learn GUI progrmming, therefore, I learnt PyQT5 library and then made this to apply my knowledge, I am pretty sure that I have done many things wrong in the code because I of my lack of experience. I also, for the first time used multiple files to make the app, this made the code much more readable. A limitation of this program is that it can't input or output decimal (float) values. 

<h2>Structure :</h2>

1. Window.py  ->  This is basically, the **main** file &amp; has the **GUI** part of the program. 
2. Area.py    ->  This contains all the **formulae** for **area** of 2-D shapes. (ex. : square, rectangle etc).
3. Volume.py  ->  This contains **formulae** for both **volume** and **surface area** of 3-D shapes. (ex. : cube, cuboid etc).
4. Functions.py -> This is basically a bridge between main file and the formula files because the values are sent to this file and then it uses the folumlea to give the result. 
5. title_bar.py -> This is a class which is used to change the default title bar of PyQt apps. The default title bar is very stiff and uncustomizable. Therefore, I had to make my own titlebar.
6. Icon.ico -> This is the icon for the program. 
7. close.png -> This is the icon for the close button in the new title bar.
8. minimise.png -> This is the icon for minimise button in the new title bar. 

<h2>Converting to executable</h2>

 You can use Pyinstaller to convert the program to an executable. If you don't know what Pyinstaller is [click here](https://pypi.org/project/pyinstaller/), if you want to know how to use Pyinstaller, [click here](https://pyinstaller.readthedocs.io/en/stable/usage.html), this will take you to the documentation of the program. But, take care of the following points. 

1. Use the Icon.ico as the icon.
2. I recommend you to not use the --onefile argument when converting.
3. After converting add the files "close.png", "Icon.png" & "minimise.png" in the directory where the .exe file is placed. (because pyinstaller doesn't include these files by itself.) 

<h2>Conclusion</h2>

If you are having any issues, please report. If you know something, which can improve the app please let me know, any help will be appreciated.
