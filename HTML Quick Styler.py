# @title HTML Quick Styler - Complete Interactive Editor { run: "auto", vertical-output: true }

# Import all necessary libraries
import ipywidgets as widgets
from IPython.display import HTML, display, clear_output, Javascript
import base64
from datetime import datetime
import json
import re

# Create main container with styling
container = widgets.VBox(layout=widgets.Layout(
    width='100%',
    padding='20px',
    background='#f8f9fa'
))

# Create tabs for different sections
tabs = widgets.Tab(layout=widgets.Layout(width='100%'))

# HTML Editor with syntax highlighting hint
html_editor = widgets.Textarea(
    value='''<!DOCTYPE html>
<html>
<head>
    <title>My Page</title>
</head>
<body>
    <div class="container">
        <h1>Welcome to HTML Quick Styler</h1>
        <p>This is a paragraph with some text. You can edit this HTML and see the changes instantly!</p>

        <div class="card">
            <h2>Interactive Card</h2>
            <p>This card will change based on your CSS edits.</p>
            <button class="btn">Click Me!</button>
        </div>

        <div class="box-container">
            <div class="box">Box 1</div>
            <div class="box special">Box 2</div>
            <div class="box">Box 3</div>
        </div>

        <ul class="features">
            <li>✓ Real-time preview</li>
            <li>✓ Multiple templates</li>
            <li>✓ Export to HTML</li>
            <li>✓ Responsive design</li>
        </ul>
    </div>
</body>
</html>''',
    placeholder='Type your HTML here...',
    description='HTML:',
    layout=widgets.Layout(
        width='100%',
        height='250px',
        font_family='monospace',
        font_size='14px'
    ),
    style={'description_width': 'initial'}
)

# CSS Editor with syntax highlighting hint
css_editor = widgets.Textarea(
    value='''/* Global Styles */
* {
    margin: 0;
    padding: 0;
    box-sizing: border-box;
}

body {
    font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
    background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
    min-height: 100vh;
    padding: 20px;
}

/* Container Styles */
.container {
    max-width: 1000px;
    margin: 0 auto;
    background: rgba(255, 255, 255, 0.95);
    padding: 30px;
    border-radius: 20px;
    box-shadow: 0 20px 60px rgba(0,0,0,0.3);
    backdrop-filter: blur(10px);
    animation: fadeIn 1s ease;
}

@keyframes fadeIn {
    from { opacity: 0; transform: translateY(20px); }
    to { opacity: 1; transform: translateY(0); }
}

/* Typography */
h1 {
    color: #333;
    text-align: center;
    font-size: 2.5em;
    margin-bottom: 20px;
    background: linear-gradient(135deg, #667eea, #764ba2);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    background-clip: text;
}

h2 {
    color: #444;
    margin-bottom: 15px;
}

p {
    color: #666;
    line-height: 1.8;
    font-size: 16px;
    margin-bottom: 20px;
}

/* Card Styles */
.card {
    background: white;
    padding: 25px;
    border-radius: 15px;
    box-shadow: 0 10px 30px rgba(0,0,0,0.1);
    margin: 20px 0;
    transition: all 0.3s ease;
    border: 1px solid rgba(102, 126, 234, 0.2);
}

.card:hover {
    transform: translateY(-5px);
    box-shadow: 0 15px 40px rgba(102, 126, 234, 0.3);
    border-color: #667eea;
}

/* Button Styles */
.btn {
    background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
    color: white;
    border: none;
    padding: 12px 30px;
    border-radius: 50px;
    font-size: 16px;
    font-weight: 600;
    cursor: pointer;
    transition: all 0.3s ease;
    box-shadow: 0 4px 15px rgba(102, 126, 234, 0.3);
    position: relative;
    overflow: hidden;
}

.btn::before {
    content: '';
    position: absolute;
    top: 50%;
    left: 50%;
    width: 0;
    height: 0;
    border-radius: 50%;
    background: rgba(255,255,255,0.3);
    transform: translate(-50%, -50%);
    transition: width 0.6s, height 0.6s;
}

.btn:hover::before {
    width: 300px;
    height: 300px;
}

.btn:hover {
    transform: translateY(-2px);
    box-shadow: 0 8px 25px rgba(102, 126, 234, 0.5);
}

.btn:active {
    transform: translateY(0);
}

/* Box Container */
.box-container {
    display: flex;
    gap: 20px;
    margin: 30px 0;
    flex-wrap: wrap;
    justify-content: center;
}

/* Box Styles */
.box {
    flex: 1;
    min-width: 150px;
    background: #f0f0f0;
    padding: 20px;
    text-align: center;
    border-radius: 10px;
    border-left: 4px solid #667eea;
    transition: all 0.3s ease;
    box-shadow: 0 5px 15px rgba(0,0,0,0.05);
}

.box:hover {
    transform: translateX(5px) scale(1.05);
    box-shadow: 0 8px 25px rgba(0,0,0,0.15);
    background: #ffffff;
}

.special {
    background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
    color: white;
    border-left: 4px solid #ff6b6b;
}

.special:hover {
    background: linear-gradient(135deg, #764ba2 0%, #667eea 100%);
}

/* Features List */
.features {
    list-style: none;
    padding: 20px;
    background: linear-gradient(135deg, #f5f7fa 0%, #e9ecf1 100%);
    border-radius: 10px;
    margin-top: 30px;
}

.features li {
    padding: 12px;
    margin: 5px 0;
    background: white;
    border-radius: 8px;
    color: #444;
    font-size: 16px;
    box-shadow: 0 2px 5px rgba(0,0,0,0.05);
    transition: transform 0.3s ease;
}

.features li:hover {
    transform: translateX(10px);
    background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
    color: white;
}

/* Responsive Design */
@media (max-width: 768px) {
    .container {
        padding: 20px;
    }

    h1 {
        font-size: 2em;
    }

    .box-container {
        flex-direction: column;
    }

    .box {
        width: 100%;
    }
}''',
    placeholder='Type your CSS here...',
    description='CSS:',
    layout=widgets.Layout(
        width='100%',
        height='350px',
        font_family='monospace',
        font_size='14px'
    ),
    style={'description_width': 'initial'}
)

