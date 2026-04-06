import React from "react";

export default function ProgressCard({ subject, completed }) {
  return (
    <div className="bg-white p-5 rounded-xl shadow-sm border border-gray-200">
      <h2 className="text-lg font-semibold mb-3">{subject}</h2>
      <div className="w-full bg-gray-200 rounded-full h-4">
        <div
          className="bg-indigo-500 h-4 rounded-full"
          style={{ width: `${completed}%` }}
        />
      </div>
      <p className="text-sm mt-2">{completed}% completed</p>
    </div>
  );
}