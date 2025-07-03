# Create the _includes directory
os.makedirs('_includes', exist_ok=True)

# Create the header include
header_include = """<header class="site-header">
    <div class="container">
        <nav class="navbar">
            <div class="navbar-brand">
                <a href="{{ '/' | relative_url }}">
                    <h2>{{ site.title }}</h2>
                </a>
            </div>
            
            <div class="navbar-toggle" id="navbar-toggle">
                <span></span>
                <span></span>
                <span></span>
            </div>
            
            <div class="navbar-menu" id="navbar-menu">
                <ul class="navbar-nav">
                    {% for item in site.navigation %}
                        <li class="nav-item">
                            <a href="{{ item.url | relative_url }}" class="nav-link {% if page.url == item.url %}active{% endif %}">
                                {{ item.title }}
                            </a>
                        </li>
                    {% endfor %}
                </ul>
            </div>
        </nav>
    </div>
</header>"""

with open('_includes/header.html', 'w', encoding='utf-8') as f:
    f.write(header_include)
    
print("Created _includes/header.html")