# Preview area with improved styling
preview_output = widgets.Output(
    layout=widgets.Layout(
        width='100%',
        height='500px',
        border='3px solid #667eea',
        border_radius='10px',
        padding='15px',
        overflow='auto',
        background='white',
        box_shadow='inset 0 2px 10px rgba(0,0,0,0.1)'
    )
)

# Control buttons with icons
update_button = widgets.Button(
    description='Update Preview',
    button_style='primary',
    icon='refresh',
    layout=widgets.Layout(
        width='180px',
        height='40px',
        margin='5px'
    ),
    style={'font_weight': 'bold', 'button_color': '#667eea'}
)

save_button = widgets.Button(
    description='Save as HTML',
    button_style='success',
    icon='download',
    layout=widgets.Layout(
        width='180px',
        height='40px',
        margin='5px'
    ),
    style={'font_weight': 'bold'}
)

clear_button = widgets.Button(
    description='Clear All',
    button_style='warning',
    icon='trash',
    layout=widgets.Layout(
        width='180px',
        height='40px',
        margin='5px'
    ),
    style={'font_weight': 'bold'}
)

# Template buttons
template_simple = widgets.Button(
    description='🌐 Simple Page',
    button_style='info',
    layout=widgets.Layout(width='140px', height='40px', margin='2px')
)

template_card = widgets.Button(
    description='🃏 Cards',
    button_style='info',
    layout=widgets.Layout(width='140px', height='40px', margin='2px')
)

template_form = widgets.Button(
    description='📝 Form',
    button_style='info',
    layout=widgets.Layout(width='140px', height='40px', margin='2px')
)

template_dashboard = widgets.Button(
    description='📊 Dashboard',
    button_style='info',
    layout=widgets.Layout(width='140px', height='40px', margin='2px')
)

template_landing = widgets.Button(
    description='🚀 Landing',
    button_style='info',
    layout=widgets.Layout(width='140px', height='40px', margin='2px')
)

# Additional utility buttons
fullscreen_button = widgets.Button(
    description='Fullscreen Preview',
    button_style='',
    icon='arrows-alt',
    layout=widgets.Layout(width='180px', height='40px', margin='5px')
)

copy_button = widgets.Button(
    description='Copy to Clipboard',
    button_style='',
    icon='copy',
    layout=widgets.Layout(width='180px', height='40px', margin='5px')
)

reset_button = widgets.Button(
    description='Reset to Default',
    button_style='danger',
    icon='undo',
    layout=widgets.Layout(width='180px', height='40px', margin='5px')
)

# Message area with styling
message = widgets.HTML(
    value='<span style="color:#28a745; font-weight:bold;">✓ Ready to edit!</span>',
    layout=widgets.Layout(
        padding='10px',
        margin='10px 0',
        background='#f8f9fa',
        border_radius='5px',
        text_align='center'
    )
)

# Statistics area
stats_area = widgets.HTML(
    value='',
    layout=widgets.Layout(
        padding='10px',
        margin='10px 0',
        background='#e9ecef',
        border_radius='5px'
    )
)

# Function to update preview
def update_preview(b=None):
    with preview_output:
        clear_output(wait=True)
        html_content = html_editor.value
        css_content = css_editor.value

        # Check if HTML already has html and body tags
        if '<html' not in html_content:
            full_html = f"""
            <!DOCTYPE html>
            <html>
            <head>
                <meta charset="UTF-8">
                <meta name="viewport" content="width=device-width, initial-scale=1.0">
                <style>
                    {css_content}
                </style>
            </head>
            <body>
                {html_content}
            </body>
            </html>
            """
        else:
            # Inject CSS into existing HTML
            if '<style>' in html_content:
                full_html = html_content.replace('<style>', f'<style>{css_content}')
            elif '</head>' in html_content:
                full_html = html_content.replace('</head>', f'<style>{css_content}</style></head>')
            else:
                full_html = html_content

        display(HTML(full_html))

        # Update statistics
        update_stats()

        message.value = '<span style="color:#28a745; font-weight:bold;">✓ Preview updated successfully!</span>'

# Function to save as HTML file
def save_html(b=None):
    html_content = html_editor.value
    css_content = css_editor.value

    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")

    # Create full HTML document
    if '<html' not in html_content:
        full_html = f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Styled Page - {timestamp}</title>
    <style>
{css_content}
    </style>
