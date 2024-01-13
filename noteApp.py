import tkinter as tk

class NoteApp:
    def __init__(self, master):
        self.master = master
        master.title("Note App")
        master.configure(bg="lightgreen")


        self.entry = tk.Entry(master, width=30,font=(14))
        self.entry.pack(pady=10)


        self.write_button = tk.Button(master, text="Write to File", command=self.on_write_button_click,font=(14))
        self.write_button.pack(pady=5)

        self.read_button = tk.Button(master, text="Read from File", command=self.show_read_window,font=(14))
        self.read_button.pack(pady=5)

    def file_writer(self, string1):
        with open("n.txt", "a") as writer:
            writer.write(string1 + "\n")

    def file_reader(self):
        with open('n.txt', 'r') as reader:
            fread = reader.readlines()
            content = ""
            for x in fread:
                new_list = x.replace("\n", '').split("\n")
                content += new_list[0] + "\n"
            return content

    def on_write_button_click(self):
        note_text = self.entry.get()
        self.file_writer(note_text)
        self.entry.delete(0, tk.END)

    def show_read_window(self):
        read_window = tk.Toplevel(self.master)
        read_window.title("Read from File")

        content = self.file_reader()

        text_area = tk.Text(read_window, height=10, width=30)
        text_area.insert(tk.END, content)
        text_area.pack(pady=10)

