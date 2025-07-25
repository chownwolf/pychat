import tkinter as tk
from tkinter import scrolledtext, messagebox
from ..pychat import add_user_to_chat, remove_user_from_chat, send_message_to_chat, get_chat_messages
from ..chat.chat_room import ChatRoom

class ChatApp:
    def __init__(self, master):
        self.master = master
        master.title("Chat Application")

        self.chat_room = ChatRoom()  # Initialize with a ChatRoom instance

        self.messages_area = scrolledtext.ScrolledText(master, state='disabled')
        self.messages_area.pack(padx=10, pady=10)

        self.message_entry = tk.Entry(master)
        self.message_entry.pack(padx=10, pady=10, fill=tk.X)

        self.send_button = tk.Button(master, text="Send", command=self.send_message)
        self.send_button.pack(padx=10, pady=10)

        self.user_entry = tk.Entry(master)
        self.user_entry.pack(padx=10, pady=10, fill=tk.X)

        self.add_user_button = tk.Button(master, text="Add User", command=self.add_user)
        self.add_user_button.pack(padx=10, pady=10)

        self.remove_user_button = tk.Button(master, text="Remove User", command=self.remove_user)
        self.remove_user_button.pack(padx=10, pady=10)

    def send_message(self):
        message = self.message_entry.get()
        user = self.user_entry.get()
        if message and user:
            send_message_to_chat(self.chat_room, user, message)
            self.update_chat_display()  # Show all messages
            self.message_entry.delete(0, tk.END)
        else:
            messagebox.showwarning("Warning", "Please enter a user and a message.")

    def update_chat_display(self):
        messages = get_chat_messages(self.chat_room)
        self.messages_area.config(state='normal')
        self.messages_area.delete(1.0, tk.END)
        for msg in messages:
            self.messages_area.insert(tk.END, msg + "\n")
        self.messages_area.config(state='disabled')
        self.messages_area.yview(tk.END)

    def add_user(self):
        user = self.user_entry.get()
        if user:
            add_user_to_chat(self.chat_room, user)
            self.user_entry.delete(0, tk.END)
        else:
            messagebox.showwarning("Warning", "Please enter a user name.")

    def remove_user(self):
        user = self.user_entry.get()
        if user:
            remove_user_from_chat(self.chat_room, user)
            self.user_entry.delete(0, tk.END)
        else:
            messagebox.showwarning("Warning", "Please enter a user name.")

    def update_chat_display(self, message):
        self.messages_area.config(state='normal')
        self.messages_area.insert(tk.END, message + "\n")
        self.messages_area.config(state='disabled')
        self.messages_area.yview(tk.END)

if __name__ == "__main__":
    root = tk.Tk()
    chat_app = ChatApp(root)
    root.mainloop()