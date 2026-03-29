## Frontend Folder Structure

frontend/
├── public/
│   ├── index.html            # Main HTML file
│   └── ...                   # Other public assets (images, favicon, etc.)
│
├── src/
│   ├── components/           # Reusable React components
│   ├── pages/                # Page-level components (e.g., Dashboard, Login)
│   ├── services/             # API calls using Axios
│   ├── App.js                # Main React component
│   └── index.js              # React entry point
│
├── package.json              # Frontend dependencies and scripts
└── node_modules/             # Installed dependencies (generated after npm install)