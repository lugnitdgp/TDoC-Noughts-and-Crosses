In this multi threading task, I have created one server file.
And there are two(can be any number) client files, which are exact same. So, basically this client file runs on several different computers at same time.

First run the server.py file.
Then the clients can join the server by running the client.py file.

In my Task, client_1 and client_2 can join at any time to the server (after running the server).
Client_1 and Client_2 are independent. At any time they can join, at any time they can leave and they can send message at the same time or different time.
The message they sent simply echo back to them by the server.

After the two client disconnect, the server also turns off.

But, here problem is that I have to specify number of maximum clients in my server.py file.
If clients more than specified maximum number tries to join, they can't join the server.
Now, if I give maximum number a large number, then this problem can be solved. But then another problem is that my server don't stop automatically. We have to stop it manually.

Please help me to overcome this problem.
