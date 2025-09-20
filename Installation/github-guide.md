# GitHub troubleshooting
If you've followed the instructions so far, you should have a main folder dedicated to this class somewhere on your computer. This folder (let's assume it is called **Programming**) should have two subfolders inside it: **Materials** and **Assignments**.

## The Materials folder
This is the folder that corresponds to [our GitHub course repository](https://github.com/barburevencu/PPE). To make things easy, **do not edit existing files or add new files to it**. To update it, in the Terminal or Git Bash window, type in:

```bash
cd your-path/Programming/Materials
git pull
```

**Do this every week at the start of the class!**

### Troubleshooting
If you get an error, this probably means that you have changed this folder by accident. To fix this, delete the **Materials** folder from your computer, go back to the **Programming** folder in the Terminal, then clone it again: 

```bash
cd your-path/Programming
git clone https://github.com/barburevencu/PPE.git
mv PPE Materials # Change the name of the folder from PPE to Materials
```

## The Assignments folder
This is the folder linked to **your cogsup-prog GitHub repository** that you will use to upload your assignments to. To make things easy, **edit this folder only on your computer**. In other words, do not **edit** it online on the GitHub website.

Every week, after you update **Materials** folder to the latest version, you will see a new subfolder inside it corresponding to the current week (e.g., **Week-1**, **Week-2**, etc.). You need to copy this subfolder into **Assignments**:

```bash
cd your-path/Programming/Assignments
cp -R ../Materials/Week-x . # Replace x with the number of the current week
```

Then, after solving the exercises, to push your solutions, you need to be inside the **Assignments** folder again, so do:

```bash
git add .
git commit -m "Added solutions for Week x"
git push
```

**Do this every week twice**:
1. At the end of the class
2. By Sunday 12:00 (noon, not midnight)

### Troubleshooting
If you get an error, this probably means that there are conflicts between your local repository copy and the online one. To fix this, move the entire contents of your **Assignments** folder outside of it (for instance, to your Desktop). Then, delete the Assignments folder completely and clone your repository again:

```bash
cd your-path/Programming
git clone https://github.com/YOUR-USERNAME/cogsup-prog.git # Change your username and the name of your repository accordingly
mv cogsup-prog Assignments # Change the name of the folder from PPE to Assignments
```

Move back the folders you copied inside Assignments so you don't lose any work. Then you'll be able to ```add```, ```commmit```, and ```push``` again.
