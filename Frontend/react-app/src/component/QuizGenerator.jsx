import React, { useState } from "react";

export default function QuizGenerator() {

  const [topic, setTopic] = useState("");
  const [quiz, setQuiz] = useState("");
  const [loading, setLoading] = useState(false);

  const generateQuiz = () => {

    if (!topic) {
      alert("Enter a topic.");
      return;
    }

    setLoading(true);

    // Simulated AI Quiz
    setTimeout(() => {

      setQuiz(
        "📝 Sample Quiz\n\n" +

        "1. What is a database?\n" +
        "A) Collection of data\n" +
        "B) Programming language\n" +
        "C) Hardware\n\n" +

        "2. What does SQL stand for?\n" +
        "A) Structured Query Language\n" +
        "B) Simple Query List\n" +
        "C) System Query Logic"
      );

      setLoading(false);

    }, 2000);

  };

  return (

    <div className="min-h-screen bg-gray-100 p-6">

      <h1 className="text-3xl font-bold text-indigo-600 mb-6">
        🧠 AI Quiz Generator
      </h1>

      {/* Input Card */}
      <div className="bg-white p-6 rounded-2xl shadow mb-6">

        <input
          type="text"
          placeholder="Enter topic (e.g., Database Systems)"
          value={topic}
          onChange={(e) =>
            setTopic(e.target.value)
          }
          className="w-full border p-3 rounded-lg mb-4"
        />

        <button
          onClick={generateQuiz}
          className="w-full bg-indigo-600 text-white p-3 rounded-lg hover:bg-indigo-700"
        >

          {loading
            ? "Generating Quiz..."
            : "Generate Quiz"}

        </button>

      </div>

      {/* Quiz Output */}
      {quiz && (

        <div className="bg-white p-6 rounded-2xl shadow">

          <h2 className="text-xl font-semibold mb-4">
            📋 Generated Quiz
          </h2>

          <div className="bg-gray-100 p-4 rounded-lg whitespace-pre-line">

            {quiz}

          </div>

        </div>

      )}

    </div>

  );
}