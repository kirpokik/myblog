---
title: "VLC + Android TV: Stream Shared PC Folders"
date: 2025-05-31
description: "Learn how to share a folder on your local network and stream its content on an Android TV box or smart TV using VLC, without the need for internet."
tags: ["vlc", "network", "windows", "streaming", "tvbox"]
categories: ["build-log"]
category: "Blog"
comments: true
---

Streaming videos directly from your PC to your Android TV box or Smart TV can be easy and efficient when using VLC Media Player and a shared folder on your local network. This guide explains how to set it up step-by-step — no internet required.

---

### What You Need

- A Windows PC with your video files.
- A Wi-Fi router (no internet needed).
- A TV or Android TV box with VLC installed.
- VLC Media Player installed on both PC (optional) and TV box.

---

### Step 1: Share a Folder on Your PC (Windows)

1. Choose the folder with your movies (e.g., `D:\Movies`).
2. Right-click on it → **Properties** → **Sharing** tab.
3. Click **"Share…"** → select **"Everyone"** from the dropdown → click **Add**.
4. Set permission level to **Read** (or Read/Write if you want to manage files).
5. Click **Share**, then **Done**.
6. Go to **Advanced Sharing…** → tick **"Share this folder"**.
7. Click **Permissions**, ensure **Everyone** has at least Read access.
8. Click **OK** and close all dialogs.

Now the folder is accessible over your local network.

---

### Step 2: Find Your PC's IP Address

1. Open **Command Prompt** (`Win + R`, type `cmd`, press Enter).
2. Type: ipconfig

3. Look for the line under your active connection:
Example: `IPv4 Address. . . . . . . . . . . : 192.168.1.42`

Write this IP down.

---

### Step 3: Access the Shared Folder via VLC on TV Box

1. Open **VLC** on your Android TV / TV box.
2. Go to **Browsing → Local Network → Windows Network (SMB)**.
3. Navigate through the workgroup until you see your PC.
- If VLC asks for credentials, enter:
  - **Username:** `guest` or leave blank
  - **Password:** leave blank
- If this doesn’t work, use your Windows user and password.

4. Find the folder you shared (`Movies`).
5. Open and play your files!

---

### ✅ Tips

- VLC on Android TV caches folders — if the folder doesn’t appear immediately, restart the app.
- Ensure both devices (TV and PC) are **connected to the same router**.
- Disable Windows Firewall temporarily if you're having access issues (or create a rule to allow SMB).

---

### 🔒 Bonus: Securing Your Share

If you’re worried about privacy:

- Avoid sharing with "Everyone" — instead, create a specific user and set permissions.
- Use password protection for shared folders.
- Don’t connect this setup to the internet if security is a concern.

---

With this setup, you can enjoy all your videos directly on your big screen without copying them or using any cloud storage. Fast, simple, and local!


