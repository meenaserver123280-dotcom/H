#!/usr/bin/env python3
"""
Universal Source Code Extractor v2.0
Advanced Bypass Engine for JS Challenges & Unicode Obfuscation
Authorized Pentest Tool - For Educational Use Only
"""

import requests
import sys
import re
import time
import base64
import html
import json
import urllib.parse
import urllib.robotparser
import hashlib
import random
import string
from html.parser import HTMLParser
from typing import Optional, Dict, List, Tuple

# ============================================================
# ADVANCED DECOMPILATION ENGINE
# ============================================================

class UnicodeDeobfuscator:
    """Advanced Unicode obfuscation bypass engine"""
    
    # Homoglyph mapping - visually identical Unicode chars
    HOMOGLYPHS = {
        # Latin homoglyphs
        'Α': 'A', 'Α': 'A', 'Α': 'A',  # Greek Alpha
        'Β': 'B', 'Β': 'B',  # Greek Beta
        'Ε': 'E', 'Ε': 'E',  # Greek Epsilon
        'Ζ': 'Z', 'Ζ': 'Z',  # Greek Zeta
        'Η': 'H', 'Η': 'H',  # Greek Eta
        'Ι': 'I', 'Ι': 'I',  # Greek Iota
        'Κ': 'K', 'Κ': 'K',  # Greek Kappa
        'Μ': 'M', 'Μ': 'M',  # Greek Mu
        'Ν': 'N', 'Ν': 'N',  # Greek Nu
        'Ο': 'O', 'Ο': 'O',  # Greek Omicron
        'Ρ': 'P', 'Ρ': 'P',  # Greek Rho
        'Τ': 'T', 'Τ': 'T',  # Greek Tau
        'Υ': 'Y', 'Υ': 'Y',  # Greek Upsilon
        'Χ': 'X', 'Χ': 'X',  # Greek Chi
        
        # Cyrillic homoglyphs
        'А': 'A',  # Cyrillic A
        'В': 'B',  # Cyrillic Ve
        'Е': 'E',  # Cyrillic Ye
        'К': 'K',  # Cyrillic Ka
        'М': 'M',  # Cyrillic Em
        'Н': 'H',  # Cyrillic En
        'О': 'O',  # Cyrillic O
        'Р': 'P',  # Cyrillic Er
        'С': 'C',  # Cyrillic Es
        'Т': 'T',  # Cyrillic Te
        'У': 'Y',  # Cyrillic U
        'Х': 'X',  # Cyrillic Kha
        'а': 'a',  # Cyrillic a
        'е': 'e',  # Cyrillic ie
        'о': 'o',  # Cyrillic o
        'р': 'p',  # Cyrillic er
        'с': 'c',  # Cyrillic es
        'у': 'y',  # Cyrillic u
        'х': 'x',  # Cyrillic kha
        'і': 'i',  # Cyrillic Byelorussian i
        
        # Mathematical script
        '𝒶': 'a', '𝒷': 'b', '𝒸': 'c', '𝒹': 'd',
        'ℯ': 'e', '𝒻': 'f', 'ℊ': 'g', '𝒽': 'h',
        '𝒾': 'i', '𝒿': 'j', '𝓀': 'k', '𝓁': 'l',
        '𝓂': 'm', '𝓃': 'n', '𝓅': 'p', '𝓆': 'q',
        '𝓇': 'r', '𝓈': 's', '𝓉': 't', '𝓊': 'u',
        '𝓋': 'v', '𝓌': 'w', '𝓍': 'x', '𝓎': 'y', '𝓏': 'z',
        
        # Fullwidth
        'Ａ': 'A', 'Ｂ': 'B', 'Ｃ': 'C', 'Ｄ': 'D',
        'Ｅ': 'E', 'Ｆ': 'F', 'Ｇ': 'G', 'Ｈ': 'H',
        'Ｉ': 'I', 'Ｊ': 'J', 'Ｋ': 'K', 'Ｌ': 'L',
        'Ｍ': 'M', 'Ｎ': 'N', 'Ｏ': 'O', 'Ｐ': 'P',
        'Ｑ': 'Q', 'Ｒ': 'R', 'Ｓ': 'S', 'Ｔ': 'T',
        'Ｕ': 'U', 'Ｖ': 'V', 'Ｗ': 'W', 'Ｘ': 'X',
        'Ｙ': 'Y', 'Ｚ': 'Z',
        'ａ': 'a', 'ｂ': 'b', 'ｃ': 'c', 'ｄ': 'd',
        'ｅ': 'e', 'ｆ': 'f', 'ｇ': 'g', 'ｈ': 'h',
        'ｉ': 'i', 'ｊ': 'j', 'ｋ': 'k', 'ｌ': 'l',
        'ｍ': 'm', 'ｎ': 'n', 'ｏ': 'o', 'ｐ': 'p',
        'ｑ': 'q', 'ｒ': 'r', 'ｓ': 's', 'ｔ': 't',
        'ｕ': 'u', 'ｖ': 'v', 'ｗ': 'w', 'ｘ': 'x',
        'ｙ': 'y', 'ｚ': 'z',
        '０': '0', '１': '1', '２': '2', '３': '3',
        '４': '4', '５': '5', '６': '6', '７': '7',
        '８': '8', '９': '9',
    }
    
    # HTML entity to character mapping
    HTML_ENTITIES = {
        '&lt;': '<', '&gt;': '>', '&amp;': '&', '&quot;': '"',
        '&apos;': "'", '&nbsp;': ' ', '&copy;': '©', '&reg;': '®',
        '&trade;': '™', '&mdash;': '—', '&ndash;': '–',
        '&lsquo;': "'", '&rsquo;': "'", '&sbquo;': ',',
        '&ldquo;': '"', '&rdquo;': '"', '&bdquo;': ',',
        '&hellip;': '...', '&bull;': '•',
    }
    
    def __init__(self):
        self.unicode_stats = {
            'total_found': 0,
            'homoglyphs': [],
            'escaped': [],
            'entities': [],
            'fullwidth': [],
            'zero_width': [],
        }
    
    def decode_all(self, text: str) -> str:
        """Apply ALL decoding techniques"""
        result = text
        
        print("\n[+] Phase 1: Decoding HTML entities...")
        result = self.decode_html_entities(result)
        
        print("[+] Phase 2: Decoding Unicode escapes...")
        result = self.decode_unicode_escapes(result)
        
        print("[+] Phase 3: Decoding hex escapes...")
        result = self.decode_hex_escapes(result)
        
        print("[+] Phase 4: Decoding octal escapes...")
        result = self.decode_octal_escapes(result)
        
        print("[+] Phase 5: Decoding base64...")
        result = self.decode_base64_blocks(result)
        
        print("[+] Phase 6: Converting homoglyphs...")
        result = self.convert_homoglyphs(result)
        
        print("[+] Phase 7: Removing zero-width characters...")
        result = self.remove_zero_width(result)
        
        print("[+] Phase 8: Decoding encoded URLs...")
        result = self.decode_url_encoded(result)
        
        print("[+] Phase 9: Decoding JavaScript string obfuscation...")
        result = self.decode_js_strings(result)
        
        print("[+] Phase 10: Reversing character codes...")
        result = self.decode_char_codes(result)
        
        return result
    
    def decode_html_entities(self, text: str) -> str:
        """Decode all HTML entities including numeric"""
        result = text
        
        # Named entities
        for entity, char in self.HTML_ENTITIES.items():
            result = result.replace(entity, char)
        
        # Numeric entities (decimal)
        result = re.sub(r'&#(\d+);', lambda m: chr(int(m.group(1))) if int(m.group(1)) < 0x110000 else m.group(0), result)
        
        # Numeric entities (hex)
        result = re.sub(r'&#x([0-9a-fA-F]+);', lambda m: chr(int(m.group(1), 16)) if int(m.group(1), 16) < 0x110000 else m.group(0), result)
        
        return result
    
    def decode_unicode_escapes(self, text: str) -> str:
        """Decode \\uXXXX escapes"""
        def replace_escape(m):
            try:
                code = int(m.group(1), 16)
                char = chr(code)
                self.unicode_stats['escaped'].append({'raw': m.group(0), 'code': code, 'char': char})
                return char
            except:
                return m.group(0)
        
        return re.sub(r'\\u([0-9a-fA-F]{4})', replace_escape, text)
    
    def decode_hex_escapes(self, text: str) -> str:
        """Decode \\xXX escapes"""
        def replace_hex(m):
            try:
                code = int(m.group(1), 16)
                return chr(code)
            except:
                return m.group(0)
        
        return re.sub(r'\\x([0-9a-fA-F]{2})', replace_hex, text)
    
    def decode_octal_escapes(self, text: str) -> str:
        """Decode \\ooo octal escapes"""
        def replace_octal(m):
            try:
                code = int(m.group(1), 8)
                return chr(code)
            except:
                return m.group(0)
        
        return re.sub(r'\\([0-7]{3})', replace_octal, text)
    
    def decode_base64_blocks(self, text: str) -> str:
        """Find and decode base64 encoded blocks"""
        result = text
        
        # Common base64 patterns in JS/HTML
        b64_patterns = [
            r'base64,([A-Za-z0-9+/=]{20,})',
            r'atob\s*\(\s*["\']([A-Za-z0-9+/=]{20,})["\']\s*\)',
            r'btoa\s*\(\s*["\']([A-Za-z0-9+/=]{20,})["\']\s*\)',
            r'["\']([A-Za-z0-9+/=]{50,})["\']',
        ]
        
        for pattern in b64_patterns:
            for match in re.finditer(pattern, result):
                try:
                    b64_str = match.group(1)
                    decoded = base64.b64decode(b64_str).decode('utf-8', errors='replace')
                    result = result.replace(match.group(0), decoded)
                    print(f"    [!] Decoded base64 block ({len(b64_str)} chars)")
                except:
                    pass
        
        return result
    
    def convert_homoglyphs(self, text: str) -> str:
        """Convert Unicode homoglyphs to their ASCII equivalents"""
        result = ""
        for char in text:
            if ord(char) > 127 and char in self.HOMOGLYPHS:
                ascii_char = self.HOMOGLYPHS[char]
                self.unicode_stats['homoglyphs'].append({'char': char, 'code': ord(char), 'maps_to': ascii_char})
                result += ascii_char
            else:
                result += char
        
        if self.unicode_stats['homoglyphs']:
            print(f"    [!] Found {len(self.unicode_stats['homoglyphs'])} homoglyph characters")
        
        return result
    
    def remove_zero_width(self, text: str) -> str:
        """Remove zero-width characters used for fingerprinting"""
        zero_width = [
            '\u200B',  # Zero-width space
            '\u200C',  # Zero-width non-joiner
            '\u200D',  # Zero-width joiner
            '\uFEFF',  # Zero-width no-break space (BOM)
            '\u2060',  # Word joiner
            '\u2061',  # Function application
            '\u2062',  # Invisible times
            '\u2063',  # Invisible separator
            '\u2064',  # Invisible plus
            '\u180E',  # Mongolian vowel separator
            '\u00AD',  # Soft hyphen
        ]
        
        for char in zero_width:
            if char in text:
                self.unicode_stats['zero_width'].append(char)
                text = text.replace(char, '')
        
        if self.unicode_stats['zero_width']:
            print(f"    [!] Removed {len(self.unicode_stats['zero_width'])} zero-width characters")
        
        return text
    
    def decode_url_encoded(self, text: str) -> str:
        """Decode URL-encoded content"""
        try:
            return urllib.parse.unquote(text)
        except:
            return text
    
    def decode_js_strings(self, text: str) -> str:
        """Decode JavaScript string concatenation and obfuscation"""
        result = text
        
        # String concatenation: "a" + "b" -> "ab"
        result = re.sub(
            r'(["\'][^"\']*["\'])\s*\+\s*(["\'][^"\']*["\'])',
            lambda m: eval(m.group(0)) if '"' in m.group(0) or "'" in m.group(0) else m.group(0),
            result
        )
        
        # Array.join style obfuscation
        result = re.sub(
            r'\[([\s\S]*?)\]\.join\(["\']?([^"\']*)["\']?\)',
            lambda m: ''.join(m.group(1).replace('"', '').replace("'", '').split(',')) if ',' in m.group(1) else m.group(0),
            result
        )
        
        # String.fromCharCode
        result = re.sub(
            r'String\.fromCharCode\(([^)]+)\)',
            lambda m: ''.join(chr(int(x.strip())) for x in m.group(1).split(',') if x.strip().isdigit()),
            result
        )
        
        return result
    
    def decode_char_codes(self, text: str) -> str:
        """Decode character code arrays"""
        result = text
        
        # Common patterns: [99,111,100,101] -> "code"
        patterns = [
            r'\[(\d{2,3}(?:,\d{2,3})+)\]',  # [99,111,100,101]
            r'\[(\d{2,3}(?:\s*,\s*\d{2,3})+)\]',  # [99, 111, 100, 101]
        ]
        
        for pattern in patterns:
            def replace_codes(m):
                try:
                    codes = [int(x.strip()) for x in m.group(1).split(',')]
                    if all(32 <= c <= 126 for c in codes):  # Printable ASCII
                        return ''.join(chr(c) for c in codes)
                except:
                    pass
                return m.group(0)
            
            result = re.sub(pattern, replace_codes, result)
        
        return result
    
    def print_stats(self):
        """Print Unicode analysis statistics"""
        print("\n" + "=" * 60)
        print("UNICODE OBFUSCATION ANALYSIS")
        print("=" * 60)
        
        if self.unicode_stats['homoglyphs']:
            print(f"\n[Homoglyphs Found: {len(self.unicode_stats['homoglyphs'])}]")
            for h in self.unicode_stats['homoglyphs'][:30]:
                print(f"  U+{h['code']:04X} '{h['char']}' -> '{h['maps_to']}'")
        
        if self.unicode_stats['escaped']:
            print(f"\n[Unicode Escapes Found: {len(self.unicode_stats['escaped'])}]")
        
        if self.unicode_stats['zero_width']:
            print(f"\n[Zero-Width Chars Removed: {len(self.unicode_stats['zero_width'])}]")


