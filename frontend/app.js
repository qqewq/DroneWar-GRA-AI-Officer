const BASE = 'http://localhost:8000';
let chart;

async function startMission() {
  const jamming = document.getElementById('jamming').value;
  await fetch(`${BASE}/mission/start?drones=20&jamming=${jamming}`, {method: 'POST'});
  setInterval(updateMetrics, 500);
}

async function updateMetrics() {
  const resp = await fetch(`${BASE}/state`);
  const state = await resp.json();
  document.getElementById('resonance').textContent = state.overall_resonance.toFixed(3);
  document.getElementById('nullification').textContent = state.nullification_level.toFixed(3);
  document.getElementById('stability').textContent = state.hierarchy_stability.toFixed(3);
  if (!chart) {
    const ctx = document.getElementById('resonanceChart').getContext('2d');
    chart = new Chart(ctx, {
      type: 'line',
      data: {
        labels: [],
        datasets: [{
          label: 'Overall Resonance',
          data: [],
          borderColor: 'rgb(75, 192, 192)',
          tension: 0.1
        }]
      },
      options: {
        scales: {
          y: { beginAtZero: true, max: 1 }
        }
      }
    });
  }
  chart.data.labels.push(new Date().toLocaleTimeString());
  chart.data.datasets[0].data.push(state.overall_resonance);
  if (chart.data.labels.length > 20) {
    chart.data.labels.shift();
    chart.data.datasets[0].data.shift();
  }
  chart.update();
}

document.getElementById('jamming').oninput = (e) => {
  document.getElementById('jam-label').textContent = 'Помехи: ' + e.target.value;
};
