# Weldork Copilot Instructions

## Project Overview

Weldork is a Bootstrap-based HTML template for welding/industrial business websites. It's a static site with 9 core pages using shared components and libraries. There's no build process, bundler, or backend—assets are served directly and CDN dependencies are loaded in each HTML file.

## Architecture

### Page Structure

- **Core Pages**: `index.html`, `about.html`, `service.html`, `team.html`, `testimonial.html`, `contact.html`, `404.html`
- **Shared Pattern**: Every page has identical `<head>` structure with the same CSS/library links and Bootstrap navbar
- **Head Template**: Located at the top of each `.html` file (lines 1-35 approx)
  - Google Fonts: Poppins (400, 600), Roboto (700, 800)
  - Icon libraries: Font Awesome 5.10.0, Bootstrap Icons 1.10.4
  - Libraries: WOW.js (animations), Owl Carousel (image carousels)
  - CSS load order: Bootstrap min → libraries → custom styles

### Component Reuse

- **Navbar** (lines ~45-70 in each page): `sticky-top` with responsive collapse
- **Topbar** (lines ~40-60): Contact info visible only on lg+ screens, social links via Font Awesome
- **Spinner** (lines ~35-40): Loading spinner with fade transition, removed on page load
- **Back-to-top button**: Fixed position, triggered at scroll > 300px

### Styling Approach

- **Bootstrap customization**: Uses `css/bootstrap.min.css` (customized version)
- **Template utilities** (`css/style.css`, 520 lines):
  - Custom spacing: `.mt-6`, `.mb-6`, `.pt-6`, `.pb-6` (5rem each)
  - Button variants: `.btn-square`, `.btn-sm-square`, `.btn-lg-square`, etc.
  - Animations via WOW.js classes: `wow fadeIn` with `data-wow-delay`
  - Spinner state management: `.show` class toggles visibility/opacity

## JavaScript Patterns

Located in `js/main.js`. Key patterns:

- **jQuery wrapper**: All code in `(function ($) { ... })(jQuery);` IIFE
- **Spinner fade**: `setTimeout` removes spinner immediately after page load
- **Sticky navbar**: Adds `shadow-sm` class and adjusts `top` CSS on scroll > 300px
- **Owl Carousel config** (testimonials):
  - `autoplay: true`, `smartSpeed: 1000`, `loop: true`
  - Navigation arrows use Bootstrap Icons: `<i class="bi bi-arrow-left"></i>`
  - Custom nav text via `navText` array

## Naming & Conventions

- **Data attributes**: `data-wow-delay`, `data-bs-toggle`, `data-bs-target` (Bootstrap conventions)
- **CSS classes**: BEM-lite (blocks like `.btn-square`, modifiers with hyphens)
- **IDs**: Global (`#spinner`, `#navbarCollapse`), match `data-bs-target` references
- **Image paths**: Relative (`img/favicon.ico`, `img/...`)
- **External CDN**: Font Awesome, Bootstrap Icons, Google Fonts

## Common Tasks

**Adding a new page**:

1. Copy an existing `.html` page as template (preserves head/navbar)
2. Keep identical `<head>` structure
3. Update `<title>` and page-specific content in `<main>`
4. Add nav link to navbar in all existing pages

**Adding animations**:

- Use WOW.js: `<element class="wow fadeIn" data-wow-delay="0.1s">`
- Supported effects: `fadeIn`, `slideInUp`, `slideInRight`, etc. (from `lib/animate/animate.min.css`)

**Adding carousel/sliders**:

- Reference Owl Carousel (`lib/owlcarousel/`): Initialize in `main.js` with jQuery
- Include CSS: `lib/owlcarousel/assets/owl.carousel.min.css`

**Form/Contact handling**:

- Currently static HTML—no backend integration. Update `contact.html` form `action` attribute to point to server endpoint if needed.

## File Dependencies

- `js/main.js` depends on: jQuery (via Bootstrap), WOW.js, Owl Carousel (each pre-loaded in HTML)
- `css/style.css` extends Bootstrap utilities—check before redefining utility classes
- `lib/` contains all third-party assets (no npm/package manager)

## Development Workflow

No build step or tooling required. Edit files directly:

1. Modify HTML/CSS/JS
2. Save and refresh browser
3. Check responsive design on lg/md/sm breakpoints (Bootstrap responsive classes)

Responsiveness hints: `d-none d-lg-flex` (hidden on small, visible on large), `navbar-expand-lg` (collapse on lg breakpoint)
