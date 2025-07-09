---
title: "Gemini CLI: A Fresh Setup Guide"
date: 2025-07-09
description: "Stuck installing the Gemini CLI on Windows 11? This is a real-world guide to fixing common npm errors, PowerShell policies, and Google Cloud setup issues that most tutorials don't show you."
tags: ["Gemini", "CLI", "Windows 11", "Node.js", "npm", "PowerShell", "Google Cloud", "Tutorial"]
categories: ["Guides"]
ShowToc: true
showBreadcrumbs: true
comments: true
share_image: "/images/gemini-cli-setup-cover.png"
---

## The Problem: When "Easy Install" Isn't Easy

I recently decided to set up the Gemini CLI on my Windows 11 machine. I watched a bunch of videos, and for everyone else, it seemed to be a simple, one-command installation.

That was not my experience.

My journey started with an `npm` command that failed due to security policies, and then led me down a rabbit hole of environment variables and cloud settings. This isn't another "perfect world" tutorial. This is the real guide to what can go wrong and exactly how to fix it.

Let's get started.

## Step 1: Installing Node.js

First things first, we need Node.js, which includes npm (Node Package Manager). The easiest way to install it on Windows is using `winget` in your terminal.

```bash
winget install OpenJS.NodeJS
```

After the installation, it's crucial to restart your terminal. This allows the system to recognize the new `npm` command.

<p align="center"><img src="/images/winget.png" alt="Gemini CLI Logo"></p>

## Step 2: Troubleshooting Common NPM Errors

This is where my problems began. If you try to install the Gemini CLI and run into errors, here are the two most likely culprits on Windows.

### Problem A: "npm: The term 'npm' is not recognized..."

After installing Node.js and restarting your terminal, you run the install command:

```bash
npm install -g @google/gemini-cli
```

And you see this error:

```powershell
npm : The term 'npm' is not recognized as the name of a cmdlet, function, script file, or operable program. Check the spelling of the name, or if a path was included, verify that the path is correct and try again.
```

Solution:
1.  Restart your terminal again. Sometimes the system just needs a fresh start.
2.  Check the installation. Run `npm -v`. If it's installed correctly, you will see a version number (e.g., `10.8.1`). If you still get an error, your Node.js installation failed or the PATH variable was not set correctly. Try reinstalling Node.js.

### Problem B: "npm.ps1 cannot be loaded..."

This was my main issue. The error looks like this:

```powershell
npm : File C:\Program Files\nodejs\npm.ps1 cannot be loaded. The file C:\Program Files\nodejs\npm.ps1 is not digitally signed. You cannot run this script on the current system. For more information about running scripts and setting execution policy, see about_Execution_Policies at https:/go.microsoft.com/fwlink/?LinkID=135170.
```

Solution:
This error means your PowerShell security policy is blocking the script from running. To fix this, you need to change the execution policy.

1.  Open PowerShell as an Administrator. (Click Start, type "PowerShell", right-click, and select "Run as administrator").
2.  Run the following command:
    ```powershell
    Set-ExecutionPolicy RemoteSigned
    ```
3.  PowerShell will ask for confirmation. Type `Y` and press Enter.
4.  Close the administrator PowerShell window and restart your regular terminal.

Now, when you run `npm install -g @google/gemini-cli`, the installation should complete successfully.


## Step 3: The "Secret Sauce" - Google Cloud Setup

After a successful installation, you'll want to log in by running `gemini auth login`. But you might immediately hit another wall:

```
Failed to login. Message: This account requires setting the GOOGLE_CLOUD_PROJECT env var.
```

This is the most important step that many tutorials miss. The Gemini CLI needs to be linked to a specific project in Google Cloud.

Solution:

1.  Create a Google Cloud Project: Go to the [Google Cloud Console](https://console.cloud.google.com/). If you don't have a project, create a new one. Give it a memorable name (e.g., "My Gemini Stuff"). Once created, you will see a Project ID (e.g., `my-gemini-stuff-12345`). Copy this ID.

2.  Set the Environment Variable on Windows:
    *   Open the Start Menu and type "Environment Variables".
    *   Select "Edit the system environment variables".
    *   In the window that opens, click the "Environment Variables..." button.
    *   In the top section ("User variables"), click "New...".
    *   For Variable name, enter: `GOOGLE_CLOUD_PROJECT`
    *   For Variable value, paste your Project ID.
    *   Click OK on all windows to close them.
    *   Restart your terminal or your entire computer for the changes to take effect.

<p align="center"><img src="/images/environment-variables.png" alt="Gemini CLI Logo"></p>

## Step 4: Enable the API

You're almost there. You try to run a command, and you get one last error:

```
Error: 403, SERVICE_DISABLED: Gemini for Google Cloud API has not been used in project [your-project-id] before or it is disabled. Enable it by visiting [a long URL]
```

Solution:
Your project exists, but the specific Gemini API is not turned on for it.

1.  Go back to the [Google Cloud Console](https://console.cloud.google.com/).
2.  Make sure your project is selected at the top of the page.
3.  In the search bar, type "API & Services" and go to that page.
4.  Click on "+ ENABLE APIS AND SERVICES".
5.  Search for "Vertex AI API".
6.  Click on it and then click the big blue "ENABLE" button. Wait a minute for it to activate.

## Step 5: Success!

Now, you can finally run the login command without any issues:

```bash
gemini auth login
```

<p align="center"><img src="/images/gemini-cli.png" alt="Gemini CLI Logo"></p>

This will open a browser window for you to log in with your Google account. After that, your Gemini CLI will be fully configured and ready to use.

I hope this detailed, real-world guide saves you the hours of frustration I went through. It's a perfect example of how the "simple" things in tech often have hidden depths.
