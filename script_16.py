# List all created files
import os

def list_files(directory, prefix=""):
    items = []
    for item in sorted(os.listdir(directory)):
        if item.startswith('.'):
            continue
        path = os.path.join(directory, item)
        if os.path.isdir(path):
            items.append(f"{prefix}📁 {item}/")
            items.extend(list_files(path, prefix + "  "))
        else:
            items.append(f"{prefix}📄 {item}")
    return items

print("🎉 Jekyll Site Created Successfully!")
print("\nFile Structure:")
print("=" * 50)

# List all files
for item in list_files("."):
    print(item)

print("\n" + "=" * 50)
print("📋 Summary:")
print("- Jekyll static site configured for GitHub Pages")
print("- Responsive design with mobile navigation")
print("- Contact form with validation")
print("- SEO optimized with meta tags")
print("- Romanian language content")
print("- Professional styling with gradient themes")
print("- GitHub Actions for automatic deployment")

print("\n🚀 Next Steps:")
print("1. Create a new GitHub repository")
print("2. Upload all these files to your repository")
print("3. Enable GitHub Pages in repository settings")
print("4. Update _config.yml with your GitHub Pages URL")
print("5. Test the contact form functionality")
print("6. Customize content and styling as needed")

print("\n📧 Contact form note:")
print("The contact form uses mailto: links as fallback.")
print("For better functionality, consider using Formspree or Netlify Forms.")

print("\n✅ All files are ready for deployment!")