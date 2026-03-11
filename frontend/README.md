# Recrux.AI Frontend - Modern Job Discovery UI

The Recrux.AI frontend is a sleek, highly-interactive dashboard designed to help users manage their professional identity and discover their next big role using AI.

## ✨ Features

- **Auth Portal**: Support for manual Email/Password login and **Google OAuth**.
- **Onboarding**: Integrated resume upload (PDF/DOCX) with an option to skip and search manually.
- **Jobs Section**: 
  - Personalized matching based on primary resume.
  - Manual search functionality with skill-based filters.
- **Resume Management**: Support for multiple resumes (up to 3) with a "Set as Primary" feature.
- **Rich Profile View**: Automatic breakdown of education, experience, and skills extracted by the AI backend.
- **Responsive Design**: Built with a mobile-first approach using Tailwind CSS.

---

## 🚀 Tech Stack

- **React 19**: Modern UI library.
- **Tailwind CSS 4**: For high-performance, utility-first styling.
- **Vite**: Ultra-fast build tool and dev server.
- **Lucide React**: Clean and consistent iconography.
- **Motion**: Fluid animations for a premium, alive feel.
- **TypeScript**: Ensuring type safety across the application.

---

## 🛠️ Development Setup

### Prerequisites
- Node.js 18+
- NPM or Yarn

### Installation
```bash
npm install
```

### Environment Config
Copy `.env.example` to `.env` and configure your backend URL:
```env
VITE_API_BASE_URL=http://localhost:8000/api
```

### Run Locally
```bash
npm run dev
```
The application will be available at [http://localhost:3000](http://localhost:3000).

---

## 🏗️ Project Structure

- `src/App.tsx`: Main application entry and routing logic.
- `src/main.tsx`: React DOM initialization.
- `src/index.css`: Tailwind directives and global styles.

---

## 🔗 Integration
The frontend communicates with the **FastAPI Multi-Agent Backend** to perform resume parsing and job scoring. All resume data is processed server-side to ensure the highest accuracy using Gemini 3 Flash.
