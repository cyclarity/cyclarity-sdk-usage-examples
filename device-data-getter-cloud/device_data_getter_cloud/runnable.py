from cyclarity_sdk.expert_builder import Runnable, BaseResultsModel
from pydantic import BaseModel, Field
from typing import Literal
import json
import time
from cyclarity_sdk.sdk_models.findings import TestResult
from cyclarity_sdk.sdk_models.findings.types import (
    TestBasicResultType
)


class DeviceData(BaseModel):
    device_id: str = ""
    device_model: str = ""
    firmware_version: str = ""
    serial_number: str = ""
    status: str = ""


class DeviceDataGetterResult(BaseModel):
    device_data: DeviceData


class DeviceDataGetterCloud(Runnable[DeviceDataGetterResult]):
    # A single device ID that can be one of: "demo-001" or "demo-002"
    device_id: Literal["demo-001", "demo-002"] = Field(
        default="demo-001",
        description="Device ID to retrieve",
    )

    def get_device_data_from_backend_using_api(self, device_id):
        # Mocked logic to simulate retrieving HW data from a cloud API
        # In a real implementation this would call an external api.

        if device_id == "demo-001":
            constant_data_mock = {
                "device_id": device_id,
                "device_model": "Model-X",
                "firmware_version": "1.2.3",
                "serial_number": "SN123456",
                "status": "online",
            }
        elif device_id == "demo-002":
            constant_data_mock = {
                "device_id": device_id,
                "device_model": "Model-Y",
                "firmware_version": "2.0.1",
                "serial_number": "SN987654",
                "status": "online",
            }
        else:
            constant_data_mock = {}

        return constant_data_mock

    def get_device_data(self, device_id: str):
        # Mocked logic to simulate retrieving HW data from a cloud API
        # In a real implementation this would call an external service.
        return self.get_device_data_from_backend_using_api(device_id)  # noqa

    def setup(self):
        self.logger.info("SETUP before running")
        self.platform_api.send_test_report_description(
            "Demo logic for getting HW data stored in cloud"
        )

    def run(self, *args, **kwargs):
        self.logger.info("RUNNING")
        self.platform_api.report_test_progress(percentage=30)
        device_data = self.get_device_data(self.device_id)
        # Send a basic TestResult with PASSED status and full description
        desc_data = json.dumps(
            device_data, sort_keys=True, indent=2, separators=(',', ': '))

        self.platform_api.send_finding(
            TestResult(
                test_name="hw_data_getter",
                topic="Device Data Getter Cloud",
                type=TestBasicResultType.PASSED,
                purpose=("check that device data properly retrieved from cloud"),  # noqa
                description=(
                    f"Retrieved Device data from cloud: {desc_data}"
                ),
            )
        )
        return DeviceDataGetterResult(device_data=DeviceData(**device_data))

    def teardown(
        self,
        exception_type=None,
        exception_value=None,
        traceback=None,
    ):
        self.logger.info("TEARDOWN after run function")


def main():
    # Local demo of the runnable with mock data
    with DeviceDataGetterCloud() as runnable_instance:
        result: DeviceDataGetterResult = runnable_instance()
        print(result)


if __name__ == '__main__':
    main()
