import Link from "next/link";

export default function Home() {
  return (
    <div className="min-h-screen bg-gradient-to-br from-slate-900 via-slate-800 to-slate-900 text-white">
      <nav className="bg-slate-950 border-b border-slate-700 p-4">
        <div className="max-w-7xl mx-auto flex justify-between items-center">
          <h1 className="text-3xl font-bold text-blue-400">⚔️ Deck Brain</h1>
          <div className="space-x-4">
            <Link href="/deck-checker" className="hover:text-blue-400">Deck Checker</Link>
            <Link href="/player-insights" className="hover:text-blue-400">Player Insights</Link>
            <Link href="/friends" className="hover:text-blue-400">Friends</Link>
          </div>
        </div>
      </nav>
      <div className="max-w-7xl mx-auto px-4 py-20 text-center">
        <h2 className="text-5xl font-bold mb-4">Clash Royale Deck Brain</h2>
        <p className="text-xl text-slate-300 mb-12">AI-powered deck analysis & friend matchups</p>
        <div className="grid grid-cols-1 md:grid-cols-3 gap-6">
          <Link href="/deck-checker" className="bg-slate-800 hover:bg-slate-700 p-6 rounded-lg border border-blue-500">
            <h3 className="text-2xl font-bold mb-2">🔍 Deck Checker</h3>
            <p>Analyze any deck and get recommendations.</p>
          </Link>
          <Link href="/player-insights" className="bg-slate-800 hover:bg-slate-700 p-6 rounded-lg border border-purple-500">
            <h3 className="text-2xl font-bold mb-2">📊 Player Insights</h3>
            <p>Track your stats and deck performance.</p>
          </Link>
          <Link href="/friends" className="bg-slate-800 hover:bg-slate-700 p-6 rounded-lg border border-green-500">
            <h3 className="text-2xl font-bold mb-2">👥 Friends</h3>
            <p>Compare with friends and see matchups.</p>
          </Link>
        </div>
      </div>
    </div>
  );
}
