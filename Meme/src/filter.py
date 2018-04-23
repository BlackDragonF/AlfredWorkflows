#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys
import json

# hard-coded available templates and information
templates = {
    'sorry' : {
        'placeholder' : ['好啊', '就算你是一流工程师', '就算你出报告再完美', '我叫你改报告你就要改', '毕竟我是客户', '客户了不起啊', 'sorry 客户真的了不起', '以后叫他天天改报告', '天天改 天天改', '客户B', '客户A', '工程师'],
        'subtitle' : '生成“为所欲为”表情包',
        'icon' : 'sorry-icon.png'
    },
    'wangjingze' : {
        'placeholder' : ['我就是饿死', '死外边 从这跳下去', '也不会吃你们一点东西', '真香'],
        'subtitle' : '生成“王境泽”表情包',
        'icon' : 'wangjingze-icon.png'
    },
    'jinkela' : {
        'placeholder' : ['金坷垃好处都有啥', '谁说对了就给他', '肥料掺了金坷垃', '不流失 不蒸发 零浪费', '肥料掺了金坷垃', '能吸收两米下氮磷钾'],
        'subtitle' : '生成“金坷垃”表情包',
        'icon' : 'jinkela-icon.png'
    },
    'dagong' : {
        'placeholder' : ['没有钱啊 肯定要做的啊', '不做的话没有钱用', '那你不会去打工啊', '有手有脚的', '打工是不可能打工的', '这辈子不可能打工的'],
        'subtitle' : '生成“窃格瓦拉”表情包',
        'icon' : 'dagong-icon.png'
    },
    'diandongche' : {
        'placeholder' : ['戴帽子的首先斤里面去', '开始拿剪刀出来 拿那个手机', '手机上有电筒 用手机照射', '寻找那个比较新的电动车', '六月六号 两名男子再次出现', '民警立刻将两人抓获'],
        'subtitle' : '生成“偷电动车”表情包',
        'icon' : 'diandongche-icon.png'
    },
    'marmot' : {
        'placeholder' : ['Aaaaaa', 'Aaaaaa'],
        'subtitle' : '生成“土拨鼠”表情包',
        'icon' : 'marmot-icon.png'
    }
}

# JSON format output's template python object
items = {
    'items' : []
}

# split user input to possible tamplate_name and sentences
inputs = '{query}'.split(None, 1)

template_name = inputs[0] if len(inputs) > 0 else ''
sentences = inputs[1].split('|') if len(inputs) > 1 else ['']

if template_name not in templates:
    # branch: template name is invalid
    # iterate through templates to generate all available items
    # this step also filters output
    for template in templates:
        # filter item that isn't start with input name
        if not template.startswith(template_name):
            continue

        item = {} # acquire a new item
        
        # configure item
        item['uid'] = template
        item['title'] = template
        item['subtitle'] = templates[template]['subtitle']
        item['autocomplete'] = template
        item['valid'] = False 
        item['icon'] = {
            'path' : templates[template]['icon']
        }
        # key 'arg' is unnecessary as valid is set to False

        # append to items
        items['items'].append(item)
else:
    # branch: template name is valid 
    # iterate through correspond template's placeholder to help user complete input
    # and judge if user has finished input

    # only one item needed
    item = {}
    placeholder = templates[template_name]['placeholder'] # get template's placeholder
    sentence_index = len(sentences) # current sentence number
    sentence_count = len(placeholder) # total sentences number

    # configure item
    item['uid'] = template_name
    item['title'] = template_name
    item['subtitle'] = '第' + str(sentence_index) + '句，共' + str(sentence_count) + '句，提示：' + placeholder[sentence_index - 1] + '。'
    item['valid'] = True if sentence_index == sentence_count else False
    item['icon'] = {
        'path' : templates[template_name]['icon']
    }
    # key auto complete is unnecessary as user has to complete templete their own
    item['arg'] = '{query}'

    # append to items
    items['items'].append(item)

# dump items to json and write to output
sys.stdout.write(json.dumps(items))