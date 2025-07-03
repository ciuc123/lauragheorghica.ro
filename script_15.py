# Create robots.txt file
robots_content = """User-agent: *
Disallow: /assets/
Disallow: /_site/
Disallow: /.git/
Disallow: /.github/

Allow: /

Sitemap: https://YOUR-USERNAME.github.io/sitemap.xml

# Note: Update the Sitemap URL with your actual GitHub Pages URL"""

with open('robots.txt', 'w', encoding='utf-8') as f:
    f.write(robots_content)
    
print("Created robots.txt")