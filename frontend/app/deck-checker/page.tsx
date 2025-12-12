"use client";

import { useMemo, useState } from "react";

type DeckEvaluateResponse = {
  win_probability: number;
  features: Record<string, number>;
};

const API_BASE =
  process.env.NEXT_PUBLIC_API_BASE_URL?.trim() || "http://127.0.0.1:8000";

export default function DeckCheckerPage() {
  const [avgElixir, setAvgElixir] = useState<string>("3.2");
  const [oppAvgElixir, setOppAvgElixir] = useState<string>("4.0");

  const [loading, setLoading] = useState(false);
  const [error, setError] = useState<string | null>(null);
  const [result, setResult] = useState<DeckEvaluateResponse | null>(null);

  const canSubmit = useMemo(() => {
    const a = Number(avgElixir);
    const b = Number(oppAvgElixir);
    return Number.isFinite(a) && Number.isFinite(b);
  }, [avgElixir, oppAvgElixir]);

  async function onEvaluate() {
    setLoading(true);
    setError(null);
    setResult(null);

    try {
      const payload = {
        avg_elixir: Number(avgElixir),
        opponent_avg_elixir: Number(oppAvgElixir),
      };

      const res = await fetch(`${API_BASE}/api/deck/evaluate`, {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
          Accept: "application/json",
        },
        body: JSON.stringify(payload),
      });

      if (!res.ok) {
        const text = await res.text();
        throw new Error(`Backend error ${res.status}: ${text}`);
      }

      const data = (await res.json()) as DeckEvaluateResponse;
      setResult(data);
    } catch (e: any) {
      setError(e?.message ?? "Unknown error");
    } finally {
      setLoading(false);
    }
  }

  const winPct =
    result ? `${(result.win_probability * 100).toFixed(2)}%` : null;

  return (
    <div className="max-w-3xl mx-auto px-4 py-10 text-white">
      <h1 className="text-3xl font-bold mb-6">Deck Checker</h1>

      <div className="bg-slate-900 border border-slate-700 rounded-lg p-6 space-y-4">
        <div className="grid grid-cols-1 md:grid-cols-2 gap-4">
          <label className="space-y-1">
            <div className="text-sm text-slate-300">Your avg elixir</div>
            <input
              className="w-full bg-slate-800 border border-slate-600 rounded px-3 py-2"
              value={avgElixir}
              onChange={(e) => setAvgElixir(e.target.value)}
              placeholder="e.g. 3.2"
            />
          </label>

          <label className="space-y-1">
            <div className="text-sm text-slate-300">Opponent avg elixir</div>
            <input
              className="w-full bg-slate-800 border border-slate-600 rounded px-3 py-2"
              value={oppAvgElixir}
              onChange={(e) => setOppAvgElixir(e.target.value)}
              placeholder="e.g. 4.0"
            />
          </label>
        </div>

        <button
          className="bg-blue-600 hover:bg-blue-500 disabled:bg-slate-700 disabled:cursor-not-allowed px-4 py-2 rounded"
          onClick={onEvaluate}
          disabled={!canSubmit || loading}
        >
          {loading ? "Evaluating..." : "Evaluate"}
        </button>

        {error && (
          <div className="text-red-300 bg-red-950/40 border border-red-800 rounded p-3">
            {error}
          </div>
        )}

        {result && (
          <div className="bg-slate-800 border border-slate-600 rounded p-4 space-y-2">
            <div className="text-lg">
              Win probability: <span className="font-semibold">{winPct}</span>
            </div>

            <div className="text-sm text-slate-300">Features sent to model:</div>
            <pre className="text-sm bg-slate-950 border border-slate-700 rounded p-3 overflow-auto">
              {JSON.stringify(result.features, null, 2)}
            </pre>
          </div>
        )}

        <div className="text-xs text-slate-400">
          Backend: {API_BASE}
        </div>
      </div>
    </div>
  );
}