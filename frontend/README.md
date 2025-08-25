# Portfolio Frontend

This is the frontend application for the portfolio website, built with modern vanilla JavaScript, HTML5, and CSS3. It's a standalone application that consumes the backend API to display portfolio information.

## 🚀 Quick Start

### Prerequisites
- Node.js 16+ 
- npm or yarn package manager

### Installation

1. **Navigate to frontend directory**
   ```bash
   cd frontend
   ```

2. **Install dependencies**
   ```bash
   npm install
   ```

3. **Start development server**
   ```bash
   npm run dev
   ```

The frontend will start on `http://localhost:3000`

## 🏗️ Architecture

### Modern JavaScript
- ES6+ features (classes, async/await, arrow functions)
- Module-based architecture
- Fetch API for HTTP requests
- Local storage for theme persistence

### Responsive Design
- Mobile-first approach
- CSS Grid and Flexbox layouts
- CSS custom properties (variables)
- Smooth animations and transitions

### API Integration
- RESTful API consumption
- Error handling and fallbacks
- Loading states and user feedback

## 📁 File Structure

```
frontend/
├── src/
│   ├── index.html          # Main HTML file
│   ├── js/
│   │   └── main.js         # Main JavaScript application
│   └── styles/
│       └── main.css        # Main CSS styles
├── package.json            # Node.js dependencies
├── vite.config.js          # Vite configuration
└── README.md               # This file
```

## 🎨 Features

### Core Functionality
- **Portfolio Display**: Showcase skills, projects, and experience
- **Responsive Navigation**: Mobile-friendly navigation with smooth scrolling
- **Contact Form**: Functional contact form with API integration
- **Theme Switching**: Dark/light theme toggle with local storage
- **Animations**: Smooth scroll animations and hover effects

### User Experience
- **Loading States**: Visual feedback during API calls
- **Error Handling**: Graceful fallbacks and user notifications
- **Responsive Design**: Works on all device sizes
- **Accessibility**: Semantic HTML and keyboard navigation

## 🔧 Development

### Available Scripts

```bash
# Development server with hot reload
npm run dev

# Build for production
npm run build

# Preview production build
npm run preview

# Serve production build locally
npm run serve
```

### Development Workflow

1. **Start backend server** (runs on port 5000)
2. **Start frontend dev server** (runs on port 3000)
3. **Make changes** to HTML, CSS, or JavaScript
4. **See changes instantly** with hot reload
5. **Build for production** when ready

### Code Organization

#### JavaScript (`src/js/main.js`)
- **APIService**: Handles all API communication
- **PortfolioManager**: Main application logic
- **Event Handlers**: User interaction management
- **DOM Manipulation**: Dynamic content rendering

#### CSS (`src/styles/main.css`)
- **CSS Variables**: Theme colors and spacing
- **Component Styles**: Modular CSS organization
- **Responsive Design**: Mobile-first breakpoints
- **Animations**: CSS transitions and keyframes

#### HTML (`src/index.html`)
- **Semantic Structure**: Proper HTML5 elements
- **Accessibility**: ARIA labels and semantic markup
- **SEO Optimization**: Meta tags and structured data

## 🎨 Customization

### Personal Information
Update your portfolio data in `src/js/main.js`:
```javascript
getFallbackData() {
    return {
        personal_info: {
            name: 'Your Name',
            title: 'Your Title',
            bio: 'Your bio here...',
            // ... more data
        }
    };
}
```

### Styling
Modify the design in `src/styles/main.css`:
```css
:root {
    --primary-color: #your-color;
    --secondary-color: #your-color;
    /* ... more variables */
}
```

### Content
Update the HTML structure in `src/index.html` to match your needs.

## 🚀 Deployment

### Production Build
```bash
npm run build
```

This creates a `dist/` folder with optimized, production-ready files.

### Deployment Options

#### Vercel (Recommended)
1. Install Vercel CLI: `npm i -g vercel`
2. Run: `vercel` in the frontend directory
3. Follow prompts to deploy

#### Netlify
1. Drag and drop the `dist/` folder to Netlify
2. Or connect your GitHub repository for auto-deploy

#### GitHub Pages
1. Push `dist/` folder to `gh-pages` branch
2. Enable GitHub Pages in repository settings

#### Any Static Hosting
Upload the contents of the `dist/` folder to any web server.

### Environment Configuration

For production, update the API base URL in `src/js/main.js`:
```javascript
const API_BASE_URL = 'https://your-backend-domain.com/api';
```

## 🔧 Build Tools

### Vite
- **Fast Development**: Instant hot reload
- **Optimized Builds**: Production-ready output
- **Modern Features**: ES modules and modern JavaScript

### Configuration
The `vite.config.js` file configures:
- Source directory (`src/`)
- Output directory (`dist/`)
- Development server settings
- Build optimization

## 📱 Responsive Design

### Breakpoints
- **Mobile**: 320px - 768px
- **Tablet**: 768px - 1024px
- **Desktop**: 1024px+

### Mobile-First Approach
- Base styles for mobile devices
- Progressive enhancement for larger screens
- Touch-friendly interactions
- Optimized navigation for small screens

## 🎭 Theme System

### Light Theme (Default)
- Clean, professional appearance
- High contrast for readability
- Subtle shadows and borders

### Dark Theme
- Modern, sleek appearance
- Reduced eye strain
- Consistent color scheme

### Theme Persistence
- User preference saved in localStorage
- Automatic theme restoration
- Smooth transitions between themes

## 🚀 Performance

### Optimization Features
- **Minified CSS/JS**: Production builds are optimized
- **Efficient Selectors**: CSS optimized for performance
- **Lazy Loading**: Images and content loaded as needed
- **Smooth Animations**: Hardware-accelerated CSS transitions

### Best Practices
- Semantic HTML for better SEO
- Optimized images and assets
- Minimal JavaScript bundle
- Efficient DOM manipulation

## 🐛 Troubleshooting

### Common Issues

1. **API Connection Errors**
   - Ensure backend server is running
   - Check API base URL configuration
   - Verify CORS settings on backend

2. **Build Errors**
   - Clear `node_modules` and reinstall
   - Check Node.js version compatibility
   - Verify all dependencies are installed

3. **Styling Issues**
   - Check CSS variable definitions
   - Verify browser compatibility
   - Clear browser cache

### Debug Mode
```bash
# Enable verbose logging
npm run dev -- --debug

# Check browser console for errors
# Use browser dev tools for debugging
```

## 📝 License

This frontend is part of the portfolio project and follows the same MIT license.

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Test on multiple devices/browsers
5. Submit a pull request

---

**Note**: This frontend is designed to work with the Flask backend API. Make sure the backend server is running before testing the frontend functionality.
