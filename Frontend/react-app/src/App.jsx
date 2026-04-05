import React, { useState } from "react";
import './App.css'

export default function AISummaryPage() {

  const [file, setFile] = useState(null);
  const [textInput, setTextInput] = useState("");
  const [subject, setSubject] = useState("");
  const [summary, setSummary] = useState("");
  const [loading, setLoading] = useState(false);

  // Handle file selection
  const handleFileChange = (e) => {
    setFile(e.target.files[0]);
  };

  // Handle text input
  const handleTextChange = (e) => {
    setTextInput(e.target.value);
  };

  // Handle subject change
  const handleSubjectChange = (e) => {
    setSubject(e.target.value);
  };

  // Handle Generate Summary (frontend only)
  const handleGenerateSummary = () => {

    if (!file && !textInput) {
      alert("Please upload a file or enter text.");
      return;
    }

    if (!subject) {
      alert("Please select a subject.");
      return;
    }

    setLoading(true);

    // Simulated summary response (for frontend testing)
    setTimeout(() => {

      setSummary(
        "This is a sample AI-generated summary.\n\n" +
        "Once backend is connected, the real summary will appear here."
      );

      setLoading(false);

    }, 2000);
  };

  return (
    <div className="container">

      <h1 className="title">
        📚 AI Study Summary Generator
      </h1>

      {/* Upload Card */}
      <div className="card">

        <h2>Upload Study Material</h2>

        {/* Subject Dropdown */}
        <select
          value={subject}
          onChange={handleSubjectChange}
          className="dropdown"
        >
          <option value="">
            Select Subject
          </option>

          <option>Mathematics</option>
          <option>Computer Science</option>
          <option>Database Systems</option>
          <option>Programming</option>
          <option>Networking</option>

        </select>

        {/* File Upload */}
        <input
          type="file"
          accept=".pdf,.txt,.docx"
          onChange={handleFileChange}
          className="fileInput"
        />

        <p className="orText">OR</p>

        {/* Text Input */}
        <textarea
          placeholder="Paste your study material here..."
          value={textInput}
          onChange={handleTextChange}
          className="textarea"
        />

        {/* Button */}
        <button
          onClick={handleGenerateSummary}
          className="button"
        >

          {loading
            ? "Generating Summary..."
            : "Generate Summary"}

        </button>

      </div>

      {/* Summary Section */}
      {summary && (

        <div className="card">

          <h2>
            🧠 AI Generated Summary
          </h2>

          <div className="summaryBox">
            {summary}
          </div>

        </div>

      )}

    </div>
  );
}
