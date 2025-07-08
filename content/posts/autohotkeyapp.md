---
title: "Auto Keyboard Language Switching on Windows"
date: 2025-07-08
description: "Learn how to use a simple AutoHotkey script to automatically switch keyboard layouts based on the application you're using in Windows. Boost your productivity today!"
share_image: "/images/build-hugo-2.png"
tags: ["AutoHotkey", "keyboard layout", "productivity", "Windows", "VS Code", "Firefox", "automation"]
categories: ["Guides"]
ShowToc: true
showBreadcrumbs: true
comments: true
---

### The Problem: Manual Language Switching

In my daily workflow, I often use AI assistants like ChatGPT and Gemini, and it so happens that I communicate with them in **Russian**. But all my notes and code in **Visual Studio Code** are in **English**.

This might be different for you, but the essence of the problem remains the same. After chatting with an AI assistant, I have to switch my language. Since I have three languages installed, I sometimes have to toggle twice to get to the right one, which is frustrating.

Yes, I know you can set up a single key for switching layouts, like using Caps Lock on iPadOS. But that wasn't my goal. I wanted to **fully automate** the process. It turns out I'm not the only one with this problem, and there are several solutions. You could install a special plugin for VS Code to force a specific layout, or use a dedicated Windows app. I'll tell you about one such app, share a working configuration that you can easily adapt, and walk you through how to set it all up.

### The Tool: AutoHotkey

The application is called [AutoHotkey](https://www.autohotkey.com/). It's a free, powerful automation tool for Windows. We'll be using **version 2.0**, which you can download from their official website.

For our example, let's set up a simple rule:
*   **VS Code**: Automatically switch to the **English** layout.
*   **Chrome/Firefox**: Automatically switch to the **Russian** layout.

---

### A Word From Your AI Assistant

As an AI, I see firsthand how small optimizations can lead to significant productivity gains. Automating repetitive tasks like switching keyboard layouts is a perfect example. It offloads a minor but frequent cognitive burden, freeing up your mental energy to focus on what truly matters: the creative and complex aspects of your work. By creating a seamless environment where the tools adapt to your context, you're not just saving a few keystrokes; you're paving the way for a more focused and uninterrupted workflow.

---

### Step 1: Find Your Keyboard Layout IDs

First, we need to get the unique hexadecimal ID for each of your keyboard layouts.

1.  Make sure [AutoHotkey](https://www.autohotkey.com/) is installed.
2.  Create a new file named `GetLayoutID.ahk`.
3.  Paste the following code into it:

    ```autohotkey
    #Requires AutoHotkey v2.0
    MsgBox Format("Current layout ID: {:#x}", DllCall("GetKeyboardLayout", "UInt", DllCall("GetWindowThreadProcessId", "UInt", WinGetID("A"), "UInt*", 0)))
    ```
4.  Save the file. Now, switch to your English layout and double-click the `GetLayoutID.ahk` file. A message box will pop up with its ID.
5.  Write it down. Then, switch to your Russian layout and run the script again. Write that ID down too.

They will look something like this:
*   English (US): `0x4090409`
*   Russian: `0x4190419`

### Step 2: Create the Automation Script

Now it's time to write the main script. Create a new file named `LayoutSwitcher.ahk` and paste this code into it. The comments inside are in English for clarity.

```autohotkey
#Requires AutoHotkey v2.0
#Persistent

; === CONFIGURATION ===

; 1. Specify your layout IDs here.
;    Run the GetLayoutID.ahk script to find them.
global english_layout := 0x4090409 ; Example for English (US)
global russian_layout := 0x4190419 ; Example for Russian

; 2. Add the executable files of your programs here (.exe)
global english_apps := ["Code.exe"]
global russian_apps := ["firefox.exe", "chrome.exe"]


; === SCRIPT LOGIC (no changes needed below) ===

SetTimer(CheckActiveWindow, 250) ; Check the active window every 250 ms

CheckActiveWindow() {
    static last_window_id := 0
    current_window_id := WinGetID("A")

    ; If the window has not changed, do nothing.
    ; This allows you to manually change the layout without the script interfering.
    if (current_window_id == last_window_id) {
        return
    }
    
    last_window_id := current_window_id
    process_name := WinGetProcessName("A")

    ; Check for English apps
    for app in english_apps {
        if (process_name == app) {
            SwitchLayout(english_layout)
            return
        }
    }

    ; Check for Russian apps
    for app in russian_apps {
        if (process_name == app) {
            SwitchLayout(russian_layout)
            return
        }
    }
}

SwitchLayout(layout_id) {
    ; Sends a message to the active window to change the language
    PostMessage(0x50, 0, layout_id, , "A")
}
```

**How to customize it:**
1.  Update the `english_apps` and `russian_apps` lists with the process names for your programs. You can find them in the Windows Task Manager under the "Details" tab.
2.  Replace the example `0x...` values for `english_layout` and `russian_layout` with the actual IDs you found in Step 1.

### Step 3: Run the Script

Save the `LayoutSwitcher.ahk` file. Double-click it to run. You should see a new AutoHotkey icon in your system tray (the area by the clock). This means the script is active.

Now, try switching between VS Code and your browser. The keyboard layout should change automatically!

**Important Note:** This script automates the initial switch. If you are in Chrome (and the layout switched to Russian) and then manually switch back to English to type a URL, the script will not interfere. It only triggers the switch once when the application window becomes active.

### Bonus: Run the Script on Windows Startup

To make this truly automatic, let's make the script run when your computer starts.

1.  Press `Win + R` to open the Run dialog.
2.  Type `shell:startup` and press Enter. This opens your personal Startup folder.
3.  Create a shortcut to your `LayoutSwitcher.ahk` script and move it into this folder.

That's it! Now the script will launch every time you log in, and you can get straight to work. I think this is an interesting method that you can further improve for your own goals and apply different rules for other programs.