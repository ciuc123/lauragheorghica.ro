# 🚀 Deployment Checklist for Laura Gheorghica Jekyll Site

## Before Deployment

- [ ] **Review content** - Check all pages for accuracy
- [ ] **Update contact info** - Verify email and phone number
- [ ] **Test locally** - Run `bundle exec jekyll serve` if possible
- [ ] **Customize colors** - Adjust theme colors in style.css if needed

## GitHub Setup

- [ ] **Create repository** - Name it `username.github.io` or `project-name`
- [ ] **Upload files** - Upload all files from the zip archive
- [ ] **Enable GitHub Pages**:
  - Go to repository Settings
  - Scroll to "Pages" section
  - Select "Source: GitHub Actions"
- [ ] **Update _config.yml**:
  - Change `url` to your GitHub Pages URL
  - Update `baseurl` if using project site

## After Deployment

- [ ] **Test website** - Visit your GitHub Pages URL
- [ ] **Test navigation** - Check all menu links work
- [ ] **Test contact form** - Verify form functionality
- [ ] **Check mobile** - Test on mobile devices
- [ ] **SEO check** - Verify meta tags and descriptions

## Optional Enhancements

- [ ] **Custom domain** - Set up custom domain if desired
- [ ] **Form service** - Set up Formspree or Netlify Forms
- [ ] **Analytics** - Add Google Analytics
- [ ] **Profile image** - Add Laura's photo to replace placeholder
- [ ] **Social media** - Add more social media links

## Contact Form Upgrade

For better contact form functionality:

1. **Formspree (Recommended)**:
   - Sign up at formspree.io
   - Get your form endpoint
   - Update contact.html form action

2. **Netlify Forms**:
   - Deploy to Netlify instead of GitHub Pages
   - Add `netlify` attribute to form

## Support

If you encounter issues:
- Check GitHub Actions tab for deployment errors
- Verify all file paths are correct
- Test in incognito/private browser mode
- Check browser console for JavaScript errors

## Content Updates

To update content:
1. Edit the relevant HTML files
2. Commit changes to GitHub
3. Site will automatically rebuild and deploy

## Maintenance

- Regularly update gems in Gemfile
- Monitor GitHub security alerts
- Keep content fresh and updated
- Test form functionality periodically

---

🎉 **Congratulations!** You now have a professional Jekyll website ready for Laura Gheorghica's relationship counseling services.

For any technical questions, refer to the README.md file or Jekyll documentation.
