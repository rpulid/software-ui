"""
Read-only parameters from the MCU
"""
import json
from typing import Union


class Params():
    """
    Params defined in serialpacketv0.26.pptx
    """
    def __init__(self) -> None:
        self._param: dict = {
            "seq_num": 0,
            "packet_version": 0,
            "mode": 0,
            "resp_rate_meas": 0,
            "resp_rate_set": 0,
            "tv_meas": 0,
            "tv_set": 0,
            "ie_ratio_meas": 0,
            "ie_ratio_set": 0,
            "peep": 0,
            "ppeak": 0,
            "pplat": 0,
            "pressure": 0,
            "flow": 0,
            "tv_insp": 0,
            "tv_exp": 0,
            "tv_min": 0,
            "control_state": 0,
            "run_state": 0,
            "battery_level": 0,
        }
        #TODO: handle alarms

    @property
    def seq_num(self) -> int:
        """ Sequence Number """
        return self._param["seq_num"]

    @seq_num.setter
    def seq_num(self, value: int) -> None:
        self._param["seq_num"] = value

    @property
    def packet_version(self) -> int:
        return self._param["packet_version"]

    @packet_version.setter
    def packet_version(self, value: int) -> None:
        self._param["packet_version"] = value

    @property
    def mode(self) -> int:
        return self._param["mode"]

    @mode.setter
    def mode(self, value: int) -> None:
        self._param["mode"] = value

    @property
    def resp_rate_meas(self) -> int:
        return self._param["resp_rate_meas"]

    @resp_rate_meas.setter
    def resp_rate_meas(self, value: int) -> None:
        self._param["resp_rate_meas"] = value

    @property
    def resp_rate_set(self) -> int:
        return self._param["resp_rate_set"]

    @resp_rate_set.setter
    def resp_rate_set(self, value: int) -> None:
        self._param["resp_rate_set"] = value

    @property
    def tv_meas(self) -> int:
        return self._param["tv_meas"]

    @tv_meas.setter
    def tv_meas(self, value: int) -> None:
        self._param["tv_meas"] = value

    @property
    def tv_set(self) -> int:
        return self._param["tv_set"]

    @tv_set.setter
    def tv_set(self, value: int) -> None:
        self._param["tv_set"] = value

    @property
    def ie_ratio_meas(self) -> int:
        return self._param["ie_ratio_meas"]

    @ie_ratio_meas.setter
    def ie_ratio_meas(self, value: int) -> None:
        self._param["ie_ratio_meas"] = value

    @property
    def ie_ratio_set(self) -> int:
        return self._param["ie_ratio_set"]

    @ie_ratio_set.setter
    def ie_ratio_set(self, value: int) -> None:
        self._param["ie_ratio_set"] = value

    @property
    def peep(self) -> int:
        return self._param["peep"]

    @peep.setter
    def peep(self, value: int) -> None:
        self._param["peep"] = value

    @property
    def ppeak(self) -> int:
        return self._param["ppeak"]

    @ppeak.setter
    def ppeak(self, value: int) -> None:
        self._param["ppeak"] = value

    @property
    def pplat(self) -> Union[int, float]:
        return self._param["pplat"]

    @pplat.setter
    def pplat(self, value: Union[int, float]) -> None:
        self._param["pplat"] = value

    @property
    def pressure(self) -> Union[int, float]:
        return self._param["pressure"]

    @pressure.setter
    def pressure(self, value: Union[int, float]) -> None:
        self._param["pressure"] = value

    @property
    def flow(self) -> Union[int, float]:
        return self._param["flow"]

    @flow.setter
    def flow(self, value: Union[int, float]) -> None:
        self._param["flow"] = value

    @property
    def tv_insp(self) -> int:
        return self._param["tv_insp"]

    @tv_insp.setter
    def tv_insp(self, value: int) -> None:
        self._param["tv_insp"] = value

    @property
    def tv_exp(self) -> int:
        return self._param["tv_exp"]

    @tv_exp.setter
    def tv_exp(self, value: int) -> None:
        self._param["tv_exp"] = value

    @property
    def tv_min(self) -> int:
        return self._param["tv_min"]

    @tv_min.setter
    def tv_min(self, value: int) -> None:
        self._param["tv_min"] = value

    @property
    def control_state(self) -> int:
        return self._param["control_state"]

    @control_state.setter
    def control_state(self, value: int) -> None:
        self._param["control_state"] = value

    @property
    def run_state(self) -> int:
        return self._param["run_state"]

    @run_state.setter
    def run_state(self, value: int) -> None:
        self._param["run_state"] = value

    @property
    def battery_level(self) -> int:
        return self._param["battery_level"]

    @battery_level.setter
    def battery_level(self, value: int) -> None:
        self._param["battery_level"] = value

    def to_JSON(self) -> str:
        """ Convert OVVE UI Params to JSON file """
        return json.dumps(self._param)

    def from_dict(self, input_dict: dict) -> None:
        """ Set OVVE UI params from input dictionary """
        for key in input_dict:
            # Check if key from input_dict exists in ours
            if key in self._param:
                self._param[key] = input_dict[key]

    def from_JSON(self, j_str: str) -> None:
        j = json.loads(j_str)
        self.from_dict(j)
