# 🤖 Agentic AI Prioritization Framework - Streamlit Edition

A comprehensive Python-based web application for evaluating and prioritizing AI use cases using a 31-dimension assessment framework.

## ✨ Features

- 📊 **31 Evaluation Dimensions** across 6 major categories
- 🤖 **AI-Powered Insights** using OpenAI (optional)
- 📈 **Interactive Visualizations** with Plotly
- 💾 **SQLite Database** for data persistence
- 📥 **Export Capabilities** (CSV, JSON)
- 🎨 **Beautiful UI** with custom styling
- 🚀 **Easy to Deploy** - runs on any platform with Python

## 🎯 Quick Start

### Prerequisites

- **Python 3.8 or higher**
- **pip** (Python package installer)
- **OpenAI API Key** (optional, for AI-powered insights)

### Installation

#### Windows

1. **Install Python**
   - Download from https://www.python.org/downloads/
   - During installation, check "Add Python to PATH"

2. **Extract the ZIP file** to a folder

3. **Open Command Prompt** in the project folder
   - Right-click in the folder → "Open in Terminal" or "Open Command Prompt here"

4. **Install dependencies**
   ```cmd
   pip install -r requirements.txt
   ```

5. **Configure OpenAI API Key** (Optional)
   - Rename `env_example.txt` to `.env`
   - Edit `.env` and add your OpenAI API key
   - If you skip this, the app will still work with basic insights

6. **Run the application**
   ```cmd
   streamlit run app.py
   ```

7. **Open your browser**
   - The app will automatically open at http://localhost:8501
   - If not, manually navigate to http://localhost:8501

#### Mac/Linux

```bash
# Install dependencies
pip3 install -r requirements.txt

# (Optional) Configure OpenAI API key
cp env_example.txt .env
nano .env  # Edit and add your API key

# Run the application
streamlit run app.py
```

## 📁 Project Structure

```
streamlit_ai_prioritizer/
├── app.py                      # Main application
├── requirements.txt            # Python dependencies
├── env_example.txt            # Environment variables template
├── README.md                  # This file
├── WINDOWS_GUIDE.md           # Detailed Windows setup guide
├── data/
│   ├── framework_data.json    # 31-dimension framework data
│   └── assessments.db         # SQLite database (auto-created)
└── utils/
    ├── __init__.py
    ├── framework_loader.py    # Framework data loader
    ├── database.py            # Database operations
    ├── ai_insights.py         # AI insights generator
    └── calculations.py        # Score calculations
```

## 🎓 How to Use

### 1. Create a Use Case

- Navigate to **"➕ New Use Case"** in the sidebar
- Fill in the use case details:
  - Use Case ID (e.g., UC-001)
  - Name
  - Description
  - Business Unit
  - Process Owner
- Click **"Create Use Case"**

### 2. Start Assessment

- Go to **"📊 Dashboard"**
- Click **"📝 Start Assessment"** on your use case
- Score all 31 dimensions on a scale of 1-5
- Each dimension has detailed descriptions for each score level

### 3. View Results

- After completing all dimensions, click **"✅ Submit Assessment"**
- The app will:
  - Calculate overall and category scores
  - Generate AI-powered insights (if OpenAI key is configured)
  - Provide actionable recommendations
- Navigate to **"📈 Results"** to view:
  - Overall readiness score
  - Category breakdown
  - Strengths and challenges
  - AI analysis
  - Detailed scoring table

### 4. Export Results

- From the Results page, you can export to:
  - **CSV** - For spreadsheet analysis
  - **JSON** - For data integration

## 📊 Assessment Categories

1. **Strategic & Business** (5 dimensions)
   - Business impact, strategic alignment, time to market, ROI, scalability

2. **Risk & Compliance** (5 dimensions)
   - AI risk, regulatory compliance, data privacy, operational risk, ethics

3. **Technical & Implementation** (6 dimensions)
   - Complexity, data readiness, integration, infrastructure, vendor maturity

4. **Resource & Investment** (4 dimensions)
   - Investment required, resource availability, skills gap, ongoing costs

5. **Organizational & Change** (4 dimensions)
   - Readiness, stakeholder alignment, change management, adoption

6. **Human-in-Loop & Autonomy** (3 dimensions)
   - Autonomy level, human oversight, explainability

7. **Process & Operational** (4 dimensions)
   - Standardization, volume, criticality, current efficiency

## 🔧 Configuration

### OpenAI API Key (Optional)

The application can work with or without an OpenAI API key:

**With OpenAI API Key:**
- Get AI-powered insights and recommendations
- Intelligent analysis of your assessment
- Customized suggestions for improvement

**Without OpenAI API Key:**
- Basic insights based on score analysis
- Standard recommendations
- All other features work normally

To configure:
1. Get an API key from https://platform.openai.com/api-keys
2. Rename `env_example.txt` to `.env`
3. Add your key: `OPENAI_API_KEY=sk-your-key-here`
4. Restart the application

### Database

- Uses SQLite (no setup required)
- Database file: `data/assessments.db`
- Automatically created on first run
- Stores all use cases and assessments

## 🐛 Troubleshooting

### "Python not found"
- Install Python from https://www.python.org/
- Make sure "Add Python to PATH" was checked during installation
- Restart your terminal/command prompt

### "Module not found" errors
- Run: `pip install -r requirements.txt`
- Make sure you're in the project directory

### "Port 8501 already in use"
- Close other Streamlit applications
- Or specify a different port: `streamlit run app.py --server.port 8502`

### OpenAI API errors
- Check your API key is correct in `.env`
- Ensure you have credits in your OpenAI account
- The app will fall back to basic insights if API fails

### Database errors
- Delete `data/assessments.db` to reset the database
- The app will recreate it automatically

## 🚀 Advanced Usage

### Running on a Different Port

```bash
streamlit run app.py --server.port 8502
```

### Running on Network

To access from other devices on your network:

```bash
streamlit run app.py --server.address 0.0.0.0
```

### Custom Theme

Edit `.streamlit/config.toml` to customize colors and appearance.

## 📦 Deployment Options

### Local Deployment
- Follow the Quick Start guide above
- Perfect for personal use or small teams

### Cloud Deployment

**Streamlit Community Cloud (Free):**
1. Push code to GitHub
2. Visit https://share.streamlit.io/
3. Connect your repository
4. Add OpenAI API key in Secrets

**Other Options:**
- Heroku
- AWS EC2
- Google Cloud Run
- Azure App Service

## 🔒 Security Notes

- Never commit `.env` file to version control
- Keep your OpenAI API key secure
- Database contains sensitive assessment data
- Use HTTPS in production deployments

## 📄 License

MIT License - Feel free to use and modify for your needs.

## 🆘 Support

For issues or questions:
1. Check the troubleshooting section above
2. Review the WINDOWS_GUIDE.md for detailed setup instructions
3. Ensure all prerequisites are installed correctly

## 🎉 Credits

- **Framework:** Agentic AI Prioritization Framework
- **Built with:** Streamlit, Plotly, OpenAI
- **Database:** SQLite

---

**Ready to get started?**

```bash
pip install -r requirements.txt
streamlit run app.py
```

Then open http://localhost:8501 in your browser! 🚀

