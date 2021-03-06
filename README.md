# Password-Generator
Password generator for creating strong passwords made using CPython.  
GUI made using tkinter.  
Passwords are generated using cryptographically strong secrets module. 

## How To Use
1. Run ***main\gui.pyw***. 
2. Make sure you have pyperclip installed (to copy the generated password). A screen, warning the user that pyperclip is not installed, will appear if it isn't. 
3. Click on the 'Install' button on the screen to install pyperclip or install it from the command line to proceed: ```pip install pyperclip``` or ```pip3 install pyperclip``` should work.
4. After you have installed pyperclip, the main window will appear.
5. On the main window use the check buttons to include/exclude alphabets, numbers or symbols.
6. Use the length scale to set password length.
7. Press 'Generate' to generate a new password with the current policy.
8. Press 'Copy' to copy currently generated password.
9. The generated password gets copied to your clipboard.

## Screenshot
![Screenshot of main window of Password Generator](screenshot.png)

## Passwords
1. Passwords of length greater than 8 are recommended.
2. A mixture of alphabets (lowercase and uppercase), numbers and symbols are recommended.
3. Reusing passwords is strongly discouraged.
4. Using a password manager is recommended if you can't remember passwords.
5. It is strongly discouraged to include personal information in your passwords.

###### As tested on Windows 10 Home 21H1
###### Available under the MIT License
