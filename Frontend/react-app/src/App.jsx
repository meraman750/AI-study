import React from "react";
import { BrowserRouter as Router, Routes, Route, Link } from "react-router-dom";

// Components
import Login from "./component/Login";
import ProgressCard from "./component/ProgressCard";
import SummaryPage from "./component/SummaryPage";
import QuizGenerator from "./component/QuizGenerator";
import Dashboard from "./component/Dashboard";

export default function App() {
  return (
    <Router>
      {/* Navigation */}
      <nav className="bg-green-500 p-4 text-gray-200 flex justify-center space-x-6">
        <Link to="/login" className="hover:text-white">Login</Link>
        <Link to="/dashboard" className="hover:text-white">Dashboard</Link>
        <Link to="/summary" className="hover:text-white">AI Summary</Link>
        <Link to="/quiz" className="hover:text-white">Quiz Generator</Link>
      </nav>

      {/* Routes */}
      <Routes>
        {/* Pair 1 */}
        <Route path="/login" element={<Login />} />
        <Route path="/quiz" element={<QuizGenerator />} />

        {/* Pair 2 */}
        <Route path="/dashboard" element={<Dashboard />} />

        {/* Pair 3 */}
        <Route path="/summary" element={<SummaryPage />} />

        {/* Default route */}
        <Route path="*" element={<Dashboard />} />
      </Routes>
    </Router>
  );
}
