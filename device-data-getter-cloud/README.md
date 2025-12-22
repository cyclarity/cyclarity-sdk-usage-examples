# Device Data Getter (Cloud) - Demo Runnable

This runnable demonstrates how a CyClarity component can:
- Report progress to the platform while it “runs”
- Retrieve mock device data from a backend (simulated)
- Send a basic TestResult to the platform (via `platform_api.send_finding`) summarizing the retrieved data
- Return structured output data for downstream components

## What it does

- Input parameter: `device_id` (must be one of `demo-001` or `demo-002`).
- During `run()`:
  - Reports progress from 0–100%.
  - Retrieves mock constant and dynamic device data using `get_device_data(...)`.
  - Sends a basic test result (`TestResult`) with:
    - `topic`: "Device Data Getter Cloud"
    - `type`: `TestBasicResultType.PASSED`
    - `purpose`: "check that device data properly retrieved from cloud"
    - `description`: JSON of the retrieved device data
  - Returns a `DeviceData` object containing:
    - `constant`: device_id, model, firmware_version, serial_number, status
    - `dynamic`: battery_percent, temperature_c, last_sync_utc

Notes:
- All backend calls are mocked; no external network requests are made.
- This is intended for demo purposes to showcase runnable structure and platform interactions.

## File of interest

- `device_data_getter_cloud/runnable.py` — the runnable implementation.

## Running locally (demo)

```bash
cd device-data-getter-cloud
poetry install
poetry run device-data-getter-cloud
```

To choose a specific device ID, set it when constructing the runnable in code (Literal constrained to `"demo-001"` or `"demo-002"`), or pass it via your orchestration layer when integrating into a flow.

## Key SDK elements used

- `Runnable` and lifecycle methods: `setup()`, `run()`, `teardown()`
- `platform_api`:
  - `report_test_progress(percentage=...)`
  - `send_test_report_description(...)`
  - `send_finding(TestResult(...))` for basic test results
- `TestResult` with `TestBasicResultType`


