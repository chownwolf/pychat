# pychat
 
## Old School Chat client with socket server 

1. Bundle Your Project
Copy the entire pychat project folder (including src and all subfolders/files) to the other PC.
Make sure you include all Python files, __init__.py files, and any requirements files.
2. Install Python
Ensure Python 3.x is installed on the other PC.
3. Install Dependencies
If you have a requirements.txt, run:

If not, install tkinter (usually included with Python) and any other modules you use.

4. Run the Server
On one PC, start the socket server:

(or python src/server/server.py if you run directly)

5. Run the Client/UI
On each PC, run the UI:

Make sure the ChatClient in your code connects to the correct server IP (not just 127.0.0.1).

Example change in chat_client.py:

6. Network Setup
Both PCs must be on the same network.
Firewall must allow traffic on the server port (default: 12345).