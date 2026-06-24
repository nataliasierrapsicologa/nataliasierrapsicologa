import re

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

replacements = [
    (r'font-size: 1\.1rem;(?!.*font-size)', r'font-size: 1.25rem;'), # body
    (r'font-size: clamp\(2\.5rem, 5vw, 3\.5rem\);', r'font-size: clamp(3rem, 6vw, 4.5rem);'),
    (r'\.hero-left p \{\n\s*font-size: 1rem;', r'.hero-left p {\n      font-size: 1.2rem;'),
    (r'font-size: clamp\(2rem, 4vw, 3rem\);', r'font-size: clamp(2.5rem, 5vw, 4rem);'),
    (r'\.hero-price-label \{\n\s*font-size: 1rem;', r'.hero-price-label {\n      font-size: 1.2rem;'),
    (r'font-size: clamp\(1\.8rem, 3\.5vw, 2\.5rem\);', r'font-size: clamp(2.2rem, 4vw, 3.5rem);'),
    (r'\.btn-outline \{\n\s*display: inline-block;\n\s*padding: 1\.2rem 3\.5rem;\n\s*border: 1px solid var\(--text\);\n\s*color: var\(--text\);\n\s*text-decoration: none;\n\s*text-transform: uppercase;\n\s*font-size: 0\.85rem;', 
     r'.btn-outline {\n      display: inline-block;\n      padding: 1.2rem 4rem;\n      border: 1px solid var(--text);\n      color: var(--text);\n      text-decoration: none;\n      text-transform: uppercase;\n      font-size: 1.1rem;'),
    (r'\.section-title \{\n\s*font-size: 2\.5rem;', r'.section-title {\n      font-size: 3rem;'),
    (r'\.about-left h2 \{\n\s*font-size: 2\.5rem;', r'.about-left h2 {\n      font-size: 3.5rem;'),
    (r'\.about-left p \{\n\s*margin-bottom: 1\.5rem;\n\s*font-size: 1\.15rem;', r'.about-left p {\n      margin-bottom: 1.5rem;\n      font-size: 1.25rem;'),
    (r'\.about-right img \{\n\s*width: 100%;\n\s*max-width: 400px;\n\s*border-radius: 4px;', r'.about-right img {\n      width: 100%;\n      max-width: 600px;\n      border-radius: 8px;'),
    (r'\.area-box \{\n\s*background-color: var\(--box-bg\);\n\s*padding: 3rem 2rem;\n\s*text-align: center;\n\s*font-family: \'Fraunces\', serif;\n\s*font-size: 1\.2rem;', r'.area-box {\n      background-color: var(--box-bg);\n      padding: 3rem 2rem;\n      text-align: center;\n      font-family: \'Fraunces\', serif;\n      font-size: 1.5rem;'),
    (r'\.step-number \{\n\s*color: var\(--accent\);\n\s*font-family: \'Fraunces\', serif;\n\s*font-size: 1\.2rem;', r'.step-number {\n      color: var(--accent);\n      font-family: \'Fraunces\', serif;\n      font-size: 1.5rem;'),
    (r'\.method-step h3 \{\n\s*font-size: 1\.1rem;', r'.method-step h3 {\n      font-size: 1.3rem;'),
    (r'\.method-step p \{\n\s*font-size: 0\.85rem;', r'.method-step p {\n      font-size: 1.1rem;'),
    (r'\.stars \{\n\s*color: var\(--accent\);\n\s*letter-spacing: 2px;\n\s*margin-bottom: 1\.5rem;\n\s*font-size: 1\.2rem;', r'.stars {\n      color: var(--accent);\n      letter-spacing: 2px;\n      margin-bottom: 1.5rem;\n      font-size: 1.5rem;'),
    (r'\.review-quote \{\n\s*font-size: 0\.95rem;', r'.review-quote {\n      font-size: 1.15rem;'),
    (r'\.review-author \{\n\s*font-family: \'Fraunces\', serif;\n\s*font-size: 1rem;', r'.review-author {\n      font-family: \'Fraunces\', serif;\n      font-size: 1.2rem;'),
    (r'\.review-date \{\n\s*font-size: 0\.8rem;', r'.review-date {\n      font-size: 1rem;'),
    (r'\.contact-label \{\n\s*font-size: 1rem;', r'.contact-label {\n      font-size: 1.2rem;'),
    (r'\.contact-email \{\n\s*color: var\(--text\);\n\s*text-decoration: none;\n\s*font-size: 0\.9rem;', r'.contact-email {\n      color: var(--text);\n      text-decoration: none;\n      font-size: 1.1rem;'),
    (r'\.contact-right h3 \{\n\s*font-size: 1\.5rem;', r'.contact-right h3 {\n      font-size: 2rem;'),
    (r'\.form-group label \{\n\s*display: block;\n\s*font-size: 0\.85rem;', r'.form-group label {\n      display: block;\n      font-size: 1rem;'),
    (r'\.form-group input,\n\s*\.form-group textarea \{\n\s*width: 100%;\n\s*padding: 0\.8rem;\n\s*background-color: var\(--input-bg\);\n\s*border: 1px solid rgba\(0,0,0,0\.2\);\n\s*font-family: \'Onest\', sans-serif;\n\s*font-size: 0\.9rem;', r'.form-group input,\n    .form-group textarea {\n      width: 100%;\n      padding: 0.8rem;\n      background-color: var(--input-bg);\n      border: 1px solid rgba(0,0,0,0.2);\n      font-family: \'Onest\', sans-serif;\n      font-size: 1.1rem;'),
    (r'\.btn-submit \{\n\s*width: 100%;\n\s*background-color: var\(--accent\);\n\s*color: #fff;\n\s*border: none;\n\s*padding: 1rem;\n\s*font-size: 1rem;', r'.btn-submit {\n      width: 100%;\n      background-color: var(--accent);\n      color: #fff;\n      border: none;\n      padding: 1.2rem;\n      font-size: 1.2rem;'),
    (r'\.footer-grid \{\n\s*display: grid;\n\s*grid-template-columns: 1fr 1fr 1fr;\n\s*gap: 2rem;\n\s*font-size: 0\.85rem;', r'.footer-grid {\n      display: grid;\n      grid-template-columns: 1fr 1fr 1fr;\n      gap: 2rem;\n      font-size: 1rem;'),
    (r'\.center-col h4 \{\n\s*margin-bottom: 1rem;\n\s*font-size: 1rem;', r'.center-col h4 {\n      margin-bottom: 1rem;\n      font-size: 1.2rem;'),
    (r'\.footer-bottom \{\n\s*display: flex;\n\s*justify-content: space-between;\n\s*font-size: 0\.75rem;', r'.footer-bottom {\n      display: flex;\n      justify-content: space-between;\n      font-size: 0.9rem;'),
    (r'\.nav-links a \{\n\s*text-decoration: none;\n\s*color: var\(--text\);\n\s*font-size: 0\.8rem;', r'.nav-links a {\n      text-decoration: none;\n      color: var(--text);\n      font-size: 1rem;'),
    (r'\.nav-cta \{\n\s*background-color: var\(--accent\);\n\s*color: #fff;\n\s*padding: 0\.7rem 1\.5rem;\n\s*text-decoration: none;\n\s*font-size: 0\.9rem;', r'.nav-cta {\n      background-color: var(--accent);\n      color: #fff;\n      padding: 0.8rem 1.8rem;\n      text-decoration: none;\n      font-size: 1.1rem;')
]

for old, new in replacements:
    content = re.sub(old, new, content)

# Since body font size regex above might be tricky, let's explicitly target it:
content = re.sub(r'body \{\n\s*font-family: \'Onest\', sans-serif;\n\s*font-weight: 300;\n\s*background-color: var\(--bg\);\n\s*color: var\(--text\);\n\s*line-height: 1\.6;\n\s*font-size: 1\.1rem;', 
                 r'body {\n      font-family: \'Onest\', sans-serif;\n      font-weight: 300;\n      background-color: var(--bg);\n      color: var(--text);\n      line-height: 1.6;\n      font-size: 1.25rem;', content)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(content)
