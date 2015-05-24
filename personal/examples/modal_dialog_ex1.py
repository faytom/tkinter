"""
Example of how to create a modal dialog

Based on: http://tkinter.unpythonic.net/wiki/ModalWindow

'transient' is only part of the solution.
You also want to 'set the grab' on the secondary window,
and then 'wait' for the secondary window to close.
So this is the magical sequence to make a window modal in tkinter:

    1. transient
    2. grab_set
    3. wait_window

Explanation based on the explanation by Eric Brunel.
"""

import tkinter as tk


class ModalDialog(tk.Toplevel):

    """Simple modal dialog with a button"""

    def __init__(self, root, *args, **kwargs):
        tk.Toplevel.__init__(self, root, *args, **kwargs)
        
        self.body = tk.Frame(self, bd=1, relief="groove")
        self.body.pack(expand=True, fill="both", padx=1, pady=1)

        self.bottom = tk.Frame(self, bd=1, relief="groove")
        self.bottom.pack(fill="x", side="bottom", padx=1, pady=1)

        self.ok_button = tk.Button(self.bottom, text="Ok", command=self._ok)
        self.ok_button.pack(side="right")

        self.close_button = tk.Button(self.bottom, text="Close", command=self.destroy)
        self.close_button.pack(side="right")

        # make window modal
        self.transient(root)
        self.grab_set()
        self.wait_window(self)

    def _ok(self):
        print("Ok")


if __name__ == "__main__":
    root = tk.Tk()
    opener = tk.Button(root, text="Open modal dialog", command=lambda: ModalDialog(root))
    opener.pack()
    root.mainloop()
