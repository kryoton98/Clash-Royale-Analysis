"use client";

import React, { useState, ChangeEvent } from "react";

export default function DeckChecker() {
  const [selectedCards, setSelectedCards] = useState<string[]>([]);
  const [trophyRange, setTrophyRange] = useState("5000-6000");
  const [result, setResult] = useState<{ predicted_win_rate: number } | null>(
    null
  );

  const handleTrophyChange = (e: ChangeEvent<HTMLSelectElement>) => {
    setTrophyRange(e.target.value);
  };

  const handleEvaluate = async () => {
    if (selectedCards.length !== 8) {
      alert("Select 8 cards");
      return;
    }
    setResult({ predicted_win_rate: 0.55 });
  };

  return (
    <div className="min-h-screen bg-gradient-to-br from-slate-900 to-slate-800 text-white p-8">
      <h1 className="text-4xl font-bold mb-8">Deck Checker</h1>
      <div className="max-w-4xl mx-auto grid grid-cols-1 lg:grid-cols-2 gap-8">
        <div className="bg-slate-800 p-6 rounded-lg">
          <h2 className="text-2xl font-bold mb-4">Select 8 Cards</h2>

          {/* Accessible label for the select */}
          <label
            htmlFor="trophyRange"
            className="block mb-2 text-sm font-medium text-slate-200"
          >
            Trophy range
          </label>
          <select
            id="trophyRange"
            value={trophyRange}
            onChange={handleTrophyChange}
            className="w-full bg-slate-700 p-2 rounded mb-4"
          >
            <option>4000-5000</option>
            <option>5000-6000</option>
            <option>6000+</option>
          </select>

          <button
            onClick={handleEvaluate}
            className="w-full bg-blue-600 hover:bg-blue-700 p-3 rounded font-bold"
          >
            Evaluate Deck
          </button>
        </div>

        <div className="bg-slate-800 p-6 rounded-lg">
          {result && (
            <p className="text-lg">
              Win Rate:{" "}
              <span className="text-green-400">
                {(result.predicted_win_rate * 100).toFixed(1)}%
              </span>
            </p>
          )}
        </div>
      </div>
    </div>
  );
}