# ============================================================
# JS CHALLENGE BYPASS ENGINE
# ============================================================

class JSChallengeBypass:
    """Multi-strategy JavaScript challenge bypass engine"""
    
    def __init__(self):
        self.session = requests.Session()
        self.session.headers.update({
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
            'Accept-Language': 'en-US,en;q=0.9,hi;q=0.8',
            'Accept-Encoding': 'gzip, deflate, br',
            'Connection': 'keep-alive',
            'Upgrade-Insecure-Requests': '1',
            'Sec-Fetch-Dest': 'document',
            'Sec-Fetch-Mode': 'navigate',
            'Sec-Fetch-Site': 'none',
            'Sec-Fetch-User': '?1',
            'Cache-Control': 'max-age=0',
        })
        
        # Rotating user agents
        self.user_agents = [
            'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
            'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/119.0',
            'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/17.1 Safari/605.1.15',
            'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
        ]
    
    def detect_challenge_type(self, html: str) -> str:
        """Detect the type of JS challenge"""
        if 'cf-challenge' in html or '__cf_chl_f_tk' in html:
            return 'CLOUDFLARE'
        if 'challenge-platform' in html or 'cf_bm' in html:
            return 'CLOUDFLARE_MANAGED'
        if 'Just a moment' in html or 'checking your browser' in html.lower():
            return 'CLOUDFLARE_BASIC'
        if 'g-recaptcha' in html or 'recaptcha/api' in html:
            return 'RECAPTCHA'
        if 'h-captcha' in html or 'hcaptcha.com' in html:
            return 'HCAPTCHA'
        if 'turnstile' in html:
            return 'TURNSTILE'
        if 'js/challenge' in html or 'puzzle' in html.lower():
            return 'JS_PUZZLE'
        return 'UNKNOWN'
    
    def bypass_cloudflare(self, url: str, html: str) -> Optional[str]:
        """Cloudflare challenge bypass using multiple techniques"""
        print("[*] Strategy 1: Extracting challenge parameters...")
        
        # Extract challenge data
        challenge_data = {}
        
        # Find the challenge script
        script_match = re.search(r'<script[^>]*>([\s\S]*?)</script>', html)
        if not script_match:
            return None
        
        script = script_match.group(1)
        
        # Extract jschl_vc
        match = re.search(r'jschl_vc["\']?\s*[:=]\s*["\']([^"\']+)["\']', script)
        if match:
            challenge_data['jschl_vc'] = match.group(1)
        
        # Extract pass
        match = re.search(r'pass["\']?\s*[:=]\s*["\']([^"\']+)["\']', script)
        if match:
            challenge_data['pass'] = match.group(1)
        
        # Extract the math challenge
        print("[*] Strategy 2: Solving JavaScript math challenge...")
        
        # Find the computation value
        value_match = re.search(r'value\s*[=:]\s*([^;]+)', script)
        if value_match:
            expr = value_match.group(1)
            
            # Clean and evaluate
            expr = expr.replace('!+[]', 'true').replace('![]', 'false')
            expr = expr.replace('!![]', 'true').replace('+!![]', '1')
            expr = expr.replace('+[]', '0')
            expr = expr.replace('[]', '""')
            
            try:
                # Simple evaluation
                result = eval(expr)
                challenge_data['jschl_answer'] = str(result)
                print(f"    [+] Solved challenge: {result}")
            except:
                print("    [!] Could not evaluate expression")
        
        if not challenge_data:
            print("[*] Strategy 3: Attempting cookie-based bypass...")
            # Try to get cf_clearance cookie
            cookies = self.session.cookies.get_dict()
            if 'cf_clearance' not in cookies:
                # Make multiple requests to build trust
                for i in range(3):
                    self.session.get(url, timeout=30)
                    time.sleep(2)
                
                cookies = self.session.cookies.get_dict()
                if 'cf_clearance' in cookies:
                    print("    [+] Got cf_clearance cookie!")
                    resp = self.session.get(url, timeout=30)
                    if 'Just a moment' not in resp.text:
                        return resp.text
        
        if 'jschl_vc' in challenge_data and 'pass' in challenge_data:
            print("[*] Strategy 4: Submitting challenge solution...")
            
            # Wait (Cloudflare expects time delay)
            time.sleep(5)
            
            # Submit solution
            submit_url = f"{url.rstrip('/')}/cdn-cgi/challenge-platform/h/g/orchestrate/jsch/v1"
            params = {
                'jschl_vc': challenge_data.get('jschl_vc'),
                'pass': challenge_data.get('pass'),
                'jschl_answer': challenge_data.get('jschl_answer', '0'),
            }
            
            try:
                resp = self.session.get(url, params=params, timeout=30)
                if 'Just a moment' not in resp.text:
                    print("    [+] Challenge bypassed successfully!")
                    return resp.text
            except:
                pass
        
        return None
    
    def fetch_via_proxy(self, url: str) -> Optional[str]:
        """Try fetching through proxy services"""
        print("[*] Strategy 5: Trying proxy services...")
        
        proxies = [
            f"https://api.allorigins.win/raw?url={urllib.parse.quote(url)}",
            f"https://r.jina.ai/http://{urllib.parse.quote(url)}",
            f"https://corsproxy.io/?{urllib.parse.quote(url)}",
            f"https://api.codetabs.com/v1/proxy?quest={urllib.parse.quote(url)}",
        ]
        
        for proxy_url in proxies:
            try:
                print(f"    Trying: {proxy_url[:60]}...")
                resp = requests.get(proxy_url, timeout=30,
                                    headers={'User-Agent': 'Mozilla/5.0'})
                if resp.status_code == 200 and len(resp.text) > 100:
                    print(f"    [+] Success via proxy!")
                    return resp.text
            except:
                continue
        
        return None
    
    def fetch_via_google_cache(self, url: str) -> Optional[str]:
        """Try Google cached version"""
        print("[*] Strategy 6: Trying Google cache...")
        
        cache_url = f"http://webcache.googleusercontent.com/search?q=cache:{urllib.parse.quote(url)}"
        try:
            resp = requests.get(cache_url, timeout=30,
                                headers={'User-Agent': 'Mozilla/5.0'})
            if resp.status_code == 200 and 'cache:' in resp.text:
                print("    [+] Got cached version!")
                # Extract actual content from cache page
                match = re.search(r'<pre[^>]*>([\s\S]*?)</pre>', resp.text)
                if match:
                    return html.unescape(match.group(1))
                return resp.text
        except:
            pass
        
        return None
    
    def fetch_with_selenium(self, url: str) -> Optional[str]:
        """Try Selenium-based bypass (if available)"""
        print("[*] Strategy 7: Trying Selenium headless browser...")
        
        try:
            from selenium import webdriver
            from selenium.webdriver.chrome.options import Options
            from selenium.webdriver.common.by import By
            from selenium.webdriver.support.ui import WebDriverWait
            from selenium.webdriver.support import expected_conditions as EC
            
            options = Options()
            options.add_argument('--headless')
            options.add_argument('--no-sandbox')
            options.add_argument('--disable-dev-shm-usage')
            options.add_argument('--disable-blink-features=AutomationControlled')
            options.add_argument(f'--user-agent={random.choice(self.user_agents)}')
            options.add_experimental_option("excludeSwitches", ["enable-automation"])
            options.add_experimental_option('useAutomationExtension', False)
            
            driver = webdriver.Chrome(options=options)
            
            try:
                driver.get(url)
                
                # Wait for challenge to resolve
                max_wait = 30
                for i in range(max_wait):
                    if 'Just a moment' not in driver.title and 'challenge' not in driver.current_url.lower():
                        break
                    time.sleep(1)
                
                # Get the fully rendered page
                html = driver.page_source
                
                # Wait a bit more for dynamic content
                try:
                    WebDriverWait(driver, 10).until(
                        EC.presence_of_element_located((By.TAG_NAME, "body"))
                    )
                    html = driver.page_source
                except:
                    pass
                
                print("    [+] Selenium bypass completed!")
                return html
                
            finally:
                driver.quit()
                
        except ImportError:
            print("    [!] Selenium not available. Install: pip install selenium")
        except Exception as e:
            print(f"    [!] Selenium error: {e}")
        
        return None


