# -*- coding: utf-8 -*-
# Copyright (c) 2018-2021, earthobservations developers.
# Distributed under the MIT License. See LICENSE for more info.
from wetterdienst.dwd.observations.metadata import (
    DwdObservationParameter,
    DwdObservationParameterSet,
)
from wetterdienst.dwd.observations.metadata.parameter import (
    DwdObservationParameterSetStructure,
)
from wetterdienst.dwd.observations.util.parameter import (
    check_dwd_observations_parameter_set,
    create_parameter_to_parameter_set_combination,
)
from wetterdienst.metadata.period import Period
from wetterdienst.metadata.resolution import Resolution


def test_create_parameter_to_parameter_set_combination():
    par_to_par_set_combination = create_parameter_to_parameter_set_combination(
        parameter=DwdObservationParameter.MINUTE_10.PRECIPITATION_HEIGHT,
        resolution=Resolution.MINUTE_10,
    )

    assert par_to_par_set_combination == (
        DwdObservationParameterSetStructure.MINUTE_10.PRECIPITATION.PRECIPITATION_HEIGHT,
        DwdObservationParameterSet.PRECIPITATION,
    )

    par_to_par_set_combination = create_parameter_to_parameter_set_combination(
        parameter=DwdObservationParameterSetStructure.MINUTE_10.PRECIPITATION.PRECIPITATION_HEIGHT,
        resolution=Resolution.MINUTE_10,
    )

    assert par_to_par_set_combination == (
        DwdObservationParameterSetStructure.MINUTE_10.PRECIPITATION.PRECIPITATION_HEIGHT,
        DwdObservationParameterSet.PRECIPITATION,
    )

    par_to_par_set_combination = create_parameter_to_parameter_set_combination(
        parameter=DwdObservationParameterSet.PRECIPITATION,
        resolution=Resolution.MINUTE_10,
    )

    assert par_to_par_set_combination == (
        DwdObservationParameterSet.PRECIPITATION,
        DwdObservationParameterSet.PRECIPITATION,
    )


def test_check_parameters():
    assert check_dwd_observations_parameter_set(
        DwdObservationParameterSet.PRECIPITATION,
        Resolution.MINUTE_10,
        Period.HISTORICAL,
    )
    assert not check_dwd_observations_parameter_set(
        DwdObservationParameterSet.CLIMATE_SUMMARY,
        Resolution.MINUTE_1,
        Period.HISTORICAL,
    )
