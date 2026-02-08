# 🛡️ NET FRED - Advanced Cybersecurity AI Assistant

<div align="center">

![NET FRED Banner](https://img.shields.io/badge/NET%20FRED-Cybersecurity%20AI-00f7ff?style=for-the-badge&logo=security&logoColor=white)
[![FastAPI](https://img.shields.io/badge/FastAPI-0.109.0-009688?style=for-the-badge&logo=fastapi&logoColor=white)](https://fastapi.tiangolo.com/)
[![Python](https://img.shields.io/badge/Python-3.8+-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![Groq](https://img.shields.io/badge/Groq-LLaMA%203.1-FF6B6B?style=for-the-badge)](https://groq.com/)
[![License](https://img.shields.io/badge/License-MIT-green?style=for-the-badge)](LICENSE)

**An elite cybersecurity expert powered by AI, providing real-time threat analysis, security guidance, and incident response assistance.**

[Features](#-features) • [Installation](#-installation) • [Usage](#-usage) • [API Documentation](#-api-documentation) • [Configuration](#-configuration)

</div>

---

## 📋 Table of Contents

- [Overview](#-overview)
- [Features](#-features)
- [Technology Stack](#-technology-stack)
- [Prerequisites](#-prerequisites)
- [Installation](#-installation)
- [Configuration](#-configuration)
- [Usage](#-usage)
- [API Documentation](#-api-documentation)
- [Project Structure](#-project-structure)
- [Security Features](#-security-features)
- [Troubleshooting](#-troubleshooting)
- [Contributing](#-contributing)
- [License](#-license)

---

## 🌟 Overview

**NET FRED** (Network Forensics, Response, and Ethical Defense) is an advanced AI-powered cybersecurity assistant built with FastAPI and powered by Groq's LLaMA 3.1 model. It provides expert-level cybersecurity guidance, threat analysis, and incident response recommendations through an intuitive web interface with real-time streaming responses.

### Key Capabilities

- 🔍 **Threat Detection & Analysis** - Real-time security threat assessment
- 🛡️ **Penetration Testing Guidance** - OWASP and CVE-based vulnerability analysis
- 🔐 **Security Architecture** - Zero-trust implementation and network security design
- 🦠 **Malware Analysis** - Reverse engineering and threat intelligence
- ☁️ **Cloud Security** - AWS, Azure, GCP security best practices
- 📊 **Compliance** - ISO 27001, NIST, GDPR, SOC 2 guidance
- 🚨 **Incident Response** - Step-by-step breach response procedures

---

## ✨ Features

### 🤖 AI-Powered Intelligence
- **LLaMA 3.1 8B Model** via Groq for lightning-fast responses
- **Streaming Responses** for real-time interaction
- **Context-Aware Conversations** with session management
- **Threat Level Assessment** (Low, Medium, High, Critical)

### 🎨 Modern UI/UX
- **Cyberpunk-Inspired Design** with animated particles
- **Real-Time Threat Monitor** with visual indicators
- **Quick Action Buttons** for common security queries
- **Responsive Layout** for desktop and mobile
- **Dark Mode Interface** optimized for security operations

### 🔒 Security-First Design
- **Environment Variable Protection** for API keys
- **CORS Middleware** for secure cross-origin requests
- **Session Isolation** for multi-user support
- **Ethical AI Boundaries** - No malicious code generation

### ⚡ Performance
- **Asynchronous Processing** with FastAPI
- **Server-Sent Events (SSE)** for streaming
- **Optimized Response Times** with Groq infrastructure
- **In-Memory Session Storage** (production-ready for Redis/DB)

---

## 🛠️ Technology Stack

| Component | Technology | Version |
|-----------|-----------|---------|
| **Backend Framework** | FastAPI | 0.109.0 |
| **ASGI Server** | Uvicorn | 0.27.0 |
| **AI Model** | Groq (LLaMA 3.1 8B) | 0.4.2 |
| **Data Validation** | Pydantic | 2.5.3 |
| **Environment Management** | python-dotenv | 1.0.0 |
| **Frontend** | HTML5, CSS3, Vanilla JS | - |
| **Language** | Python | 3.8+ |

---

## 📦 Prerequisites

Before installing NET FRED, ensure you have:

- **Python 3.8 or higher** installed
- **pip** package manager
- **Groq API Key** (Get yours at [console.groq.com](https://console.groq.com/keys))
- **Git** (optional, for cloning)

---

## 🚀 Installation

### Step 1: Clone the Repository

```bash
git clone https://github.com/yourusername/AI_bot.git
cd AI_bot
```

Or download the ZIP file and extract it.

### Step 2: Create Virtual Environment (Recommended)

```bash
# Create virtual environment
python -m venv venv

# Activate virtual environment
# On Linux/Mac:
source venv/bin/activate

# On Windows:
venv\Scripts\activate
```

### Step 3: Install Dependencies

```bash
pip install -r requirements.txt
```

**Dependencies installed:**
- `fastapi==0.109.0` - Modern web framework
- `uvicorn[standard]==0.27.0` - ASGI server
- `groq==0.4.2` - Groq AI client
- `pydantic==2.5.3` - Data validation
- `python-multipart==0.0.6` - Form data parsing
- `python-dotenv==1.0.0` - Environment variable management

### Step 4: Configure Environment Variables

```bash
# Copy the example environment file
cp .env.example .env

# Edit .env and add your Groq API key
nano .env  # or use your preferred editor
```

**`.env` file contents:**
```env
# Groq API Configuration
# Get your API key from: https://console.groq.com/keys
GROQ_API_KEY=your_actual_groq_api_key_here
```

⚠️ **IMPORTANT**: Never commit your `.env` file to version control!

---

## ⚙️ Configuration

### Environment Variables

| Variable | Description | Required | Default |
|----------|-------------|----------|---------|
| `GROQ_API_KEY` | Your Groq API key for LLaMA access | ✅ Yes | None |

### Application Settings

You can modify these settings in `main.py`:

```python
# Model Configuration
model="llama-3.1-8b-instant"  # AI model to use
max_tokens=1500                # Maximum response length
temperature=0.3                # Response creativity (0.0-1.0)
top_p=0.9                      # Nucleus sampling parameter

# Server Configuration
host="0.0.0.0"                 # Listen on all interfaces
port=8000                      # Server port
```

### CORS Configuration

By default, CORS is configured to allow all origins. For production, restrict this:

```python
app.add_middleware(
    CORSMiddleware,
    allow_origins=["https://yourdomain.com"],  # Specific domains
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
```

---

## 🎯 Usage

### Starting the Server

#### Development Mode

```bash
# Run with auto-reload
python main.py
```

Or using uvicorn directly:

```bash
uvicorn main:app --reload --host 0.0.0.0 --port 8000
```

#### Production Mode

```bash
uvicorn main:app --host 0.0.0.0 --port 8000 --workers 4
```

### Accessing the Application

Once the server is running, open your browser and navigate to:

```
http://localhost:8000
```

You should see the NET FRED interface with:
- 🛡️ Cybersecurity-themed UI
- 💬 Chat interface
- 📊 Threat level monitor
- ⚡ Quick action buttons

### Using the Chat Interface

1. **Type your security question** in the input field
2. **Press Enter** or click **Send**
3. **Watch the AI respond** in real-time with streaming
4. **Monitor threat levels** in the sidebar
5. **Use quick actions** for common queries

### Quick Action Examples

- 🔍 **Security Scan Tips** - Best practices for security scanning
- 📧 **Phishing Detection** - How to identify phishing attempts
- 🔐 **Password Security** - Password management best practices
- 🛡️ **Firewall Configuration** - Firewall setup guidance
- ⚠️ **Vulnerability Assessment** - Vulnerability testing procedures
- 🚨 **Incident Response** - Breach response protocols

---

## 📡 API Documentation

### Interactive API Docs

FastAPI provides automatic interactive documentation:

- **Swagger UI**: http://localhost:8000/docs
- **ReDoc**: http://localhost:8000/redoc

### Endpoints

#### 1. Root Endpoint

```http
GET /
```

**Description**: Serves the main HTML interface

**Response**: HTML page

---

#### 2. Chat Endpoint (Streaming)

```http
POST /chat
```

**Description**: Send a message and receive streaming AI responses

**Request Body**:
```json
{
  "content": "How do I detect SQL injection vulnerabilities?",
  "session_id": "session_12345"
}
```

**Response**: Server-Sent Events (SSE) stream

```
data: {"content": "SQL", "done": false}
data: {"content": " injection", "done": false}
...
data: {"content": "", "done": true}
```

**Example using cURL**:
```bash
curl -X POST http://localhost:8000/chat \
  -H "Content-Type: application/json" \
  -d '{
    "content": "Explain XSS attacks",
    "session_id": "test_session"
  }'
```

---

#### 3. Threat Analysis Endpoint

```http
POST /analyze-threat
```

**Description**: Quick threat analysis without streaming

**Request Body**:
```json
{
  "content": "Suspicious login attempts from unknown IP",
  "session_id": "session_12345"
}
```

**Response**:
```json
{
  "analysis": "Threat Level: High\nCategory: Unauthorized Access\n..."
}
```

---

#### 4. Clear Session

```http
DELETE /clear-session/{session_id}
```

**Description**: Clear conversation history for a session

**Parameters**:
- `session_id` (path): Session identifier

**Response**:
```json
{
  "status": "cleared",
  "session_id": "session_12345"
}
```

---

#### 5. Health Check

```http
GET /health
```

**Description**: Check if the service is operational

**Response**:
```json
{
  "status": "operational",
  "service": "CyberGuard AI"
}
```

---

## 📁 Project Structure

```
AI_bot/
├── main.py                 # FastAPI application & API endpoints
├── index.html              # Frontend UI (cyberpunk design)
├── requirements.txt        # Python dependencies
├── .env                    # Environment variables (API keys)
├── .env.example            # Example environment file
├── .gitignore              # Git ignore rules
├── README.md               # This file
├── __pycache__/            # Python cache (auto-generated)
└── venv/                   # Virtual environment (if created)
```

### Key Files

#### `main.py` (Backend)
- FastAPI application setup
- Groq AI client initialization
- Chat streaming logic
- Session management
- API endpoints

#### `index.html` (Frontend)
- Responsive cybersecurity-themed UI
- Real-time chat interface
- Animated background particles
- Threat level visualization
- Quick action buttons

#### `requirements.txt`
- All Python package dependencies
- Pinned versions for reproducibility

#### `.env`
- **CRITICAL**: Contains API keys
- **Never commit to Git**
- Use `.env.example` as template

---

## 🔐 Security Features

### System Prompt Safeguards

NET FRED is designed with ethical boundaries:

✅ **Allowed**:
- Defensive security strategies
- Vulnerability detection guidance
- Security best practices
- Incident response procedures
- Compliance recommendations

❌ **Prohibited**:
- Malicious code generation
- Unauthorized access assistance
- Exploit creation for illegal purposes
- Attack tool development

### Threat Level Assessment

Responses are automatically analyzed for threat indicators:

| Level | Icon | Indicator | Percentage |
|-------|------|-----------|------------|
| 🟢 Low | Green | Minimal risk | 20% |
| 🟡 Medium | Yellow | Moderate concern | 50% |
| 🟠 High | Orange | Significant threat | 75% |
| 🔴 Critical | Red | Severe danger | 95% |

### API Key Protection

- API keys stored in `.env` file
- `.gitignore` prevents accidental commits
- Environment variable validation on startup
- No hardcoded credentials

---

## 🐛 Troubleshooting

### Common Issues

#### 1. "GROQ_API_KEY not found" Error

**Problem**: API key not configured

**Solution**:
```bash
# Ensure .env file exists
cp .env.example .env

# Edit .env and add your key
nano .env
```

#### 2. "ModuleNotFoundError"

**Problem**: Dependencies not installed

**Solution**:
```bash
pip install -r requirements.txt
```

#### 3. "Address already in use"

**Problem**: Port 8000 is occupied

**Solution**:
```bash
# Use a different port
uvicorn main:app --port 8001

# Or kill the process using port 8000
lsof -ti:8000 | xargs kill -9  # Linux/Mac
```

#### 4. "index.html not found"

**Problem**: HTML file not in the same directory as `main.py`

**Solution**:
```bash
# Ensure both files are in the same directory
ls -la
# Should show both main.py and index.html
```

#### 5. CORS Errors

**Problem**: Cross-origin request blocked

**Solution**: Check CORS configuration in `main.py`:
```python
allow_origins=["*"]  # Development
# Or specify your domain for production
```

### Debug Mode

Enable detailed logging:

```bash
uvicorn main:app --log-level debug
```

---

## 🤝 Contributing

Contributions are welcome! Here's how you can help:

1. **Fork the repository**
2. **Create a feature branch**: `git checkout -b feature/amazing-feature`
3. **Commit your changes**: `git commit -m 'Add amazing feature'`
4. **Push to the branch**: `git push origin feature/amazing-feature`
5. **Open a Pull Request**

### Development Guidelines

- Follow PEP 8 style guide
- Add docstrings to functions
- Test new features thoroughly
- Update documentation as needed

---

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

## 🙏 Acknowledgments

- **Groq** for providing ultra-fast LLaMA inference
- **FastAPI** for the excellent web framework
- **LLaMA 3.1** by Meta for the powerful language model
- **Cybersecurity Community** for inspiration and best practices

---

## 📞 Support

If you encounter issues or have questions:

1. Check the [Troubleshooting](#-troubleshooting) section
2. Review the [API Documentation](#-api-documentation)
3. Open an issue on GitHub
4. Contact the maintainer

---

## 🚀 Future Enhancements

- [ ] Redis/Database integration for persistent sessions
- [ ] User authentication and authorization
- [ ] Multi-model support (GPT-4, Claude, etc.)
- [ ] Export chat history to PDF/Markdown
- [ ] Voice input/output capabilities
- [ ] Integration with security tools (Nmap, Metasploit, etc.)
- [ ] Custom threat intelligence feeds
- [ ] Team collaboration features

---

<div align="center">

**Built with ❤️ for the Cybersecurity Community**

⭐ **Star this repo** if you find it useful!

</div>
