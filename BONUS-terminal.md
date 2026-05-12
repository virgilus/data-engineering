# 🐧 Linux Terminal Basics — Beginner Course

## 🎯 Course Objective
This course introduces the **fundamental Linux terminal commands**.  
You’ll learn how to:
- Navigate the file system  
- Manage files and directories  
- Work with permissions  
- Search text and monitor processes  

---

## Introduction

### What is the Terminal?  

The terminal (or command line) is a text-based interface that allows you to interact with your computer using commands. It provides more control and flexibility compared to graphical user interfaces (GUIs).

### Why Use the Terminal?

- **Efficiency**: Perform tasks quickly with commands.
- **Automation**: Write scripts to automate repetitive tasks.
- **Remote Access**: Manage servers and systems remotely.

### What is the difference between Terminal, Shell, and Command Line?

- **Terminal**: The application that provides access to the command line interface (e.g., GNOME Terminal, iTerm2).
- **Shell**: The program that interprets and executes commands (e.g., Bash, Zsh).
- **Command Line**: The text-based interface where you type commands.

### Windows vs Linux based OS

- On Windows you have several terminals and shells available (Command Prompt, PowerShell, Windows Subsystem for Linux, Git Bash, Anaconda Prompt...). They all have different purposes, commands, functionalities and shortcuts. 😱

- On linux/unix based OS (like Ubuntu, Debian, MacOS, etc.) you have one shell (usually bash or zsh) that uses the same set of commands. 👍

### Bash vs Zsh

- **Bash** (Bourne Again SHell) is the most common shell on Linux systems. It is widely used and has a large community.
- **Zsh** (Z Shell) is an extended version of bash with additional features like improved tab completion, better scripting capabilities, and more customization options. Many people use also a framework like Oh My Zsh to enhance their zsh experience.

Overall, almost all the commands work the same in both shells.

### WSL2 (Windows Subsystem for Linux)

WSL2 allows you to run a Linux environment directly on Windows without the overhead of a traditional virtual machine. It provides a full Linux kernel and supports most Linux command-line tools and applications. It used to be difficult to install, but now it's very easy and straightforward.

### Anaconda Prompt

Anaconda Prompt is a command line interface that comes with the Anaconda distribution, primarily used for managing Python environments and packages. It is tailored for data science and machine learning tasks.

### Git Bash

If you're using Windows and want a simple way to access a bash terminal, Git Bash is a great option. It comes bundled with Git for Windows and provides a minimal bash environment.

## 🧭 1. Navigating the File System

### 📍 Show the current directory

```bash
pwd
```

> Prints the full (absolute) path of the current working directory.

### 📂 List files and directories

```bash
ls
```

> Lists the contents of the current directory.

Useful options:

* `ls -l` → detailed list (permissions, size, owner, date)
* `ls -a` → include hidden files (those starting with `.`)
* `ls -lh` → human-readable sizes (KB, MB, GB)

### 🚶 Change directories

```bash
cd directory_name
```

Examples:

```bash
cd /home/user/Documents
cd ..        # Go up one directory
cd ~         # Go to your home directory
cd /         # Go to the system root
```
---

## 📄 2. Managing Files and Directories

### 🆕 Create a new empty file

```bash
touch file.txt
```
### Create multiple files

```bash
touch file1.txt file2.txt file3.txt
```
### Create a file with content

#### With a text editor (vim)

```bash
vim notes.txt
```

Once inside `vim`, press `i` to enter insert mode, type your content, then press `Esc`, type `:wq!`, and hit `Enter` to save and exit. Let's break down the steps:

- `Esc` exits insert mode.
- `:` enters command-line mode, you can type several commands after this.
- `w` writes (saves) the file.
- `q` quits the editor.
- `!` forces the action (no confirmation is required).


#### With echo and redirection

```bash
echo "Hello, World!" > hello.txt
```
The `>` sign is used for redirecting the output of a program to something other than stdout (standard output, which is the terminal by default). The `>>` appends to a file or creates the file if it doesn't exist. The `>` overwrites the file if it exists or creates it if it doesn't exist.

```bash
echo "This is an additional line." >> hello.txt
```

#### With cat (concatenate)

```bash
cat > newfile.txt
```
Type your content, then press `Ctrl + D` to save and exit.

### 📁 Create a new directory

```bash
mkdir my_folder
```

Use `-p` to create parent directories if needed:

```bash
mkdir -p projects/code/python
```

### 📋 Copy files and folders

```bash
cp source.txt destination.txt
cp -r folder1 folder2  # copy a directory
```

The flag `-r` stands for "recursive", which is necessary when copying directories to ensure all contents are copied.

### 🔀 Move or rename files

```bash
mv old_name.txt new_name.txt
mv file.txt folder/   # move file to a directory
```

