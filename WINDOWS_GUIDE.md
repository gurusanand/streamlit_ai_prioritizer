# 🪟 Windows Setup Guide - Step by Step

Complete guide for running the Agentic AI Prioritization Framework on Windows.

## 📋 Prerequisites Checklist

Before you begin, you'll need:

- [ ] Windows 10 or Windows 11
- [ ] Internet connection
- [ ] Administrator access (for Python installation)
- [ ] OpenAI API key (optional, but recommended)

## 🔧 Step-by-Step Installation

### Step 1: Install Python

1. **Download Python**
   - Go to https://www.python.org/downloads/
   - Click the yellow "Download Python 3.x.x" button
   - Save the installer file

2. **Run the Installer**
   - Double-click the downloaded file
   - ⚠️ **IMPORTANT:** Check the box "Add Python to PATH"
   - Click "Install Now"
   - Wait for installation to complete
   - Click "Close"

3. **Verify Installation**
   - Press `Win + R`
   - Type `cmd` and press Enter
   - In the Command Prompt, type:
     ```cmd
     python --version
     ```
   - You should see something like: `Python 3.11.x`
   - Type:
     ```cmd
     pip --version
     ```
   - You should see pip version information

### Step 2: Extract the Project

1. **Locate the ZIP file**
   - Find `streamlit_ai_prioritizer.zip` in your Downloads folder

