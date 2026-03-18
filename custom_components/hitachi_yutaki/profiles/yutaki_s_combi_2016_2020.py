"""Profile for the Hitachi Yutaki S Combi 2016-2020 heat pump."""

from typing import Any

from .yutaki_s_combi import YutakiSCombiProfile


class YutakiSCombi20162020Profile(YutakiSCombiProfile):
    """Profile for the Hitachi Yutaki S Combi 2016-2020 heat pump."""

    @staticmethod
    def detect(data: dict[str, Any]) -> bool:
        """Return True if the profile is detected."""
        return data.get("unit_model") == "yutaki_s_combi_2016_2020"

    @property
    def name(self) -> str:
        """Return the human-readable name of the heat pump model."""
        return "Yutaki S Combi 2016-2020"

    def get_registers(self) -> list[dict[str, Any]]:
        """Return the list of registers for the heat pump."""
        registers = super().get_registers()
        overrides = {
            "dhw_target_temperature": 1066,
            "dhw_tank_temperature": 1075,
            "unit_status": 1077,
            "outdoor_temperature": 1078,
            "water_inlet_temperature": 1079,
            "water_outlet_temperature_circuit1": 1080,
            "circuit1_target_temperature": 1086,
            "circuit1_room_temperature": 1088,
        }
        for register in registers:
            if register["name"] in overrides:
                register["address"] = overrides[register["name"]]
        return registers
