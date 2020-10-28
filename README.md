# ti83python-menulib
A free library for python on ti83 premium CE python to create simple menu
You can all personalize (the options, the title, the start cursor position)

![menulib in work](https://i.postimg.cc/CzhNjyrD/Webp-net-gifmaker.gif)

(sorry if my calculator is in french)

You can control it with the buttons up, down, numbers, enter, (annul, suppr, trace, graphe return 0 because it's the best place for a quit button)

## How to install :
you can download the .8xv file and put it on your TI83 with [TI Connect](https://education.ti.com/en/products/computer-software/ti-connect-ce-sw) or [TILP](https://www.ticalc.org/archives/files/fileinfo/374/37481.html).

Also you can get the source code from the source branch [here]() to get a look into it.

## How to use it :
You just have to import the MENU script like that : `from MENU import menu` and you can call like this :

    menu( &#91;list&#93;, &lt;curs&gt;, &lt;title&gt;)
Were :
* `list` is the list of all options can be displayed
* `curs` the place where the cursor is displayed at start (is 0 at default)
* `title` is a text thatwill be displayed on the top if the menu if you want to disable it put it on `False` (is False at default)
