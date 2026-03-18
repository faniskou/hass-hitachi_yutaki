"""Profiles for Hitachi heat pumps."""

import logging

from .base import HitachiHeatPumpProfile
from .ycc import YccProfile
from .yutaki_m import YutakiMProfile
from .yutaki_s import YutakiSProfile
from .yutaki_s80 import YutakiS80Profile
from .yutaki_s_combi import YutakiSCombiProfile
from .yutaki_s_combi_2016_2020 import YutakiSCombi20162020Profile
from .yutaki_sc_lite import YutakiScLiteProfile
from .yutampo_r32 import YutampoR32Profile

_LOGGER = logging.getLogger(__name__)

PROFILES: dict[str, type[HitachiHeatPumpProfile]] = {
    "yutaki_s": YutakiSProfile,
    "yutaki_s_combi": YutakiSCombiProfile,
    "yutaki_s_combi_2016_2020": YutakiSCombi20162020Profile,
    "yutaki_s80": YutakiS80Profile,
    "yutaki_m": YutakiMProfile,
    "yutampo_r32": YutampoR32Profile,
    "yutaki_sc_lite": YutakiScLiteProfile,
    "ycc": YccProfile,
}
