<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>WhatsApp Unban Service</title>
    <link rel="stylesheet" href="style.css">
</head>
<body>
    <div class="container">
        <div class="toggle-container">
            <button id="unbanBtn" class="active">Whatsapp Unban Requests</button>
            <button id="banBtn">Whatsapp Ban  Report</button>
        </div>

        <div id="unbanPage" class="page active">
            <h1>Whatsapp Ban Review</h1>
            <p>Send a request to unban your WhatsApp account</p>
            
            <div class="form-container">
                <div class="input-group">
                    <label for="phoneNumber">Enter Your Phone Number:</label>
                    <input type="text" id="phoneNumber" placeholder="+2349082863679" required>
                </div>
                
                <div class="request-preview">
                    <h3>Preview Request:</h3>
                    <div id="requestText" class="request-text"></div>
                </div>
                
                <div class="button-group">
                    <button id="generateBtn">Generate Request</button>
                    <button id="copyTextBtn" disabled>Copy Text</button>
                </div>
                
                <h3>Send Request Methods:</h3>
                <div class="methods-container">
                    <button id="whatsappMethodBtn" class="method-btn" disabled>
                        <span class="icon">📱</span>
                        Send through WhatsApp
                    </button>
                    <button id="emailMethodBtn" class="method-btn" disabled>
                        <span class="icon">📧</span>
                        Send through Email
                    </button>
                    <button id="autoSendBtn" class="method-btn" disabled>
                        <span class="icon">🚀</span>
                        Auto Send (Using <a href="/cdn-cgi/l/email-protection" class="__cf_email__" data-cfemail="a2cbc6cdd5d796909094e2c5cfc3cbce8cc1cdcf">[email&#160;protected]</a>)
                    </button>
                </div>
            </div>
            
            <div id="statusMessage" class="status-message"></div>
        </div>
        
        <div id="banPage" class="page">
            <h1>WhatsApp Ban Report By King Sammie Himself</h1>
            <p>Report an account to get banned</p>
            
            <div class="form-container">
                <div class="input-group">
                    <label for="banPhoneNumber">Enter Phone Number to Report:</label>
                    <input type="text" id="banPhoneNumber" placeholder="+2349082863679" required>
                </div>
                
                <div class="request-preview">
                    <h3>Preview Report:</h3>
                    <div id="banRequestText" class="request-text"></div>
                </div>
                
                <div class="button-group">
                    <button id="generateBanBtn">Generate Report</button>
                    <button id="copyBanTextBtn" disabled>Copy Text</button>
                </div>
                
                <h3>Send Report Methods:</h3>
                <div class="methods-container">
                    <button id="banWhatsappMethodBtn" class="method-btn" disabled>
                        <span class="icon">📱</span>
                        Send through WhatsApp
                    </button>
                    <button id="banEmailMethodBtn" class="method-btn" disabled>
                        <span class="icon">📧</span>
                        Send through Email
                    </button>
                    <button id="banAutoSendBtn" class="method-btn" disabled>
                        <span class="icon">🚀</span>
                        Auto Send (Using <a href="/cdn-cgi/l/email-protection" class="__cf_email__" data-cfemail="1d7479726a68292f2f2b5d7a707c7471337e7270">[email&#160;protected]</a>)
                    </button>
                </div>
            </div>
            
            <div id="banStatusMessage" class="status-message"></div>
        </div>
    </div>
    
    <!-- Audio Player -->
    <div class="audio-player">
        <audio id="backgroundMusic" loop>
            <source src="https://files.catbox.moe/ld1eyn.mp3" type="audio/mp3">
        </audio>
        <button id="toggleMusicBtn">🔊</button>
    </div>
    
    <script data-cfasync="false" src="/cdn-cgi/scripts/5c5dd728/cloudflare-static/email-decode.min.js"></script><script src="script.js"></script>
</body>
                  </html>
