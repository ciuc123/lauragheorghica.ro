# Create the _layouts directory
os.makedirs('_layouts', exist_ok=True)

# Create the default layout
default_layout = """<!DOCTYPE html>
<html lang="ro">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{% if page.title %}{{ page.title }} - {% endif %}{{ site.title }}</title>
    <meta name="description" content="{{ page.description | default: site.description }}">
    
    <!-- SEO -->
    {% seo %}
    
    <!-- CSS -->
    <link rel="stylesheet" href="{{ '/assets/css/style.css' | relative_url }}">
    
    <!-- Fonts -->
    <link href="https://fonts.googleapis.com/css2?family=Playfair+Display:wght@400;700&family=Inter:wght@300;400;500;600&display=swap" rel="stylesheet">
    
    <!-- Icons -->
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0/css/all.min.css">
</head>
<body>
    {% include header.html %}
    
    <main>
        {{ content }}
    </main>
    
    {% include footer.html %}
    
    <!-- JavaScript -->
    <script src="{{ '/assets/js/main.js' | relative_url }}"></script>
</body>
</html>"""

with open('_layouts/default.html', 'w', encoding='utf-8') as f:
    f.write(default_layout)
    
print("Created _layouts/default.html")