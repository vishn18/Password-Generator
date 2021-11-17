"""
Password Generator made using tkinter
"""
import sys
import secrets
import subprocess
import tkinter as tk

# Colours
DARK_BLUE, LIGHT_BLUE, GREY_BLUE = "#122B57", "#4885F7", "#2A3F63"
PINK, YELLOW = "#F64F64", "#F3D88D"

pwd = ""  # Generated password


def install_screen():
    """
    Install window
    :return: None
    """
    install_root = tk.Tk()
    install_root.title("Install Module pyperclip – Password Generator")  # Title
    install_root.geometry("600x250")
    install_root.configure(bg=DARK_BLUE)
    tk.Label(
        install_root,
        text="Password Generator",
        font=(
            "calibri",
            19
        ),
        fg=LIGHT_BLUE,
        bg=DARK_BLUE
    ).pack()
    tk.Label(
        install_root,
        font=(
            "calibri",
            12
        ),
        text="pyperclip not installed\n\n",
        fg=PINK,
        bg=DARK_BLUE
    ).pack()
    tk.Label(
        install_root,
        text="Password Generator requires pyperclip to copy generated passwords to clipboard",
        fg=YELLOW,
        bg=DARK_BLUE
    ).pack()
    tk.Label(
        install_root,
        text="You can install pyperclip from the command line or by pressing the button below",
        fg=YELLOW,
        bg=DARK_BLUE
    ).pack()

    def install():
        """
        Install pyperclip
        :return: None
        """
        try:
            subprocess.check_call([sys.executable, "-m", "pip", "install", "pyperclip"])
            install_root.destroy()
            subprocess.run([sys.executable, __file__])
        except subprocess.CalledProcessError:
            install_error_root = tk.Tk()
            install_error_root.title("Error – Password Generator")
            install_error_root.geometry("400x200")
            install_error_root.configure(bg=DARK_BLUE)
            tk.Label(
                install_error_root,
                text="Password Generator",
                font=(
                    "calibri",
                    19
                ),
                fg=LIGHT_BLUE,
                bg=DARK_BLUE
            ).pack()
            tk.Label(
                install_error_root,
                text="Oops! Something went wrong.\n\n\n\nCheck your connection.\nTry again from the command line.",
                fg=YELLOW,
                bg=DARK_BLUE
            ).pack()
            install_root.destroy()
            install_error_root.mainloop()
        exit()

    tk.Button(
        install_root,
        text="Install",
        command=install,
        bg=DARK_BLUE,
        fg=YELLOW,
        activebackground=DARK_BLUE,
        activeforeground=YELLOW,
        relief="ridge"
    ).place(
        relx=0.5,
        y=200,
        anchor="center"
    )
    install_root.mainloop()
    exit()


try:
    import pyperclip
except ModuleNotFoundError:
    install_screen()


