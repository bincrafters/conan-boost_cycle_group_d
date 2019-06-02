#!/usr/bin/env python
# -*- coding: utf-8 -*-

from conans import python_requires, tools


base = python_requires("boost_base/2.0.0@bincrafters/testing")


class BoostCycleGroupDConan(base.BoostBaseConan):
    name = "boost_cycle_group_d"
    version = "1.70.0"