2. **Extract the files**
   - Right-click the ZIP file
   - Select "Extract All..."
   - Choose a location (e.g., `C:\Projects\`)
   - Click "Extract"

3. **Note the folder path**
   - Remember where you extracted it
   - Example: `C:\Projects\streamlit_ai_prioritizer\`

### Step 3: Install Dependencies

1. **Open Command Prompt in the project folder**
   
   **Method 1 (Easy):**
   - Open the extracted folder in File Explorer
   - Click in the address bar (where it shows the path)
   - Type `cmd` and press Enter
   
   **Method 2:**
   - Press `Win + R`
   - Type `cmd` and press Enter
   - Type: `cd C:\Projects\streamlit_ai_prioritizer` (use your actual path)
   - Press Enter

2. **Install Python packages**
   ```cmd
   pip install -r requirements.txt
   ```
   
   - This will take a few minutes
   - You'll see progress as packages are downloaded and installed
   - Wait for it to complete

3. **Verify installation**
   ```cmd
   pip list
   ```
   - You should see streamlit, pandas, plotly, openai, and other packages

### Step 4: Configure OpenAI API Key (Optional but Recommended)

1. **Get an OpenAI API Key**
   - Go to https://platform.openai.com/
   - Sign up or log in
   - Go to https://platform.openai.com/api-keys
   - Click "Create new secret key"
   - Copy the key (starts with `sk-`)
   - ⚠️ Save it somewhere safe - you can't see it again!

2. **Create .env file**
   - In the project folder, find `env_example.txt`
   - Right-click it → "Open with" → "Notepad"
   - Replace `sk-your-openai-api-key-here` with your actual API key
   - Click "File" → "Save As"
   - Change "Save as type" to "All Files"
   - Name it `.env` (with the dot at the beginning)
   - Click "Save"

3. **Verify the .env file**
   - In File Explorer, you should now see a `.env` file
   - If you don't see it, make sure "File name extensions" is checked in View menu

### Step 5: Run the Application

1. **Start the app**
   - In the Command Prompt (still in the project folder), type:
     ```cmd
     streamlit run app.py
     ```
   - Press Enter

2. **Wait for startup**
   - You'll see some messages
   - Look for: "You can now view your Streamlit app in your browser"
   - The app should automatically open in your default browser

3. **If browser doesn't open automatically**
   - Look for the URL in the Command Prompt
   - It will say something like: "Local URL: http://localhost:8501"
   - Copy this URL and paste it in your browser

4. **Success!**
   - You should see the Agentic AI Prioritization Framework home page
   - The Command Prompt window must stay open while using the app

### Step 6: Using the Application

1. **Create your first use case**
   - Click "➕ New Use Case" in the sidebar
   - Fill in the details
   - Click "Create Use Case"

2. **Start assessment**
   - Go to "📊 Dashboard"
   - Click "📝 Start Assessment"
   - Score all 31 dimensions
   - Click "✅ Submit Assessment"

3. **View results**
   - Go to "📈 Results"
   - See your scores, insights, and recommendations

## 🛑 Stopping the Application

1. Go to the Command Prompt window
2. Press `Ctrl + C`
3. Type `Y` when asked to terminate
4. Close the Command Prompt window

## 🔄 Running the Application Again

1. Open Command Prompt in the project folder (see Step 3.1)
2. Type: `streamlit run app.py`
3. Press Enter
4. Your browser will open automatically

## 🎯 Creating a Desktop Shortcut

1. **Create a batch file**
   - In the project folder, right-click → New → Text Document
   - Name it `START_APP.bat` (change extension from .txt to .bat)
   - Right-click the .bat file → Edit
   - Add these lines:
     ```batch
     @echo off
     cd /d "%~dp0"
     streamlit run app.py
     pause
     ```
   - Save and close

2. **Create shortcut**
   - Right-click `START_APP.bat` → "Create shortcut"
   - Drag the shortcut to your Desktop
   - Double-click the shortcut to start the app!

## 🐛 Common Issues and Solutions

### Issue 1: "Python is not recognized"

**Problem:** Command Prompt says "python is not recognized"

**Solution:**
1. Python wasn't added to PATH during installation
2. Uninstall Python
3. Reinstall and make sure to check "Add Python to PATH"

### Issue 2: "pip is not recognized"

**Problem:** Command Prompt says "pip is not recognized"

**Solution:**
1. Try using `python -m pip` instead of `pip`
2. Example: `python -m pip install -r requirements.txt`

### Issue 3: Permission Errors

**Problem:** "Access denied" or "Permission error"

**Solution:**
1. Right-click Command Prompt
2. Select "Run as administrator"
3. Navigate to project folder and try again

### Issue 4: Port Already in Use

**Problem:** "Port 8501 is already in use"

**Solution:**
1. Close any other Streamlit applications
2. Or use a different port:
   ```cmd
   streamlit run app.py --server.port 8502
   ```

### Issue 5: OpenAI API Errors

**Problem:** "Invalid API key" or "Insufficient credits"

**Solution:**
1. Check your API key in `.env` file is correct
2. Verify you have credits at https://platform.openai.com/account/usage
3. The app will still work without OpenAI - just with basic insights

### Issue 6: Can't See .env File

**Problem:** Can't find or create .env file

**Solution:**
1. In File Explorer, click "View" tab
2. Check "File name extensions"
3. Check "Hidden items"
4. Now you can see and create .env files

### Issue 7: Browser Doesn't Open

**Problem:** App starts but browser doesn't open

**Solution:**
1. Look at the Command Prompt for the URL
2. Usually: http://localhost:8501
3. Copy and paste this URL into your browser manually

## 📊 Data Storage

- All your data is stored in `data/assessments.db`
- This is a SQLite database file
- To backup your data, copy this file
- To reset everything, delete this file (it will be recreated)

## 🔒 Security Tips

1. **Keep your .env file private**
   - Never share it
   - Don't upload it to cloud storage
   - Don't commit it to Git

2. **Protect your OpenAI API key**
   - Keep it secret
   - Monitor usage at https://platform.openai.com/account/usage
   - Set spending limits in OpenAI dashboard

3. **Backup your data**
   - Regularly copy `data/assessments.db`
   - Store backups in a safe location

## 🎓 Next Steps

Once you have the app running:

1. Read the main README.md for feature details
2. Explore the About page in the app
3. Create a test use case to familiarize yourself
4. Review the 31 dimensions in the framework

## 📞 Getting Help

If you're still having trouble:

1. Check the main README.md troubleshooting section
2. Make sure Python 3.8+ is installed
3. Verify all packages installed correctly: `pip list`
4. Check the Command Prompt for error messages
5. Try running with: `streamlit run app.py --logger.level=debug`

## ✅ Quick Checklist

Before asking for help, verify:

- [ ] Python 3.8+ is installed
- [ ] Python is in PATH (can run `python --version`)
- [ ] All packages installed (`pip install -r requirements.txt`)
- [ ] In correct directory (project folder)
- [ ] .env file created (if using OpenAI)
- [ ] No other apps using port 8501

---

**You're all set!** Enjoy using the Agentic AI Prioritization Framework! 🎉

