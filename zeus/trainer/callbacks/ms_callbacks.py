# -*- coding:utf-8 -*-

# Copyright (C) 2020. Huawei Technologies Co., Ltd. All rights reserved.
# This program is free software; you can redistribute it and/or modify
# it under the terms of the MIT License.
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# MIT License for more details.

"""Custom callbacks used in mindspore."""

import logging
from mindspore.train.callback import Callback


class EvalCallBack(Callback):
    """
    Monitor the metric in training.

    :param model: the mindspore model
    :type model: Class of mindspore.train.Model
    :param eval_dataset: valid dataloader
    :type eval_dataset: MindDataset
    """

    def __init__(self, model, eval_dataset):
        super(EvalCallBack, self).__init__()
        self.model = model
        self.eval_dataset = eval_dataset

    def epoch_end(self, run_context):
        """Be called after each epoch."""
        cb_params = run_context.original_args()
        metric = self.model.eval(self.eval_dataset, dataset_sink_mode=False)
        logging.info(
            "Current epoch : [{}/{}], current valid metric {}.".format(cb_params.cur_epoch_num, cb_params.epoch_num,
                                                                       metric))
