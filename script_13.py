# Create a README file with setup instructions
readme_content = """# Laura Gheorghica - Educație Relațională

Static Jekyll website for Laura Gheorghica's relationship counseling services.

## Quick Setup

1. **Upload files to GitHub**:
   - Create a new repository on GitHub
   - Upload all these files to your repository
   - Name your repository `username.github.io` (for user site) or any name (for project site)

2. **Configure GitHub Pages**:
   - Go to your repository Settings
   - Scroll down to "Pages" section
   - Under "Source", select "GitHub Actions"
   - The site will automatically build and deploy

3. **Update configuration**:
   - Edit `_config.yml` file
   - Change the `url` to your GitHub Pages URL
   - Update `baseurl` if needed (for project sites)

## File Structure

```
├── _config.yml          # Jekyll configuration
├── _layouts/            # HTML templates
│   ├── default.html     # Main layout
│   └── page.html        # Page layout
├── _includes/           # Reusable HTML components
│   ├── header.html      # Site header
│   └── footer.html      # Site footer
├── assets/              # CSS, JS, images
│   ├── css/style.css    # Main stylesheet
│   └── js/main.js       # JavaScript functionality
├── .github/workflows/   # GitHub Actions
│   └── jekyll-gh-pages.yml  # Deployment workflow
├── Gemfile              # Ruby dependencies
├── index.html           # Homepage
├── despre.html          # About page
├── servicii.html        # Services page
├── contact.html         # Contact page
└── README.md           # This file
```

## Customization

### Updating Content

1. **Homepage** (`index.html`):
   - Edit hero section text
   - Update services information
   - Modify about section

2. **About Page** (`despre.html`):
   - Add personal story
   - Update experience details
   - Change philosophy section

3. **Services Page** (`servicii.html`):
   - Modify service descriptions
   - Update pricing information
   - Add new services

4. **Contact Page** (`contact.html`):
   - Update contact information
   - Modify form fields
   - Add location details

### Styling

- Edit `assets/css/style.css` to change colors, fonts, layout
- Current color scheme uses blue/purple gradients with red accents
- Font combination: Playfair Display (headings) + Inter (body)

### Contact Form

The contact form currently uses `mailto:` links as fallback. For better functionality, consider:

1. **Formspree** (recommended):
   - Sign up at formspree.io
   - Replace form action with Formspree endpoint
   - Update JavaScript in `assets/js/main.js`

2. **Netlify Forms**:
   - Add `netlify` attribute to form
   - Deploy to Netlify instead of GitHub Pages

3. **EmailJS**:
   - Set up EmailJS account
   - Update JavaScript with EmailJS configuration

## Domain Setup

To use a custom domain:

1. Buy a domain from a registrar
2. Add a `CNAME` file to your repository with your domain name
3. Configure DNS records at your registrar
4. Update `_config.yml` with your custom domain

## Local Development

To run locally:

```bash
# Install Ruby and Bundler
gem install bundler

# Install dependencies
bundle install

# Run local server
bundle exec jekyll serve

# Open http://localhost:4000
```

## SEO Optimization

The site includes:
- Jekyll SEO Tag plugin
- Meta descriptions
- Structured data
- Sitemap generation
- Social media optimization

## Performance

- Optimized CSS and JavaScript
- Responsive design
- Fast loading times
- Mobile-friendly

## Support

For technical issues:
- Check GitHub Actions logs for deployment errors
- Verify file paths and URLs
- Test contact form functionality

## License

This website template is created for Laura Gheorghica's personal use.

---

**Note**: Remember to update the contact information and personalize the content before going live!"""

with open('README.md', 'w', encoding='utf-8') as f:
    f.write(readme_content)
    
print("Created README.md")