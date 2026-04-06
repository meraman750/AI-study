import React from "react";
import "./Dashboard.css";

export default function Dashboard() {

  const progress = [
    { subject: "Mathematics", percent: 70 },
    { subject: "Programming", percent: 50 },
    { subject: "Database", percent: 80 },
    { subject: "Networking", percent: 40 }
  ];

  return (
    <div className="dashboard-container">

      <h1 className="dashboard-title">📊 Progress Dashboard</h1>

      <div className="dashboard-grid">

        {progress.map((item, index) => (

          <div key={index} className="dashboard-card">

            <h3>{item.subject}</h3>

            <div className="progress-bar">
              <div
                className="progress-fill"
                style={{ width: item.percent + "%" }}
              ></div>
            </div>

            <p>{item.percent}% Completed</p>

          </div>

        ))}

      </div>

    </div>
  );
}