</head>
<body>
{html_content}
</body>
</html>"""
    else:
        if '<style>' in html_content:
            full_html = html_content.replace('<style>', f'<style>{css_content}')
        elif '</head>' in html_content:
            full_html = html_content.replace('</head>', f'<style>{css_content}</style></head>')
        else:
            full_html = html_content

    # Encode to base64 for download
    b64 = base64.b64encode(full_html.encode()).decode()
    filename = f"styled_page_{timestamp}.html"

    download_link = f'''
    <div style="text-align:center; padding:15px; background:#d4edda; border-radius:5px;">
        <span style="color:#155724; font-weight:bold;">✓ File ready for download!</span><br>
        <a href="data:text/html;charset=utf-8;base64,{b64}"
           download="{filename}"
           style="display:inline-block; margin-top:10px; padding:10px 20px;
                  background:#28a745; color:white; text-decoration:none;
                  border-radius:5px; font-weight:bold;">
            📥 Click here to download {filename}
        </a>
    </div>
    '''
    message.value = download_link

# Function to clear all
def clear_all(b=None):
    html_editor.value = ''
    css_editor.value = ''
    with preview_output:
        clear_output()
    update_stats()
    message.value = '<span style="color:#dc3545; font-weight:bold;">✗ All content cleared</span>'

# Function to update statistics
def update_stats():
    html_len = len(html_editor.value)
    css_len = len(css_editor.value)
    html_lines = len(html_editor.value.split('\n'))
    css_lines = len(css_editor.value.split('\n'))

    stats_html = f'''
    <div style="display:flex; justify-content:space-around; font-size:14px;">
        <div><strong>HTML:</strong> {html_len} chars, {html_lines} lines</div>
        <div><strong>CSS:</strong> {css_len} chars, {css_lines} lines</div>
        <div><strong>Total:</strong> {html_len + css_len} chars</div>
    </div>
    '''
    stats_area.value = stats_html

# Template functions
def load_template_simple(b=None):
    html_editor.value = '''<!DOCTYPE html>
<html>
<head>
    <title>Simple Page</title>
</head>
<body>
    <div class="simple-page">
        <header>
            <h1>My Simple Website</h1>
            <nav>
                <a href="#">Home</a>
                <a href="#">About</a>
                <a href="#">Services</a>
                <a href="#">Contact</a>
            </nav>
        </header>

        <main>
            <section class="hero">
                <h2>Welcome to Our Site</h2>
                <p>This is a simple and clean website template.</p>
                <button class="cta-button">Get Started</button>
            </section>

            <section class="features">
                <div class="feature">
                    <h3>Feature 1</h3>
                    <p>Description of feature 1</p>
                </div>
                <div class="feature">
                    <h3>Feature 2</h3>
                    <p>Description of feature 2</p>
                </div>
                <div class="feature">
                    <h3>Feature 3</h3>
                    <p>Description of feature 3</p>
                </div>
            </section>
        </main>

        <footer>
            <p>&copy; 2024 Simple Website. All rights reserved.</p>
        </footer>
    </div>
</body>
</html>'''

    css_editor.value = '''/* Simple Template Styles */
* {
    margin: 0;
    padding: 0;
    box-sizing: border-box;
}

body {
    font-family: 'Arial', sans-serif;
    line-height: 1.6;
    color: #333;
}

.simple-page {
    max-width: 1200px;
    margin: 0 auto;
    padding: 20px;
}

header {
    background: #2c3e50;
    color: white;
    padding: 20px;
    text-align: center;
    border-radius: 10px;
    margin-bottom: 30px;
}

nav {
    margin-top: 20px;
}

nav a {
    color: white;
    text-decoration: none;
    margin: 0 15px;
    padding: 5px 10px;
    border-radius: 5px;
    transition: background 0.3s;
}

nav a:hover {
    background: #34495e;
}

.hero {
    text-align: center;
    padding: 60px 20px;
    background: #ecf0f1;
    border-radius: 10px;
    margin-bottom: 40px;
}

.hero h2 {
    font-size: 2.5em;
    margin-bottom: 20px;
    color: #2c3e50;
}

.cta-button {
    background: #e74c3c;
    color: white;
    border: none;
    padding: 15px 30px;
    font-size: 1.2em;
    border-radius: 5px;
    cursor: pointer;
    margin-top: 20px;
    transition: background 0.3s;
}

.cta-button:hover {
    background: #c0392b;
}

.features {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
    gap: 30px;
    margin-bottom: 40px;
}

.feature {
    padding: 30px;
    background: white;
    border-radius: 10px;
    box-shadow: 0 5px 20px rgba(0,0,0,0.1);
    text-align: center;
}

.feature h3 {
    color: #2c3e50;
    margin-bottom: 15px;
}

footer {
    text-align: center;
    padding: 20px;
    background: #34495e;
    color: white;
    border-radius: 10px;
}

@media (max-width: 768px) {
    .features {
        grid-template-columns: 1fr;
    }

    nav a {
        display: block;
        margin: 10px 0;
    }
}'''
    update_preview()

def load_template_card(b=None):
    html_editor.value = '''<!DOCTYPE html>
<html>
<head>
    <title>Card Template</title>
</head>
<body>
    <div class="cards-showcase">
        <h1>Our Services</h1>
        <p class="subtitle">Choose the perfect plan for you</p>

        <div class="card-grid">
            <div class="card">
                <div class="card-icon">🚀</div>
                <h3>Basic Plan</h3>
                <div class="price">$9.99<span>/month</span></div>
                <ul class="features-list">
                    <li>✓ 5 Projects</li>
                    <li>✓ 10GB Storage</li>
                    <li>✓ Basic Support</li>
                </ul>
                <button class="card-btn">Choose Plan</button>
            </div>

            <div class="card popular">
                <div class="popular-badge">Most Popular</div>
                <div class="card-icon">⭐</div>
                <h3>Pro Plan</h3>
                <div class="price">$19.99<span>/month</span></div>
                <ul class="features-list">
                    <li>✓ Unlimited Projects</li>
                    <li>✓ 100GB Storage</li>
                    <li>✓ Priority Support</li>
                    <li>✓ Advanced Features</li>
                </ul>
                <button class="card-btn">Choose Plan</button>
            </div>

            <div class="card">
                <div class="card-icon">👑</div>
                <h3>Enterprise</h3>
                <div class="price">$49.99<span>/month</span></div>
                <ul class="features-list">
                    <li>✓ Everything in Pro</li>
                    <li>✓ 1TB Storage</li>
                    <li>✓ 24/7 Phone Support</li>
                    <li>✓ Custom Solutions</li>
                </ul>
                <button class="card-btn">Contact Us</button>
            </div>
        </div>
    </div>
</body>
</html>'''

    css_editor.value = '''/* Card Template Styles */
* {
    margin: 0;
    padding: 0;
    box-sizing: border-box;
}

body {
    font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
    background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
    min-height: 100vh;
    padding: 40px 20px;
}

.cards-showcase {
    max-width: 1200px;
    margin: 0 auto;
    text-align: center;
}

.cards-showcase h1 {
    font-size: 2.5em;
    color: white;
    margin-bottom: 10px;
    text-shadow: 2px 2px 4px rgba(0,0,0,0.2);
}

.subtitle {
    color: rgba(255,255,255,0.9);
    font-size: 1.2em;
    margin-bottom: 50px;
}

.card-grid {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
    gap: 30px;
    padding: 20px;
}

.card {
    background: white;
    border-radius: 20px;
    padding: 40px 30px;
    position: relative;
    transition: all 0.3s ease;
    box-shadow: 0 10px 30px rgba(0,0,0,0.2);
}

.card:hover {
    transform: translateY(-15px);
    box-shadow: 0 20px 40px rgba(0,0,0,0.3);
}

.card.popular {
    transform: scale(1.05);
    border: 3px solid #ffd700;
    background: linear-gradient(135deg, #fff 0%, #fef9e7 100%);
}

.popular-badge {
    position: absolute;
    top: -15px;
    left: 50%;
    transform: translateX(-50%);
    background: #ffd700;
    color: #333;
    padding: 8px 25px;
    border-radius: 30px;
    font-weight: bold;
    font-size: 0.9em;
    box-shadow: 0 5px 15px rgba(255,215,0,0.3);
}

.card-icon {
    font-size: 4em;
    margin-bottom: 20px;
}

.card h3 {
    font-size: 1.8em;
    color: #333;
    margin-bottom: 15px;
}

.price {
    font-size: 2.5em;
    font-weight: bold;
    color: #667eea;
    margin-bottom: 25px;
}

.price span {
    font-size: 0.4em;
    color: #999;
    font-weight: normal;
}

.features-list {
    list-style: none;
    margin-bottom: 30px;
    text-align: left;
}

.features-list li {
    padding: 10px 0;
    color: #666;
    border-bottom: 1px solid #eee;
}

.features-list li:last-child {
    border-bottom: none;
}

.card-btn {
    background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
    color: white;
    border: none;
    padding: 15px 40px;
    border-radius: 50px;
    font-size: 1.1em;
    font-weight: 600;
    cursor: pointer;
    transition: all 0.3s ease;
    width: 100%;
    text-transform: uppercase;
    letter-spacing: 1px;
}

.card-btn:hover {
    transform: translateY(-2px);
    box-shadow: 0 10px 25px rgba(102, 126, 234, 0.4);
}

@media (max-width: 768px) {
    .card.popular {
        transform: scale(1);
    }

    .card-grid {
        grid-template-columns: 1fr;
    }
}'''
    update_preview()

def load_template_form(b=None):
    html_editor.value = '''<!DOCTYPE html>
<html>
<head>
    <title>Modern Form</title>
</head>
<body>
    <div class="form-page">
        <div class="form-container">
            <div class="form-header">
                <h2>Create Account</h2>
                <p>Join our community today</p>
            </div>

            <form class="modern-form" id="signupForm">
                <div class="form-row">
                    <div class="form-group">
                        <label for="firstName">First Name</label>
                        <input type="text" id="firstName" placeholder="John" required>
                    </div>

                    <div class="form-group">
                        <label for="lastName">Last Name</label>
                        <input type="text" id="lastName" placeholder="Doe" required>
                    </div>
                </div>

                <div class="form-group">
                    <label for="email">Email Address</label>
                    <input type="email" id="email" placeholder="john@example.com" required>
                </div>

                <div class="form-group">
                    <label for="password">Password</label>
                    <input type="password" id="password" placeholder="Create a password" required>
                    <small>Minimum 8 characters</small>
                </div>

                <div class="form-group">
                    <label for="confirmPassword">Confirm Password</label>
                    <input type="password" id="confirmPassword" placeholder="Confirm your password" required>
                </div>

                <div class="form-group">
                    <label for="country">Country</label>
                    <select id="country" required>
                        <option value="">Select your country</option>
                        <option value="us">United States</option>
                        <option value="uk">United Kingdom</option>
                        <option value="ca">Canada</option>
                        <option value="au">Australia</option>
                        <option value="other">Other</option>
                    </select>
                </div>

                <div class="form-group checkbox-group">
                    <label class="checkbox-label">
                        <input type="checkbox" required>
                        <span>I agree to the <a href="#">Terms of Service</a> and <a href="#">Privacy Policy</a></span>
                    </label>
                </div>

                <button type="submit" class="submit-btn">Create Account</button>

                <div class="form-footer">
                    <p>Already have an account? <a href="#">Sign In</a></p>
                </div>
            </form>
        </div>
    </div>

    <script>
        document.getElementById('signupForm').addEventListener('submit', function(e) {
            e.preventDefault();
            alert('Form submitted successfully! (Demo)');
        });
    </script>
</body>
</html>'''

    css_editor.value = '''/* Modern Form Styles */
* {
    margin: 0;
    padding: 0;
    box-sizing: border-box;
}

body {
    font-family: 'Poppins', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;
    background: linear-gradient(135deg, #74b9ff 0%, #a29bfe 100%);
    min-height: 100vh;
    display: flex;
    align-items: center;
    justify-content: center;
    padding: 20px;
}

.form-page {
    width: 100%;
    max-width: 600px;
}

.form-container {
    background: white;
    border-radius: 20px;
    padding: 40px;
    box-shadow: 0 20px 60px rgba(0,0,0,0.3);
    animation: slideUp 0.5s ease;
}

@keyframes slideUp {
    from {
        opacity: 0;
        transform: translateY(30px);
    }
    to {
        opacity: 1;
        transform: translateY(0);
    }
}

.form-header {
    text-align: center;
    margin-bottom: 30px;
}

.form-header h2 {
    font-size: 2.2em;
    color: #2d3436;
    margin-bottom: 10px;
}

.form-header p {
    color: #636e72;
    font-size: 1.1em;
}

.form-row {
    display: grid;
    grid-template-columns: 1fr 1fr;
    gap: 20px;
    margin-bottom: 20px;
}

.form-group {
    margin-bottom: 25px;
}

.form-group label {
    display: block;
    margin-bottom: 8px;
    color: #2d3436;
    font-weight: 500;
    font-size: 0.95em;
}

.form-group input,
.form-group select {
    width: 100%;
    padding: 12px 15px;
    border: 2px solid #dfe6e9;
    border-radius: 10px;
    font-size: 16px;
    transition: all 0.3s ease;
    font-family: inherit;
}

.form-group input:focus,
.form-group select:focus {
    outline: none;
    border-color: #74b9ff;
    box-shadow: 0 0 0 4px rgba(116, 185, 255, 0.1);
}

.form-group input:hover,
.form-group select:hover {
    border-color: #b2bec3;
}

.form-group small {
    display: block;
    margin-top: 5px;
    color: #636e72;
    font-size: 0.85em;
}

.checkbox-group {
    margin: 20px 0;
}

.checkbox-label {
    display: flex;
    align-items: center;
    gap: 10px;
    cursor: pointer;
}

.checkbox-label input[type="checkbox"] {
    width: 20px;
    height: 20px;
    cursor: pointer;
}

.checkbox-label span {
    color: #636e72;
    font-size: 0.95em;
}

.checkbox-label a {
    color: #74b9ff;
    text-decoration: none;
    font-weight: 500;
}

.checkbox-label a:hover {
    text-decoration: underline;
}

.submit-btn {
    width: 100%;
    padding: 15px;
    background: linear-gradient(135deg, #74b9ff 0%, #a29bfe 100%);
    color: white;
    border: none;
    border-radius: 10px;
    font-size: 1.2em;
    font-weight: 600;
    cursor: pointer;
    transition: all 0.3s ease;
    text-transform: uppercase;
    letter-spacing: 1px;
    margin-bottom: 20px;
}

.submit-btn:hover {
    transform: translateY(-2px);
    box-shadow: 0 10px 25px rgba(116, 185, 255, 0.4);
}

.submit-btn:active {
    transform: translateY(0);
}

.form-footer {
    text-align: center;
    color: #636e72;
}

.form-footer a {
    color: #74b9ff;
    text-decoration: none;
    font-weight: 500;
}

.form-footer a:hover {
    text-decoration: underline;
}

/* Error states */
.form-group.error input {
    border-color: #ff7675;
}

.form-group.success input {
    border-color: #00b894;
}

/* Responsive */
@media (max-width: 480px) {
    .form-container {
        padding: 25px;
    }

    .form-row {
        grid-template-columns: 1fr;
        gap: 0;
    }

    .form-header h2 {
        font-size: 1.8em;
    }
}'''
    update_preview()

def load_template_dashboard(b=None):
    html_editor.value = '''<!DOCTYPE html>
<html>
<head>
    <title>Analytics Dashboard</title>
</head>
<body>
    <div class="dashboard">
        <aside class="sidebar">
            <div class="logo">📊 Dashboard</div>
            <nav class="nav-menu">
                <a href="#" class="active">🏠 Home</a>
                <a href="#">📈 Analytics</a>
                <a href="#">📦 Products</a>
                <a href="#">👥 Customers</a>
                <a href="#">⚙️ Settings</a>
            </nav>
            <div class="user-profile">
                <img src="https://via.placeholder.com/40" alt="User">
                <div>
                    <strong>John Doe</strong>
                    <span>Admin</span>
                </div>
            </div>
        </aside>

        <main class="main-content">
            <header class="header">
                <h1>Welcome back, John!</h1>
                <div class="header-actions">
                    <span>🔔</span>
                    <span>📧</span>
                </div>
            </header>

            <div class="stats-grid">
                <div class="stat-card">
                    <div class="stat-icon">💰</div>
                    <div class="stat-info">
                        <h3>$54,239</h3>
                        <p>Total Revenue</p>
                        <span class="trend up">↑ 12.5%</span>
                    </div>
                </div>

                <div class="stat-card">
                    <div class="stat-icon">👥</div>
                    <div class="stat-info">
                        <h3>3,247</h3>
                        <p>Total Users</p>
                        <span class="trend up">↑ 8.2%</span>
                    </div>
                </div>

                <div class="stat-card">
                    <div class="stat-icon">📦</div>
                    <div class="stat-info">
                        <h3>1,482</h3>
                        <p>Orders</p>
                        <span class="trend down">↓ 3.1%</span>
                    </div>
                </div>

                <div class="stat-card">
                    <div class="stat-icon">⭐</div>
                    <div class="stat-info">
                        <h3>4.8</h3>
                        <p>Rating</p>
                        <span class="trend up">↑ 0.3</span>
                    </div>
                </div>
            </div>

            <div class="charts-row">
                <div class="chart-card">
                    <h3>Recent Activity</h3>
                    <div class="activity-list">
                        <div class="activity-item">
                            <span class="time">2 min ago</span>
                            <span>New user registered</span>
                        </div>
                        <div class="activity-item">
                            <span class="time">15 min ago</span>
                            <span>Order #1234 completed</span>
                        </div>
                        <div class="activity-item">
                            <span class="time">1 hour ago</span>
                            <span>Payment received</span>
                        </div>
                    </div>
                </div>

                <div class="chart-card">
                    <h3>Quick Actions</h3>
                    <div class="actions-grid">
                        <button>➕ Add Product</button>
                        <button>📧 Send Email</button>
                        <button>📊 Generate Report</button>
                        <button>⚙️ Update Settings</button>
                    </div>
                </div>
            </div>
        </main>
    </div>
</body>
</html>'''

    css_editor.value = '''/* Dashboard Styles */
* {
    margin: 0;
    padding: 0;
    box-sizing: border-box;
}

body {
    font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, sans-serif;
    background: #f5f6fa;
}

.dashboard {
    display: flex;
    min-height: 100vh;
}

.sidebar {
    width: 250px;
    background: #2c3e50;
    color: white;
    padding: 20px;
    display: flex;
    flex-direction: column;
}

.logo {
    font-size: 1.5em;
    font-weight: bold;
    padding: 20px 0;
    border-bottom: 1px solid #34495e;
    margin-bottom: 20px;
}

.nav-menu {
    flex: 1;
}

.nav-menu a {
    display: block;
    padding: 12px 15px;
    color: #ecf0f1;
    text-decoration: none;
    border-radius: 8px;
    margin-bottom: 5px;
    transition: background 0.3s;
}

.nav-menu a:hover,
.nav-menu a.active {
    background: #34495e;
}

.user-profile {
    display: flex;
    align-items: center;
    gap: 10px;
    padding: 20px 0;
    border-top: 1px solid #34495e;
}

.user-profile img {
    border-radius: 50%;
}

.user-profile div {
    display: flex;
    flex-direction: column;
}

.user-profile span {
    font-size: 0.85em;
    color: #bdc3c7;
}

.main-content {
    flex: 1;
    padding: 20px;
}

.header {
    display: flex;
    justify-content: space-between;
    align-items: center;
    margin-bottom: 30px;
}

.header h1 {
    color: #2c3e50;
}

.header-actions span {
    font-size: 1.5em;
    margin-left: 15px;
    cursor: pointer;
}

.stats-grid {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
    gap: 20px;
    margin-bottom: 30px;
}

.stat-card {
    background: white;
    padding: 20px;
    border-radius: 10px;
    display: flex;
    align-items: center;
    gap: 15px;
    box-shadow: 0 2px 10px rgba(0,0,0,0.1);
}

.stat-icon {
    font-size: 2.5em;
}

.stat-info h3 {
    font-size: 1.5em;
    color: #2c3e50;
    margin-bottom: 5px;
}

.stat-info p {
    color: #7f8c8d;
    margin-bottom: 5px;
}

.trend {
    font-size: 0.85em;
    padding: 3px 8px;
    border-radius: 15px;
}

.trend.up {
    background: #d4edda;
    color: #155724;
}

.trend.down {
    background: #f8d7da;
    color: #721c24;
}

.charts-row {
    display: grid;
    grid-template-columns: 1fr 1fr;
    gap: 20px;
}

.chart-card {
    background: white;
    padding: 20px;
    border-radius: 10px;
    box-shadow: 0 2px 10px rgba(0,0,0,0.1);
}

.chart-card h3 {
    margin-bottom: 20px;
    color: #2c3e50;
}

.activity-list {
    display: flex;
    flex-direction: column;
    gap: 15px;
}

.activity-item {
    display: flex;
    gap: 15px;
    padding: 10px;
    background: #f8f9fa;
    border-radius: 8px;
}

.time {
    color: #7f8c8d;
    font-size: 0.85em;
    min-width: 80px;
}

.actions-grid {
    display: grid;
    grid-template-columns: 1fr 1fr;
    gap: 10px;
}

.actions-grid button {
    padding: 10px;
    background: #3498db;
    color: white;
    border: none;
    border-radius: 5px;
    cursor: pointer;
    transition: background 0.3s;
}

.actions-grid button:hover {
    background: #2980b9;
}

@media (max-width: 768px) {
    .dashboard {
        flex-direction: column;
    }

    .sidebar {
        width: 100%;
    }

    .charts-row {
        grid-template-columns: 1fr;
    }
}'''
    update_preview()

def load_template_landing(b=None):
    html_editor.value = '''<!DOCTYPE html>
<html>
<head>
    <title>Product Launch</title>
</head>
<body>
    <div class="landing-page">
        <nav class="navbar">
            <div class="logo">🚀 LaunchPro</div>
            <div class="nav-links">
                <a href="#">Features</a>
                <a href="#">Pricing</a>
                <a href="#">About</a>
                <a href="#">Contact</a>
                <button class="nav-cta">Get Started</button>
            </div>
        </nav>

        <section class="hero">
            <div class="hero-content">
                <h1>Launch Your Product <span class="gradient-text">Faster</span></h1>
                <p>The all-in-one platform for product launches. Get your product in front of thousands of users today.</p>
                <div class="hero-buttons">
                    <button class="primary-btn">Start Free Trial</button>
                    <button class="secondary-btn">Watch Demo</button>
                </div>
                <div class="hero-stats">
                    <div class="stat">
                        <strong>10K+</strong>
                        <span>Products Launched</span>
                    </div>
                    <div class="stat">
                        <strong>50K+</strong>
                        <span>Happy Customers</span>
                    </div>
                    <div class="stat">
                        <strong>4.9/5</strong>
                        <span>User Rating</span>
                    </div>
                </div>
            </div>
            <div class="hero-image">
                <img src="https://via.placeholder.com/500x400" alt="Hero">
            </div>
        </section>

        <section class="features-section">
            <h2>Everything You Need</h2>
            <p class="section-subtitle">Powerful features to make your launch successful</p>

            <div class="features-grid">
                <div class="feature-card">
                    <div class="feature-icon">⚡</div>
                    <h3>Lightning Fast</h3>
                    <p>Launch your product in minutes, not days.</p>
                </div>

                <div class="feature-card">
                    <div class="feature-icon">📊</div>
                    <h3>Analytics</h3>
                    <p>Track your launch performance in real-time.</p>
                </div>

                <div class="feature-card">
                    <div class="feature-icon">🔒</div>
                    <h3>Secure</h3>
                    <p>Enterprise-grade security for your data.</p>
                </div>

                <div class="feature-card">
                    <div class="feature-icon">💬</div>
                    <h3>24/7 Support</h3>
                    <p>Get help whenever you need it.</p>
                </div>
            </div>
        </section>

        <section class="cta-section">
            <h2>Ready to Launch Your Product?</h2>
            <p>Join thousands of successful product launches today</p>
            <button class="cta-btn">Get Started Now</button>
        </section>

        <footer class="footer">
            <p>&copy; 2024 LaunchPro. All rights reserved.</p>
        </footer>
    </div>
</body>
</html>'''

    css_editor.value = '''/* Landing Page Styles */
* {
    margin: 0;
    padding: 0;
    box-sizing: border-box;
}

body {
    font-family: 'Inter', -apple-system, BlinkMacSystemFont, sans-serif;
    color: #333;
}

.landing-page {
    overflow-x: hidden;
}

/* Navigation */
.navbar {
    display: flex;
    justify-content: space-between;
    align-items: center;
    padding: 20px 50px;
    background: white;
    box-shadow: 0 2px 20px rgba(0,0,0,0.1);
    position: fixed;
    top: 0;
    width: 100%;
    z-index: 1000;
}

.logo {
    font-size: 1.5em;
    font-weight: bold;
    background: linear-gradient(135deg, #667eea, #764ba2);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
}

.nav-links {
    display: flex;
    gap: 30px;
    align-items: center;
}

.nav-links a {
    text-decoration: none;
    color: #4a5568;
    font-weight: 500;
    transition: color 0.3s;
}

.nav-links a:hover {
    color: #667eea;
}

.nav-cta {
    background: linear-gradient(135deg, #667eea, #764ba2);
    color: white;
    border: none;
    padding: 10px 20px;
    border-radius: 25px;
    cursor: pointer;
    font-weight: 600;
    transition: transform 0.3s, box-shadow 0.3s;
}

.nav-cta:hover {
    transform: translateY(-2px);
    box-shadow: 0 5px 15px rgba(102, 126, 234, 0.4);
}

/* Hero Section */
.hero {
    display: grid;
    grid-template-columns: 1fr 1fr;
    gap: 50px;
    padding: 150px 50px 100px;
    background: linear-gradient(135deg, #f5f7fa 0%, #e4e8f0 100%);
    min-height: 100vh;
    align-items: center;
}

.hero-content h1 {
    font-size: 3.5em;
    line-height: 1.2;
    margin-bottom: 20px;
    color: #2d3748;
}

.gradient-text {
    background: linear-gradient(135deg, #667eea, #764ba2);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
}

.hero-content p {
    font-size: 1.2em;
    color: #718096;
    margin-bottom: 30px;
    line-height: 1.6;
}

.hero-buttons {
    display: flex;
    gap: 15px;
    margin-bottom: 40px;
}

.primary-btn {
    background: linear-gradient(135deg, #667eea, #764ba2);
    color: white;
    border: none;
    padding: 15px 30px;
    border-radius: 30px;
    font-size: 1.1em;
    font-weight: 600;
    cursor: pointer;
    transition: transform 0.3s, box-shadow 0.3s;
}

.primary-btn:hover {
    transform: translateY(-2px);
    box-shadow: 0 10px 25px rgba(102, 126, 234, 0.4);
}

.secondary-btn {
    background: transparent;
    color: #667eea;
    border: 2px solid #667eea;
    padding: 13px 28px;
    border-radius: 30px;
    font-size: 1.1em;
    font-weight: 600;
    cursor: pointer;
    transition: all 0.3s;
}

.secondary-btn:hover {
    background: #667eea;
    color: white;
}

.hero-stats {
    display: flex;
    gap: 40px;
}

.hero-stats .stat {
    display: flex;
    flex-direction: column;
}

.hero-stats strong {
    font-size: 1.8em;
    color: #2d3748;
}

.hero-stats span {
    color: #718096;
}

.hero-image img {
    width: 100%;
    border-radius: 20px;
    box-shadow: 0 20px 40px rgba(0,0,0,0.2);
    animation: float 3s ease-in-out infinite;
}

@keyframes float {
    0%, 100% { transform: translateY(0); }
    50% { transform: translateY(-20px); }
}

/* Features Section */
.features-section {
    padding: 100px 50px;
    text-align: center;
}

.features-section h2 {
    font-size: 2.5em;
    color: #2d3748;
    margin-bottom: 15px;
}

.section-subtitle {
    color: #718096;
    font-size: 1.2em;
    margin-bottom: 50px;
}

.features-grid {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
    gap: 30px;
    max-width: 1200px;
    margin: 0 auto;
}

.feature-card {
    padding: 40px 30px;
    background: white;
    border-radius: 15px;
    box-shadow: 0 10px 30px rgba(0,0,0,0.1);
    transition: transform 0.3s;
}

.feature-card:hover {
    transform: translateY(-10px);
}

.feature-icon {
    font-size: 3em;
    margin-bottom: 20px;
}

.feature-card h3 {
    font-size: 1.3em;
    margin-bottom: 15px;
    color: #2d3748;
}

.feature-card p {
    color: #718096;
    line-height: 1.6;
}

/* CTA Section */
.cta-section {
    background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
    padding: 100px 50px;
    text-align: center;
    color: white;
}

.cta-section h2 {
    font-size: 2.5em;
    margin-bottom: 20px;
}

.cta-section p {
    font-size: 1.2em;
    margin-bottom: 30px;
    opacity: 0.9;
}

.cta-btn {
    background: white;
    color: #667eea;
    border: none;
    padding: 18px 40px;
    border-radius: 40px;
    font-size: 1.2em;
    font-weight: 600;
    cursor: pointer;
    transition: transform 0.3s, box-shadow 0.3s;
}

.cta-btn:hover {
    transform: translateY(-2px);
    box-shadow: 0 10px 25px rgba(0,0,0,0.2);
}

/* Footer */
.footer {
    text-align: center;
    padding: 30px;
    background: #2d3748;
    color: white;
}

/* Responsive */
@media (max-width: 768px) {
    .navbar {
        flex-direction: column;
        padding: 15px;
        position: relative;
    }

    .nav-links {
        flex-direction: column;
        gap: 15px;
        margin-top: 15px;
    }

    .hero {
        grid-template-columns: 1fr;
        padding: 80px 20px 50px;
        text-align: center;
    }

    .hero-content h1 {
        font-size: 2.5em;
    }

    .hero-buttons {
        justify-content: center;
    }

    .hero-stats {
        justify-content: center;
    }

    .features-section {
        padding: 60px 20px;
    }

    .cta-section {
        padding: 60px 20px;
    }
}'''
    update_preview()

# Function for fullscreen preview
def fullscreen_preview(b=None):
    html_content = html_editor.value
    css_content = css_editor.value

    if '<html' not in html_content:
        full_html = f"""
        <!DOCTYPE html>
        <html>
        <head>
            <meta charset="UTF-8">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <style>
                {css_content}
            </style>
        </head>
        <body>
            {html_content}
        </body>
        </html>
        """
    else:
        full_html = html_content

    # Create a new window with the preview
    display(Javascript(f'''
        var newWindow = window.open("about:blank", "_blank");
        newWindow.document.write({json.dumps(full_html)});
        newWindow.document.close();
    '''))

    message.value = '<span style="color:#28a745; font-weight:bold;">✓ Opened in new window!</span>'

# Function to copy to clipboard
def copy_to_clipboard(b=None):
    full_html = f"{html_editor.value}\n\n<style>\n{css_editor.value}\n</style>"

    display(Javascript(f'''
        navigator.clipboard.writeText({json.dumps(full_html)}).then(function() {{
            alert('Copied to clipboard!');
        }});
    '''))

    message.value = '<span style="color:#28a745; font-weight:bold;">✓ Copied to clipboard!</span>'

# Function to reset to default
def reset_to_default(b=None):
    html_editor.value = '''<div class="container">
    <h1>Welcome to HTML Quick Styler</h1>
    <p>This is a paragraph with some text.</p>
    <button class="btn">Click Me!</button>
    <div class="box">Box 1</div>
    <div class="box special">Box 2</div>
</div>'''

    css_editor.value = '''body {
    font-family: Arial, sans-serif;
    margin: 20px;
    background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
    min-height: 100vh;
}

.container {
    max-width: 800px;
    margin: 0 auto;
    background: white;
    padding: 30px;
    border-radius: 15px;
    box-shadow: 0 10px 30px rgba(0,0,0,0.2);
}

h1 {
    color: #333;
    text-align: center;
    border-bottom: 3px solid #667eea;
    padding-bottom: 10px;
}

p {
    color: #666;
    line-height: 1.6;
    font-size: 16px;
}

.btn {
    background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
    color: white;
    border: none;
    padding: 12px 30px;
    border-radius: 25px;
    font-size: 16px;
    cursor: pointer;
    transition: transform 0.3s, box-shadow 0.3s;
    margin: 10px 0;
    display: inline-block;
}

.btn:hover {
    transform: translateY(-2px);
    box-shadow: 0 5px 15px rgba(102, 126, 234, 0.4);
}

.box {
    background: #f0f0f0;
    padding: 20px;
    margin: 10px 0;
    border-radius: 8px;
    border-left: 4px solid #667eea;
    transition: all 0.3s;
}

.box:hover {
    transform: translateX(5px);
    box-shadow: 0 5px 15px rgba(0,0,0,0.1);
}

.special {
    background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
    color: white;
    border-left: 4px solid #ff6b6b;
}'''
    update_preview()
    message.value = '<span style="color:#28a745; font-weight:bold;">✓ Reset to default template</span>'

# Attach functions to buttons
update_button.on_click(update_preview)
save_button.on_click(save_html)
clear_button.on_click(clear_all)
template_simple.on_click(load_template_simple)
template_card.on_click(load_template_card)
template_form.on_click(load_template_form)
template_dashboard.on_click(load_template_dashboard)
template_landing.on_click(load_template_landing)
fullscreen_button.on_click(fullscreen_preview)
copy_button.on_click(copy_to_clipboard)
reset_button.on_click(reset_to_default)

# Create button rows
template_row1 = widgets.HBox(
    [template_simple, template_card, template_form],
    layout=widgets.Layout(
        justify_content='center',
        margin='5px 0',
        flex_wrap='wrap'
    )
)

template_row2 = widgets.HBox(
    [template_dashboard, template_landing],
    layout=widgets.Layout(
        justify_content='center',
        margin='5px 0',
        flex_wrap='wrap'
    )
)

button_row1 = widgets.HBox(
    [update_button, save_button, clear_button],
    layout=widgets.Layout(
        justify_content='center',
        margin='5px 0',
        flex_wrap='wrap'
    )
)

button_row2 = widgets.HBox(
    [fullscreen_button, copy_button, reset_button],
    layout=widgets.Layout(
        justify_content='center',
        margin='5px 0',
        flex_wrap='wrap'
    )
)

# Create tabs
tabs.children = [html_editor, css_editor]
tabs.set_title(0, '📝 HTML Editor')
tabs.set_title(1, '🎨 CSS Editor')

# Style the tabs
tabs.style = {'tab_height': '40px'}

# Add header with custom styling
header_html = widgets.HTML(
    value='''
    <div style="
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        padding: 30px;
        border-radius: 15px;
        margin-bottom: 20px;
        text-align: center;
        box-shadow: 0 10px 30px rgba(0,0,0,0.2);
    ">
        <h1 style="
            color: white;
            font-size: 2.5em;
            margin: 0;
            text-shadow: 2px 2px 4px rgba(0,0,0,0.2);
        ">
            🎨 HTML Quick Styler
        </h1>
        <p style="
            color: rgba(255,255,255,0.9);
            font-size: 1.2em;
            margin: 10px 0 0 0;
        ">
            Edit HTML and CSS, see the results instantly!
            Choose from 5 beautiful templates to get started.
        </p>
    </div>
    '''
)

# Instructions
instructions = widgets.HTML(
    value='''
    <div style="
        background: #e3f2fd;
        padding: 15px;
        border-radius: 10px;
        margin: 10px 0;
        border-left: 5px solid #2196f3;
    ">
        <strong>💡 Quick Tips:</strong>
        <ul style="margin: 10px 0 0 20px; color: #555;">
            <li>Edit HTML/CSS in the tabs above</li>
            <li>Click "Update Preview" to see changes</li>
            <li>Try different templates to learn</li>
            <li>Save your work as a complete HTML file</li>
            <li>Use fullscreen mode for better preview</li>
        </ul>
    </div>
    '''
)

# Assemble the complete interface
container.children = [
    header_html,
    tabs,
    instructions,
    widgets.HTML("<h3 style='color:#667eea; margin:15px 0 10px;'>📋 Quick Templates</h3>"),
    template_row1,
    template_row2,
    widgets.HTML("<h3 style='color:#667eea; margin:15px 0 10px;'>🛠️ Controls</h3>"),
    button_row1,
    button_row2,
    widgets.HTML("<h3 style='color:#667eea; margin:15px 0 10px;'>👁️ Preview</h3>"),
    preview_output,
    stats_area,
    message
]

# Display the complete interface
display(container)

# Initial preview and stats
update_preview()
update_stats()

print("\n" + "="*50)
print("✅ HTML Quick Styler loaded successfully!")
print("📝 Available templates: Simple, Cards, Form, Dashboard, Landing")
print("🎯 Features: Live preview, Export HTML, Fullscreen, Copy to clipboard")
print("="*50)