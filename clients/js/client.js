async function run() {
  const url = "http://127.0.0.1:8000/predict";
  const res = await fetch(url, {
    method: "POST",
    headers: { "content-type": "application/json" },
    body: JSON.stringify({ features: [5.1, 3.5, 1.4, 0.2] }),
  });
  const data = await res.json();
  console.log("Response:", data);
}
run();
