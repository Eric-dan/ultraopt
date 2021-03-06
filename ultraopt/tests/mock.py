#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : qichun tang
# @Date    : 2020-12-20
# @Contact    : tqichun@gmail.com
from ConfigSpace import ConfigurationSpace, Configuration
from hpolib.benchmarks.synthetic_functions import MultiFidelityRosenbrock2D

__all__ = ["config_space", "evaluation"]

synthetic_function_cls = MultiFidelityRosenbrock2D

config_space = ConfigurationSpace()
config_space.generate_all_continuous_from_bounds(synthetic_function_cls.get_meta_information()['bounds'])
synthetic_function = synthetic_function_cls()


# 定义目标函数
def evaluation(config: dict, budget=100):
    config = Configuration(config_space, values=config)
    return synthetic_function.objective_function(config, budget=budget)["function_value"] - \
           synthetic_function.get_meta_information()["f_opt"]
