# Downloads manager

This project provides small tools to manage the files on the
infamous-rebel downloads folder. This directory of our machines
is famous for containing all sort of bullshit, and depending on how
of a tidy person you are, it could even contain duplicated files.

In my particular case, this folder is clean most of the times. As a command
line enthusiast, I like to keep this folder clean to move arround my PC the
files I download using basic regex or whatever. Anyways, for me this folder
is usually cleaner than my bedroom.

But there is a thing that bugs me a lot: **file names**. As I said, being a 
command-line heavy user, the filenames matter a lot. I want them to be
**snake_case**, why? because it is easier to work from the command line
if the filenames do not contain spaces.

At the moment, this project only contains that kind of functionality: a script
to clean the names of the downloaded files. Other possible additions for the
future could include a way to organise the files based on their extension.

## Installation and use

Clone the project
```
git clone https://github.com/gabrielblancogarcia/downloads_manager.git
```

cd into the project and run the script

```
cd downloads_manager
python clean_filenames.py
```

or running from outside without cd'ing inside. 

```
python downloads_manager/clean_filenames.py
```

Although the default behaviour will target the downloads folder, the same
script can be used over other folders by passing the folder as an argument

```
python clean_filenames.py --directory path_to_other_dir
```

If you run Linux, you can make it executable by running

```
chmod 755 clean_filenames.py
```
and then run it without having to specify "python" with

```
./clean_filenames.py
```

This project does not include a `requirements.txt` because, at the moment, all
the modules needed exist in the python base.
