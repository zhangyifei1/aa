#!/usr/bin/python3.6
# -*- coding: utf-8 -*-
# @Time    : 2021/10/22 9:34
# @Author  : zhangyifei
# @File    :   cnn.py

import paddle

def convolutional_neural_network():
    img = paddle.fluid.layers.data(name='pixel',type=paddle.fluid.data_type)
