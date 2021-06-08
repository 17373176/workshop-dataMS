# encoding=utf-8

# -----------------------------------------------------------------
# File Name:        defineConst.py
# Description:      相关常量、列表、字典的定义
# Date:             2021/4/16
# License:          (C)Copyright 2021, Bob
# Function List:
#
#
# -----------------------------------------------------------------


import os


"""默认状态，机器关节信息，托盘工件位姿信息"""
DEFAULT_STATUS = {
    '2': {"J1": "0", "J2": "0", "J3": "0", "J4": "0"},
    '7': {"X": "0", "Y": "0", "Angle": "0"},
    '8': {"X": "0", "Y": "0", "Angle": "0"},
    '16': {"J1": "0", "J2": "0", "J3": "0", "J4": "0"},
}

MACHINE_STATUS = {
}



# id对应的no字段
ID_TO_NO = {
    '1': 1, '1_1': 1, '1_2': 1, '1_3': 1, '1_4': 1, '1_5': 1, '1_6': 1,
    '2': 1, '3': 1, '4': 1, '5': 1, '6': 1, '7': 1, '8': 1, '9': 1, '10': 1,

    '11': 2, '12': 2, '12_1': 2, '12_2': 2, '12_3': 2, '13': 2, '14': 2, '15': 2, '16': 2, '17': 2,

    '21_1': 3, '21_2': 3,'21_3': 3,'21_4': 3,'21_5': 3,'21_6': 3,'21_7': 3,'21_8': 3,'21_9': 3,'21_10': 3,
    '21_11': 3,'21_12': 3,
    '22_1': 3, '22_2': 3,'22_3': 3,'22_4': 3,'22_5': 3,'22_6': 3,'22_7': 3,'22_8': 3,'22_9': 3,'22_10': 3,
    '22_11': 3,'22_12': 3,

    '31': 4, '32': 4, '33': 4, '34': 4, '35': 4, '36': 4, '37': 4, '38': 4, '39': 4
}

# id对应的name字段
MACHINE_ID_NAME = {
    "1": "传感器状态",
    "1_1": "托盘一退料到位",
    "1_2": "托盘一进料到位",
    "1_3": "托盘二退料到位",
    "1_4": "托盘二进料到位",
    "1_5": "传送带暂停",
    "1_6": "传送带状态",
    "2": "机器人关节信息",
    "3": "一号托盘累计抓取数量",
    "4": "二号托盘累计抓取数量",
    "5": "托盘一工件数量",
    "6": "托盘二工件数量",
    "7": "托盘一工件位姿信息",
    "8": "托盘二工件位姿信息",
    "9": "工位一电流",
    "10": "工位一扭力",

    "11": "工件当前编号",
    "12": "合格/残次形式",
    "12_1": "合格/残次形式",
    "12_2": "合格/残次形式",
    "12_3": "合格/残次形式",
    "12_4": "合格/残次形式",
    "13": "过检数",
    "14": "良品数量",
    "15": "不良品数量",
    "16": "机器人关节信息",
    "17": "工位二扭力",

    "21": "装配动作",
    "21_1": "装配动作",
    "21_2": "装配动作",
    "21_3": "装配动作",
    "21_4": "装配动作",
    "21_5": "装配动作",
    "21_6": "装配动作",
    "21_7": "装配动作",
    "21_8": "装配动作",
    "21_9": "装配动作",
    "21_10": "装配动作",
    "21_11": "装配动作",
    "21_12": "装配动作",

    "22": "装配结果",
    "22_1": "装配结果",
    "22_2": "装配结果",
    "22_3": "装配结果",
    "22_4": "装配结果",
    "22_5": "装配结果",
    "22_6": "装配结果",
    "22_7": "装配结果",
    "22_8": "装配结果",
    "22_9": "装配结果",
    "22_10": "装配结果",
    "22_11": "装配结果",
    "22_12": "装配结果",

    "31": "检测时间",
    "32": "检测步骤",
    "33": "检测流程",
    "34": "电流",
    "35": "推力",
    "36": "噪声",
    "37": "振动",
    "38": "转速",
    "39": "被检测工件编号"
}

# id对应合格残次
ID_QUALIFIED_VALUE = {
    "12_1": "缺角", "12_2": "划痕", "12_3": "标签错误", "12_4": "合格"
}

# id对应装配动作vlaue字段
ACTION_ID_VALUE = {
    "21_1": "上盖抓取完成",
    "21_2": "上盖抓取错误",
    "21_3": "锁轴垫片抓取完成",
    "21_4": "锁轴垫片抓取错误",
    "21_5": "螺旋桨抓取完成",
    "21_6": "螺旋桨抓取错误",
    "21_7": "上板抓取完成",
    "21_8": "上板抓取错误",
    "21_9": "螺钉一抓取完成",
    "21_10": "螺钉一抓取错误",
    "21_11": "螺钉二抓取完成",
    "21_12": "螺钉二抓取错误"
}

RESULT_ID_VALUE = {
    "22_1": "上盖安装完成",
    "22_2": "上盖安装错误",
    "22_3": "锁轴垫片安装完成",
    "22_4": "锁轴垫片安装错误",
    "22_5": "螺旋桨安装完成",
    "22_6": "螺旋桨安装错误",
    "22_7": "上板安装完成",
    "22_8": "上板安装错误",
    "22_9": "螺钉一安装完成",
    "22_10": "螺钉一安装错误",
    "22_11": "螺钉二安装完成",
    "22_12": "螺钉二安装错误",
}


"""图片"""
# 图片类型
IMG_TAG = {
    1: 'L1', 2: 'L2', 3: 'reg', 4: 'action', 5: 'result'
}

# 图片类型对应的name
IMG_TAG_NAME = {
    'L1': '托盘一工件图片', 'L2': '托盘二工件图片', 'reg': '良品不良品图片',
    'action': '装配动作图片', 'result': '装配结果图片'
}

# 图片类型对应的id
IMG_TAG_ID = {
    'L1': '41', 'L2': '42', 'reg': '43', 'action': '44', 'result': '45'
}

# 图片类型对应文件夹路径
cur_path = os.getcwd()
IMG_PATH = {
    'L1': cur_path + '\\static\\imgLoading1\\', 'L2': cur_path + '\\static\\imgLoading2\\',
    'reg': cur_path + '\\static\\imgReg\\',
    'action': cur_path + '\\static\\imgAction\\', 'result': cur_path + '\\static\\imgResult\\'
}


