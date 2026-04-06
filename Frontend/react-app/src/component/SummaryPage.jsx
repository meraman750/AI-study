import React, { useState } from "react";

export default function SummaryPage() {
  const [file, setFile] = useState(null);
  const [textInput, setTextInput] = useState("");
  const [subject, setSubject] = useState("");
  const [summary, setSummary] = useState("");
  const [loading, setLoading] = useState(false);

  const handleFileChange = (e) => setFile(e.target.files[0]);
  const handleTextChange = (e) => setTextInput(e.target.value);
  const handleSubjectChange = (e) => setSubject(e.target.value);

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
    setTimeout(() => {
      setSummary(
        "This is a sample AI-generated summary.\n\nOnce backend is connected, the real summary will appear here."
      );
      setLoading(false);
    }, 2000);
  };

  return (
    <div className="max-w-3xl mx-auto p-5 font-sans">
      <h1 className="text-3xl font-bold text-center mb-8">📚 AI Study Summary Generator</h1>

      {/* Upload Card */}
      <div className="bg-white p-6 rounded-xl shadow-md border border-gray-200">
        <h2 className="text-xl font-semibold mb-4">Upload Study Material</h2>

        {/* Subject Dropdown */}
        <select
          value={subject}
          onChange={handleSubjectChange}
          className="w-full p-2.5 mb-4 rounded-lg border border-gray-300"
        >
          <option value="">Select Subject</option>
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
          className="mb-3"
        />

        <p className="text-center text-gray-500 my-2.5">OR</p>

        {/* Text Input */}
        <textarea
          placeholder="Paste your study material here..."
          value={textInput}
          onChange={handleTextChange}
          className="w-full h-36 p-3 rounded-lg border border-gray-300 resize-none"
        />

        {/* Button */}
        <button
          onClick={handleGenerateSummary}
          className="mt-4 px-4 py-3 bg-indigo-500 text-white rounded-lg text-base hover:bg-indigo-600"
        >
          {loading ? "Generating Summary..." : "Generate Summary"}
        </button>
      </div>

      {/* Summary Section */}
      {summary && (
        <div className="bg-white p-6 mt-6 rounded-xl shadow-md border border-gray-200 whitespace-pre-wrap">
          <h2 className="text-xl font-semibold mb-3">🧠 AI Generated Summary</h2>
          <div>{summary}</div>
        </div>
      )}
    </div>
  );
}