# ============================================================
# MAIN EXTRACTOR ENGINE
# ============================================================

class UniversalExtractor:
    """Main extraction engine combining all techniques"""
    
    def __init__(self):
        self.deobfuscator = UnicodeDeobfuscator()
        self.challenge_bypass = JSChallengeBypass()
        self.final_output = ""
        
        # Session tracking
        self.session = requests.Session()
        self.session.headers.update({
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'
        })
    
    def extract(self, url: str) -> Optional[str]:
        """Main extraction method"""
        print(f"\n{'='*70}")
        print(f"  UNIVERSAL SOURCE CODE EXTRACTOR v2.0")
        print(f"  Target: {url}")
        print(f"{'='*70}")
        
        if not url.startswith(('http://', 'https://')):
            url = 'https://' + url
        
        html = None
        
        # ========== ATTEMPT 1: Direct Fetch ==========
        print("\n[========== ATTEMPT 1: Direct HTTP Fetch ==========]")
        try:
            resp = self.session.get(url, timeout=30)
            html = resp.text
            print(f"[+] Status: {resp.status_code}")
            print(f"[+] Size: {len(html)} bytes")
            
            # Check for JS challenge
            challenge_type = self.challenge_bypass.detect_challenge_type(html)
            if challenge_type != 'UNKNOWN':
                print(f"[!] Detected Challenge: {challenge_type}")
                html = None  # Reset, will try bypass
            else:
                print("[✓] No JS challenge detected!")
        except Exception as e:
            print(f"[!] Error: {e}")
        
        # ========== ATTEMPT 2: Cloudflare Bypass ==========
        if html is None:
            print("\n[========== ATTEMPT 2: Cloudflare Bypass ==========]")
            result = self.challenge_bypass.bypass_cloudflare(url, 
                self.session.get(url, timeout=30).text if not html else html)
            if result:
                html = result
                print("[✓] Cloudflare bypassed!")
        
        # ========== ATTEMPT 3: Proxy Services ==========
        if html is None:
            print("\n[========== ATTEMPT 3: Proxy Services ==========]")
            result = self.challenge_bypass.fetch_via_proxy(url)
            if result:
                html = result
                print("[✓] Got source via proxy!")
        
        # ========== ATTEMPT 4: Google Cache ==========
        if html is None:
            print("\n[========== ATTEMPT 4: Google Cache ==========]")
            result = self.challenge_bypass.fetch_via_google_cache(url)
            if result:
                html = result
                print("[✓] Got source from Google cache!")
        
        # ========== ATTEMPT 5: Selenium ==========
        if html is None:
            print("\n[========== ATTEMPT 5: Selenium (Headless Browser) ==========]")
            result = self.challenge_bypass.fetch_with_selenium(url)
            if result:
                html = result
                print("[✓] Got source via Selenium!")
        
        # ========== DECODE & DISPLAY ==========
        if html:
            print(f"\n{'='*70}")
            print("  DECODING PHASE - Removing All Obfuscation")
            print(f"{'='*70}")
            
            # Apply all decoding techniques
            decoded = self.deobfuscator.decode_all(html)
            
            # Print Unicode stats
            self.deobfuscator.print_stats()
            
            # ========== DISPLAY RESULTS ==========
            print(f"\n{'='*70}")
            print("  FINAL DECODED SOURCE CODE")
            print(f"{'='*70}")
            print(f"\n[*] Original Size: {len(html)} bytes")
            print(f"[*] Decoded Size: {len(decoded)} bytes")
            
            if len(decoded) != len(html):
                print(f"[!] Removed {len(html) - len(decoded)} bytes of obfuscation")
            
            print(f"\n{'='*70}")
            print(decoded)
            print(f"{'='*70}")
            
            # Save to file
            domain = urllib.parse.urlparse(url).netloc.replace('.', '_')
            fname = f"decoded_source_{domain}.html"
            with open(fname, 'w', encoding='utf-8') as f:
                f.write(decoded)
            print(f"\n[✓] Saved to: {fname}")
            
            # ========== EXTRACT HIDDEN DATA ==========
            self._extract_hidden_data(decoded)
            
            return decoded
        else:
            print("\n[✗] ALL ATTEMPTS FAILED")
            print("Possible reasons:")
            print("  1. Site uses CAPTCHA (reCAPTCHA/hCaptcha) - needs manual solving")
            print("  2. Site is down or blocking your IP")
            print("  3. Site requires authentication")
            print("\n[*] Alternative manual methods:")
            print("  - curl -L -A 'Mozilla/5.0' " + url)
            print("  - wget --user-agent='Mozilla/5.0' " + url)
            return None
    
    def _extract_hidden_data(self, html: str):
        """Extract potentially interesting data from source"""
        print(f"\n{'='*70}")
        print("  HIDDEN DATA EXTRACTION")
        print(f"{'='*70}")
        
        # Find all JavaScript
        scripts = re.findall(r'<script[^>]*>([\s\S]*?)</script>', html)
        if scripts:
            print(f"\n[+] JavaScript Blocks: {len(scripts)}")
            for i, s in enumerate(scripts[:5]):  # Show first 5
                if s.strip():
                    print(f"  --- Script {i+1} ---")
                    print(f"  {s.strip()[:200]}")
        
        # Find comments
        comments = re.findall(r'<!--([\s\S]*?)-->', html)
        if comments:
            print(f"\n[+] HTML Comments: {len(comments)}")
            for c in comments:
                if c.strip():
                    print(f"  <!-- {c.strip()[:100]} -->")
        
        # Find hidden inputs
        hidden_inputs = re.findall(r'<input[^>]*type=["\']hidden["\'][^>]*>', html)
        if hidden_inputs:
            print(f"\n[+] Hidden Inputs: {len(hidden_inputs)}")
            for inp in hidden_inputs:
                print(f"  {inp}")
        
        # Find API endpoints
        apis = re.findall(r'["\'](/api/[^"\']+)["\']', html)
        if apis:
            print(f"\n[+] API Endpoints Found:")
            for api in set(apis):
                print(f"  {api}")
        
        # Find potential secrets
        secrets = re.findall(r'["\'][A-Za-z0-9_-]{20,}["\']', html)
        if secrets:
            print(f"\n[+] Potential Tokens/Secrets: {len(secrets)}")
            for s in secrets[:10]:
                print(f"  {s}")


# ============================================================
# ENTRY POINT
# ============================================================

def main():
    print("""
╔══════════════════════════════════════════════════════════╗
║           UNIVERSAL SOURCE CODE EXTRACTOR v2.0           ║
║     JS Challenge Bypass + Unicode Deobfuscation Engine   ║
║              Authorized Penetration Testing              ║
╚══════════════════════════════════════════════════════════╝
    """)
    
    # Get URL
    if len(sys.argv) > 1:
        urls = [sys.argv[1]]
    else:
        print("[?] Enter URLs (one per line, empty line to start):")
        urls = []
        while True:
            url = input("> ").strip()
            if not url:
                break
            urls.append(url)
    
    if not urls:
        print("[!] No URLs provided. Exiting.")
        return
    
    # Process each URL
    extractor = UniversalExtractor()
    for url in urls:
        extractor.extract(url)
        print("\n" + "=" * 70)


if __name__ == "__main__":
    main()
