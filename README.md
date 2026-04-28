# Observability & SRE Demo Stack

This project demonstrates a full-stack observability solution using Prometheus, Grafana, and the Blackbox Exporter. It was built to showcase PromQL mastery and automated monitoring strategies.

## Architecture
- **Mock App:** A Python service generating HTTP traffic, errors, and latency metrics.
- **Blackbox Exporter:** Monitoring external connectivity for key domains (Google, Coralogix, etc.).
- **Prometheus:** Aggregating metrics and calculating P95 latencies and error rates.
- **Grafana:** Visualizing the "Golden Signals" of service health.

## Key PromQL Queries Used
- **P95 Latency:** `histogram_quantile(0.95, sum by (le, endpoint) (rate(http_request_duration_seconds_bucket[5m])))`
- **Error Rate %:** `sum(rate(http_requests_total{status="500"}[5m])) / sum(rate(http_requests_total[5m])) * 100`

## How to Run
1. Ensure Docker is installed.
2. Run `docker-compose up -d`.
3. Access Grafana at `http://localhost:3000` (admin/admin).