The command `mv` is used for both moving and renaming files or directories.

### ❌ Delete files or directories

```bash
rm file.txt
rm -r folder/
```

Again the `-r` flag is used for recursive deletion of directories and their contents.

⚠️ Be careful when using `rm` — **this does not use the trash bin**.
If you want to send files to the trash, consider using a tool like [`trash-cli`](https://github.com/andreafrancia/trash-cli).

---

## 🔍 3. Viewing and Searching Files

### 📖 View file content

```bash
cat file.txt
```

Other useful commands:

* `less file.txt` → view file page by page
* `head file.txt` → show the first 10 lines
* `tail file.txt` → show the last 10 lines
* `tail -f logfile.log` → follow new lines in real time

### 🔎 Search text inside files

```bash
grep "keyword" file.txt
```

Options:

* `-i` → ignore case
* `-r` → recursive search in directories
* `-n` → show line numbers

Example:

```bash
grep -rin "error" /var/log/
```

## 4. Operators

### && (Logical AND)

```bash
command1 && command2
```
The `&&` operator allows you to chain commands together, where the second command will only execute if the first command is successful (returns a zero exit status).

Example:
```bash
mkdir new_folder && cd new_folder
```
In this example, `cd new_folder` will only execute if `mkdir new_folder` is successful.

### | (Pipe)

```bash
command1 | command2
```
The pipe operator (`|`) is a powerful feature in Linux that allows you to chain commands together, passing the output of one command as input to another.

Example:
```bash
cat file.txt | grep "search_term"
```
Here, the output of `cat file.txt` is passed as input to `grep`, which searches for "search_term" in that output.

---

## 🔐 5. Permissions and Ownership

### 📜 View permissions

```bash
ls -l
```

Example output:

```
-rw-r--r-- 1 user user 1234 Oct 29  file.txt
```

Explanation:

* First character: `-` = file, `d` = directory
* `r` = read, `w` = write, `x` = execute
* Three groups: owner / group / others

### 🔧 Change permissions

Each group has three types of permissions: read (r), write (w), and execute (x). You can change permissions using `chmod`.

**Octal digit permission**

| Octal | Bits        | Symbolic | Permissions                |
|-------:|------------|----------|---------------------------|
| 7     | 4 + 2 + 1  | `rwx`    | read, write and execute   |
| 6     | 4 + 2      | `rw-`    | read and write            |
| 5     | 4 + 1      | `r-x`    | read and execute          |
| 4     | 4          | `r--`    | read only                 |
| 3     | 2 + 1      | `-wx`    | write and execute         |
| 2     | 2          | `-w-`    | write only                |
| 1     | 1          | `--x`    | execute only              |
| 0     | 0          | `---`    | none                      |

```bash
chmod 751 script.sh
```

Numbers correspond to:

* 7 = read + write + execute
* 5 = read + execute
* 1 = execute only

So `751` means:
* Owner: read, write, execute
* Group: read, execute
* Others: execute only


### 👤 Change file owner

```bash
sudo chown new_user:new_group file.txt
```

---

## ⚙️ 6. System and Process Management

### Sudo

`sudo` (superuser do) allows a permitted user to execute a command as the superuser or another user, as specified by the security policy.

```bash
sudo command
```

### 👤 Show current user

```bash
whoami
```

### 📊 List running processes

```bash
ps aux
```

### 🔪 Kill a process

```bash
kill PID
```

> Find the PID using `ps` or `top`.

### 🚀 Monitor system activity

```bash
top
```

Or the improved version (if installed):

```bash
htop
```

---

## 📦 7. Package Management (Debian/Ubuntu example)

### 🔍 Search for a package

```bash
apt search package_name
```

### ⬇️ Install a package

```bash
sudo apt install package_name
```

### 🔁 Update the system

```bash
sudo apt update && sudo apt upgrade
```

---

## 🧰 8. Other Useful Commands

| Command         | Description                      |
| --------------- | -------------------------------- |
| `clear`         | Clear the terminal screen        |
| `history`       | Show your command history        |
| `man <command>` | Display the manual for a command |
| `echo "text"`   | Print text to the terminal       |
| `date`          | Show the current date and time   |
| `df -h`         | Show disk space usage            |
| `du -sh folder` | Show the size of a folder        |

---

## 🧩 9. Practice Exercises

Try these small challenges to reinforce what you’ve learned:

1. Create a directory named `project` and a subdirectory `src`.
2. Create an empty file called `notes.txt` inside `project`.
3. Copy `notes.txt` into `src/` and rename it `backup.txt`.
4. Display the current path using `pwd`.
5. Check the permissions of all files in `project` with `ls -l`.
6. Use `grep` to search for the word “TODO” inside a text file.
7. View the last 5 lines of a log file using `tail`.