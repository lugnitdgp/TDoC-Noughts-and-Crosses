So, The friend1.py and friend2.py files are the two players more precisely the friend1.py is the server file and friend2.py is the client file that will work only when the friend1.py file is executed first.
One more thing I have used Emojis in place of NOUGHTS and CROSSES.

The code works like this:

-> The friend1.py file sends the first response to the friend2.py file and simultaneously, the board of the NOUGHTS AND CROSSES gets filled up in both the files. Then the code is checking if anyone wins. 

-> If anyone wins or the game is "draw" immediately the code terminates else the user gets flipped now, the other one will be sending the response.



-> It may be noted the following validation rules:

==> The position entered should not be less than 1 or greater than 9 otherwise it will ask your response again
==> You can not enter the position which may be filled up earlier.


-> You will need to install the 'emojis' module of python3 in order to run the files.
-> Just use the command: "$ pip3 install emoji"

That's it :)