const API_URL = process.env.NEXT_PUBLIC_API_URL || "http://localhost:8000";

export async function evaluateDeck(cardIds: string[], trophyRange: string) {
  const response = await fetch(`${API_URL}/api/deck/evaluate`, {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({ card_ids: cardIds, trophy_range: trophyRange }),
  });
  return response.json();
}