def main():
    """
    Main window
    :return: None
    """
    root = tk.Tk()  # Window
    root.title("Password Generator")  # Title
    root.minsize(width=300, height=500)  # Minimum window size
    root.maxsize(width=300, height=500)  # Maximum window size

    root.attributes('-topmost', True)  # Always on top

    root.configure(bg=DARK_BLUE)  # Background color

    # Title
    tk.Label(
        text="Password Generator",
        font=(
            "calibri",
            20
        ),
        width=29,
        height=2,
        fg=LIGHT_BLUE,
        bg=DARK_BLUE
    ).place(
        relx=0.5,
        y=40,
        anchor="center"
    )
    frm = tk.Frame(root)  # Frame for check buttons
    frm.place(relx=0.5, y=160, anchor="center")
    _az, _AZ, _09, char = tk.IntVar(), tk.IntVar(), tk.IntVar(), tk.IntVar()  # Checkbutton variables

    # Check buttons
    button1 = tk.Checkbutton(
        frm,
        text="a-z",
        variable=_az,
        onvalue=1,
        offvalue=0,
        height=2,
        width=10,
        bg=DARK_BLUE,
        fg=PINK,
        activeforeground=PINK,
        activebackground=DARK_BLUE,
        font=(
            "calibri",
            12,
            "bold"
        ),
        justify="left",
        anchor="w"
    )

    button2 = tk.Checkbutton(
        frm,
        text="A-Z",
        variable=_AZ,
        onvalue=1,
        offvalue=0,
        height=2,
        width=10,
        bg=DARK_BLUE,
        fg=PINK,
        activeforeground=PINK,
        activebackground=DARK_BLUE,
        font=(
            "calibri",
            12,
            "bold"
        ),
        justify="left",
        anchor="w"
    )

    button3 = tk.Checkbutton(
        frm,
        text="0-9",
        variable=_09,
        onvalue=1,
        offvalue=0,
        height=2,
        width=10,
        bg=DARK_BLUE,
        fg=PINK,
        activeforeground=PINK,
        activebackground=DARK_BLUE,
        font=(
            "calibri",
            12,
            "bold"
        ),
        justify="left",
        anchor="w"
    )

    button4 = tk.Checkbutton(
        frm,
        text="!@#$%^&*",
        variable=char,
        onvalue=1,
        offvalue=0,
        height=2,
        width=10,
        bg=DARK_BLUE,
        fg=PINK,
        activeforeground=PINK,
        activebackground=DARK_BLUE,
        font=(
            "calibri",
            12,
            "bold"
        ),
        justify="left",
        anchor="w"
    )

    button1.pack()
    button2.pack()
    button3.pack()
    button4.pack()

    # "Length"
    tk.Label(
        root,
        text="Length",
        bg=DARK_BLUE,
        fg=YELLOW,
        font=(
            "calibri",
            8)
    ).place(
        relx=0.5,
        y=300,
        anchor="center"
    )
    length = tk.DoubleVar()  # Length variable
    # Length scale
    tk.Scale(
        root,
        variable=length,
        from_=1,
        to=32,
        orient="horizontal",
        bg=DARK_BLUE,
        fg=YELLOW,
        troughcolor=GREY_BLUE,
        bd=0,
        activebackground=DARK_BLUE,
        highlightbackground=DARK_BLUE
    ).place(
        relx=0.5,
        y=270,
        anchor="center"
    )

    def generate():
        """
        Generate password
        :return: None
        """
        global pwd

        options = {
            "alpha_upper": _AZ.get(),
            "alpha_lower": _az.get(),
            "nums": _09.get(),
            "special_chars": char.get(),
            "length": int(length.get()),
        }

        pwd = ""
        choices = []
        alpha = "qwertyuiopasdfghjklzxcvbnm"  # Alphabets
        nums = "1234567890"  # Numbers
        special_chars = "!@#$%^&*"  # Special characters / symbols

        if options["alpha_upper"]:
            choices.append(alpha.upper())
        if options["alpha_lower"]:
            choices.append(alpha)
        if options["nums"]:
            choices.append(nums)
        if options["special_chars"]:
            choices.append(special_chars)

        if choices:
            for x in range(options["length"]):
                pwd += secrets.choice(secrets.choice(choices))

        # Covers existing "Copied to clipboard"
        tk.Label(
            root,
            text="",
            bg=DARK_BLUE,
            fg=YELLOW,
            font=(
                "consolas",
                8
            ),
            width=300
        ).place(
            relx=0.5,
            y=430,
            anchor="center"
        )

        # Password
        tk.Label(
            root,
            text=pwd,
            bg=DARK_BLUE,
            fg=LIGHT_BLUE,
            font=(
                "consolas",
                12
            ),
            width=300
        ).place(
            relx=0.5,
            y=410,
            anchor="center"
        )

    # Generate password button
    tk.Button(
        root,
        text="Generate",
        bg=DARK_BLUE,
        fg=YELLOW,
        activebackground=DARK_BLUE,
        activeforeground=YELLOW,
        command=generate,
        relief="ridge"
    ).place(
        relx=0.5,
        y=350,
        anchor="center"
    )

    def copy():
        """
        Copy password to clipboard
        :return: None
        """
        if pwd != "":
            pyperclip.copy(pwd)  # Copies password to clipboard

            # "Copied to clipboard"
            tk.Label(
                root,
                text="Copied to clipboard",
                bg=DARK_BLUE,
                fg=YELLOW,
                font=(
                    "consolas",
                    8
                ),
                width=300
            ).place(
                relx=0.5,
                y=430,
                anchor="center"
            )

    # Copy button
    tk.Button(
        root,
        text="Copy",
        bg=DARK_BLUE,
        fg=YELLOW,
        activebackground=DARK_BLUE,
        activeforeground=YELLOW,
        command=copy,
        relief="ridge"
    ).place(
        relx=0.5,
        y=480,
        anchor="center"
    )

    root.mainloop()  # Main loop


if __name__ == "__main__":
    main()
