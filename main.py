from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from fastapi.responses import HTMLResponse, StreamingResponse
from pydantic import BaseModel
from groq import Groq
from dotenv import load_dotenv
import os
import json
from typing import List, Dict
import asyncio

# Load environment variables from .env file
load_dotenv()

app = FastAPI(title="NET FRED AI", description="Advanced Cybersecurity Assistant")

# CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Initialize Groq client with API key from environment variables
api_key = os.getenv("GROQ_API_KEY")
if not api_key:
    raise ValueError(
        "GROQ_API_KEY not found in environment variables. "
        "Please create a .env file with your API key or set the environment variable."
    )

client = Groq(api_key=api_key)

# Enhanced system prompt
SYSTEM_PROMPT = """You are NET FRED AI, an elite cybersecurity expert and ethical hacking consultant with 15+ years of experience in:

🛡️ CORE EXPERTISE:
- Threat detection & incident response (SIEM, IDS/IPS, EDR)
- Penetration testing & vulnerability assessment (OWASP, CVE analysis)
- Network security architecture & zero-trust implementation
- Malware analysis & reverse engineering
- Cloud security (AWS, Azure, GCP) & container security
- Cryptography & secure communications
- Security compliance (ISO 27001, NIST, GDPR, SOC 2)
- Social engineering defense & security awareness

🎯 YOUR MISSION:
1. Detect and analyze potential security threats with precision
2. Provide actionable, step-by-step defensive strategies
3. Explain complex security concepts in clear, accessible language
4. Always prioritize ETHICAL and LEGAL approaches
5. Never provide offensive hacking tools or malicious code

📋 RESPONSE GUIDELINES:
- Start with threat level assessment (🟢 Low | 🟡 Medium | 🟠 High | 🔴 Critical)
- Provide technical depth while remaining accessible
- Include real-world examples and industry best practices
- Suggest specific tools, frameworks, and methodologies
- Reference CVEs, CWEs, and MITRE ATT&CK when relevant
- Always conclude with preventive measures

⚠️ ETHICAL BOUNDARIES:
- NO assistance with unauthorized access or malicious activities
- NO creation of malware, exploits for illegal purposes, or attack tools
- Always emphasize legal compliance and responsible disclosure
- Promote defensive security and user protection

You communicate with confidence, precision, and a commitment to cybersecurity excellence."""

# In-memory conversation storage (use Redis/DB in production)
conversations: Dict[str, List[Dict]] = {}

class Message(BaseModel):
    content: str
    session_id: str = "default"

class ChatResponse(BaseModel):
    response: str
    threat_level: str
    session_id: str

@app.get("/", response_class=HTMLResponse)
async def read_root():
    try:
        with open("index.html", "r", encoding="utf-8") as f:
            return f.read()
    except FileNotFoundError:
        return HTMLResponse(
            content="<h1>Error: index.html not found</h1><p>Please ensure index.html is in the same directory as main.py</p>",
            status_code=404
        )

@app.post("/chat", response_class=StreamingResponse)
async def chat(message: Message):
    """Streaming chat endpoint for real-time responses"""
    session_id = message.session_id
    
    # Initialize conversation history
    if session_id not in conversations:
        conversations[session_id] = [
            {"role": "system", "content": SYSTEM_PROMPT}
        ]
    
    # Add user message
    conversations[session_id].append({
        "role": "user",
        "content": message.content
    })
    
    async def generate():
        try:
            # Create streaming completion
            stream = client.chat.completions.create(
                model="llama-3.1-8b-instant",
                messages=conversations[session_id],
                max_tokens=1500,
                temperature=0.3,
                top_p=0.9,
                stream=True
            )
            
            full_response = ""
            for chunk in stream:
                if chunk.choices[0].delta.content:
                    content = chunk.choices[0].delta.content
                    full_response += content
                    yield f"data: {json.dumps({'content': content, 'done': False})}\n\n"
            
            # Store assistant response
            conversations[session_id].append({
                "role": "assistant",
                "content": full_response
            })
            
            # Send completion signal
            yield f"data: {json.dumps({'content': '', 'done': True})}\n\n"
            
        except Exception as e:
            error_message = f"Error: {str(e)}"
            yield f"data: {json.dumps({'error': error_message, 'done': True})}\n\n"
    
    return StreamingResponse(generate(), media_type="text/event-stream")

@app.post("/analyze-threat")
async def analyze_threat(message: Message):
    """Quick threat analysis endpoint"""
    try:
        analysis_prompt = f"""Analyze this potential security threat and provide:
1. Threat Level (Low/Medium/High/Critical)
2. Threat Category
3. Brief Risk Assessment
4. Immediate Action Required

Query: {message.content}

Provide response in JSON format."""

        response = client.chat.completions.create(
            model="llama-3.1-8b-instant",
            messages=[
                {"role": "system", "content": SYSTEM_PROMPT},
                {"role": "user", "content": analysis_prompt}
            ],
            max_tokens=500,
            temperature=0.2
        )
        
        return {"analysis": response.choices[0].message.content}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.delete("/clear-session/{session_id}")
async def clear_session(session_id: str):
    """Clear conversation history"""
    if session_id in conversations:
        conversations[session_id] = [
            {"role": "system", "content": SYSTEM_PROMPT}
        ]
    return {"status": "cleared", "session_id": session_id}

@app.get("/health")
async def health_check():
    return {"status": "operational", "service": "CyberGuard AI"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
