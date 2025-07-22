import http from 'k6/http';
import { sleep } from 'k6';
export let options = { vus: 10, duration: '30s' };
export default function () {
  const url = 'http://localhost:8000/predict';
  const payload = JSON.stringify({ features: [5.1, 3.5, 1.4, 0.2] });
  const params = { headers: { 'Content-Type': 'application/json' } };
  http.post(url, payload, params);
  sleep(1);
}


export default function () {
  const url = 'http://localhost:8000/predict';
  const payload = JSON.stringify({ features: [5.1, 3.5, 1.4, 0.2] });
  const params = { headers: { 'Content-Type': 'application/json' } };
  http.post(url, payload, params);
  sleep(1);
}
