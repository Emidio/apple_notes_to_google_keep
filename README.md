# Apple notes to Google Keep
Move Apple Notes to Google Keep (iPhone to Android) step by step guide.

Moving from Apple Notes to Google Keep is not easy task, as Apple is notoriously a closed echosystem, and Google Keep lack official API support for free users. I tried solutions googling around, and I finally succeded mixing different parts from them - sharing my experience here hoping it can be helpful to someone else moving from iPhone to Android.

## Export from iCloud
Sync your iPhone notes with iCloud (if not already synched), and ask Apple to get your data (selecting Notes only) - @alekzandriia wrote a very clear blog post with step-by-step guide here:

https://alekzandriia.com/how-to-export-icloud-notes/#instructions

There's a PDF copy here in case @alekzandriia helpful post disappear.

The iCloud export is a zip file with notes as text files. Copy all note text files in the same folder and eventually rename the files - I removed the date part, web is plenty of free renaming tools to do that in batch. Here's you one for Windows and Mac:

https://www.advancedrenamer.com/


## Import into Google Keep
As Google Keep has no import menu and there are no official API to use, I ended up installing unofficial API Python library `gkeepapi` - it can be found here:

https://github.com/kiwiz/gkeepapi

Install python in yor system (if not already there) and install gkeepapi using:
~~~
pip install gkeepapi
~~~
There's a script to import Keep notes using `gkeepapi` on github:

https://gist.github.com/sliceofbytes/f5eab8911c761ff6760362beb17e6477

The script is a little old, and the username/password login is no more supported by Google. Also, I got a problem with unicode characters in notes, so I slightly modified it to use the new authentication method and handle unicode chracters in notes.

Here's the code: [get_mastertoken.py](https://github.com/Emidio/apple_notes_to_google_keep/blob/main/get_mastertoken.py)

You need your Google username (your Google email), and the master token to be able to upload the text files in Google Keep. To obtain the master token, the easiest way is to use your browser and open this link:

https://accounts.google.com/EmbeddedSetup

Enter your Google email address, [Next], your password, [Next], if you have 2 step verification enabled you should receive anotification, confir it's you, the you'll finally get a Welcome screen with [I agree] button. Click [I agree], then open your browser developer tools (ignore if you see the loading gif).

With Firefox, press F12, go to "Storage" menu on top, on the left expand cookies and copy the value of your oauth_token cookie. It should start with: `oauth2_4/`.
To copy, just select the oauth_token line and double click on the value, then CTRL+C. You also need an "Android ID", you should use any hex string like: `0123456789abcdef`.
I used the MAC address stripping the ":" and padding some "0" at the beginning to reach 16 characters. With the `oauth_token` you can finally obtain the master token, using this script (if you have docker installed):
~~~
docker run --rm -it --entrypoint /bin/sh python:3 -c 'pip install gpsoauth; python3 -c '\''print(__import__("gpsoauth").exchange_token(input("Email: "), input("OAuth Token: "), input("Android ID: ")))'\'
~~~
or install `gpsoauth` python library with:
~~~
pip install gpsoauth
~~~
and then run this script after substituting your email, Android ID and `oauth_token` value:
~~~
pithon3 get_mastertoken.py
~~~
Pay attention, the `oauth_token` lasts a few minutes, so you need to generate your master token quickly after `oauth_token` procedure.

You'll get a string starting with: `aas_et/`. Now put your email and master token value in this script, and run it from the folder with the txt files of your notes:
~~~
pithon3 keep_import.py
~~~
Now you have your Apple notes imported in Google Keep. Remember that running multiple times the script on the same notes will import multiple copies of the notes. Also, Google could limit the number of notes to be imported. If so, just limit the txt files number in the import folder to 100 or 200.


