# Create the page layout
page_layout = """---
layout: default
---

<div class="page-header">
    <div class="container">
        <h1>{{ page.title }}</h1>
        {% if page.subtitle %}
            <p class="subtitle">{{ page.subtitle }}</p>
        {% endif %}
    </div>
</div>

<div class="container">
    <div class="content">
        {{ content }}
    </div>
</div>"""

with open('_layouts/page.html', 'w', encoding='utf-8') as f:
    f.write(page_layout)
    
print("Created _layouts/page.html")