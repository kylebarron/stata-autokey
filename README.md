# Stata + Autokey
#### Run Stata code in a Stata GUI window from a text editor.

**NOTE: This only works on Linux.**

This repository holds files to run code snippets from a text editor in a graphical session of Stata, using the Autokey desktop automation utility. This works by invisibly copying the selected text in your text editor, moving to the Stata window, pasting it in the console, and pressing enter. Autokey lets you bind a script to a keyboard sequence, thus you can run code by pressing control-R, for example.

## Getting Started

### Prerequisites

The Python 3 version of Autokey is necessary as a prerequisite. Please check the [Autokey repository](https://github.com/autokey-py3/autokey) for installation instructions.

You _should_ be able to install Autokey on Ubuntu 16.04 with just 
```
sudo add-apt-repository ppa:troxor/autokey
sudo apt update
sudo apt install autokey-gtk
```
Then to run the program, just type `autokey-gtk` into your console.

### Installing

The files in `code/` are just configuration files. To "install" them, you just need to download them and put them into your configuration folder.

By [default](https://github.com/autokey-py3/autokey/wiki/FAQ), Autokey stores your configuration information at `~/.config/autokey`. So you should be able to get the files working with the code below.

```
mkdir -p "~/.config/autokey/data/My Phrases"
git clone https://github.com/kylebarron/stata-autokey.git
cp stata-autokey/code/run_stata*.py "~/.config/autokey/data/My Phrases/"
cp stata-autokey/code/.run_stata.json "~/.config/autokey/data/My Phrases/"
cp stata-autokey/code/.run_stata.chunk.json "~/.config/autokey/data/My Phrases/"
rm -rf stata-autokey
``` 

### Using

By default, this code is set up to run from the Atom text editor in a graphical Stata window. With these files installed, you should be able to open a .do file in Atom, have a Stata window open somewhere, and press `ctrl-r` to send a selection to Stata.

Soon, I hope to make it clearer how to adjust the scripts to run from Sublime or Visual Studio. Add a bug report if you're interested in using these from a different editor and I haven't updated this.


### Limitations

- If there are two Stata windows open at the same time, this doesn't always know what to do. For me it usually pastes and runs code in the first window I opened, but not always.
- There seems to be a bug when running ~ 80-100 lines of code. I use it mostly for smaller code chunks.
- This uses the "name" doesn't work with a console version of stata (if you're using a text editor like atom, just use a terminal inside the program if you want the console version).



## Author

* [**Kyle Barron**](https://github.com/kylebarron)

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details

