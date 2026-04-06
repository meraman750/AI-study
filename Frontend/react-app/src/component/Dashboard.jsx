import React from "react";
import ProgressCard from "./ProgressCard";

export default function Dashboard() {
  const progressData = [
    { subject: "Mathematics", completed: 70 },
    { subject: "Computer Science", completed: 40 },
    { subject: "Database Systems", completed: 90 },
  ];

  return (
    <div className="p-5 max-w-4xl mx-auto">
      <h1 className="text-2xl font-bold mb-5 text-center">📊 Progress Dashboard</h1>

      <div className="grid md:grid-cols-3 gap-5">
        {progressData.map((item, index) => (
          <ProgressCard key={index} subject={item.subject} completed={item.completed} />
        ))}
      </div>
    </div>
  );
}