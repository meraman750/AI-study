import React, { useState } from "react";

export default function Login() {

  const [email, setEmail] = useState("");
  const [password, setPassword] = useState("");

  const handleLogin = () => {

    if (!email || !password) {
      alert("Please enter email and password.");
      return;
    }

    // Simulated login
    alert("Login successful (frontend demo)");

  };

  return (

    <div className="min-h-screen flex items-center justify-center bg-gray-100">

      <div className="bg-white p-8 rounded-2xl shadow w-full max-w-md">

        <h1 className="text-2xl font-bold text-indigo-600 mb-6 text-center">
          🔐 Login
        </h1>

        {/* Email */}
        <input
          type="email"
          placeholder="Email"
          value={email}
          onChange={(e) =>
            setEmail(e.target.value)
          }
          className="w-full border p-3 rounded-lg mb-4"
        />

        {/* Password */}
        <input
          type="password"
          placeholder="Password"
          value={password}
          onChange={(e) =>
            setPassword(e.target.value)
          }
          className="w-full border p-3 rounded-lg mb-6"
        />

        {/* Login Button */}
        <button
          onClick={handleLogin}
          className="w-full bg-indigo-600 text-white p-3 rounded-lg hover:bg-indigo-700"
        >
          Login
        </button>

      </div>

    </div>

  );
}