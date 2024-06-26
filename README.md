# Calculator Microservice

[![Build and Publish Container Images](https://github.com/MaxAnderson95/calculator-microservice/actions/workflows/build.yaml/badge.svg)](https://github.com/MaxAnderson95/calculator-microservice/actions/workflows/build.yaml)

A distributed calculator service written in Python.

<img src="./assets/ui.gif" alt="Main UI screen" width="400px" />

## Services

| Service  | Purpose                                          | Notes                                                                                                                                         |
| -------- | ------------------------------------------------ | --------------------------------------------------------------------------------------------------------------------------------------------- |
| frontend | Frontend UI written in HTMX + business logic API | Calls the other services for calculation services.                                                                                            |
| add      | Addition services                                |                                                                                                                                               |
| subtract | Subtraction services                             | Calls the add service with the 2nd number as a negative.                                                                                       |
| multiply | Multiplication services                          |                                                                                                                                               |
| divide   | Division services                                |                                                                                                                                               |
| redis    | Caching                                          | Caches already computed computations. Each math service introduces an artifical delay of 2 seconds so the speed from caching can be observed. |
| postgres | Request logging                                  | Logs all sucessful computation requests. Optional. If not specified, a local SQLite DB is used.                                               |
| jager    | Distributed Tracing                              | A service which collects and allows the viewing of distributed trace data.                                                                     |

## Architecture Diagram

<img src="./assets/diagram.png" alt="Service Diagram" width="900px"/>

## Run locally

To run locally, the easiest way is Docker compose. Simply run:

```
docker-compose up
```

You can then access:

- The frontend of the service at `http://localhost:8000`
- The Jager instance to view traces at `http://localhost:16686`
- The pgweb instance to view the Postgres database at `http://localhost:8081`
- The Redis Commander instance to view the Redis cache at `http://localhost:8081`

## Todo List

- [x] Build a basic two tier service architecture

- [x] Build a frontend web UI

- [x] Add Redis caching to the frontend to cache recently computed calculations. Add delays to all calls by default to see the difference on a cache hit.

- [x] Add a Postgres database to store a log of all calculation queries.

- [x] Instrument each service with OpenTelemetry to allow for exporting of trace data.

- [ ] Add Prometheus (OpenMetrics) endpoints to export various metrics for each service.

- [ ] Add a "chaos" switch which enables purposeful bugs, errors, and delays in various functions.

- [ ] Add an artifical load-generator service that sends calls to the frontend to simulate usage while monitoring metrics and traces.
