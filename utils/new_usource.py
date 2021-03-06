#!/usr/bin/env python3
# -*- coding:utf-8 -*-
#
#   Author  :   renyuneyun
#   E-mail  :   renyuneyun@gmail.com
#   Date    :   18/04/22 00:15:11
#   License :   Apache 2.0 (See LICENSE)
#

'''

'''

import argparse
import sys
import os.path
import templates

template_maps = {
        'main': {
            'skill': templates.tmpl_usource_skill,
            'data': templates.tmpl_usource_data,
            'data_factory': templates.tmpl_usource_data_factory,
            'view_fragment': templates.tmpl_skill_view_fragment,
            'tracker': templates.tmpl_usource_tracker,
            'slot': templates.tmpl_usource_slot,
            },
        'androidTest': {
            'androidTest$data': templates.tmpl_androidTest_data,
            },
        }

def new_event(cname, identifier):
    pdef = {}
    pdef['package'] = "ryey.easer.skills.usource.{}".format(identifier)
    pdef['skill'] = "{}USourceSkill".format(cname)
    pdef['id'] = identifier
    pdef['data'] = "{}USourceData".format(cname)
    pdef['data_factory'] = "{}USourceDataFactory".format(cname)
    pdef['view_fragment'] = "{}SkillViewFragment".format(cname)
    pdef['tracker'] = "{}Tracker".format(cname)
    pdef['slot'] = "{}Slot".format(cname)
    pdef['androidTest$data'] = "{}USourceDataTest".format(cname)
    for t, template_map in template_maps.items():
        dest = "app/src/{}/java/ryey/easer/skills/usource/{}".format(t, identifier)
        if not os.path.isfile(dest):
            os.mkdir(dest)
        for k in template_map:
            class_content = template_map[k].format_map(pdef)
            with open("{}/{}.java".format(dest, pdef[k]), 'w') as fd:
                fd.write(templates.tmpl_copyright)
                fd.write('\n')
                fd.write(class_content)

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('cname', metavar='class_name_prefix', help='Prefix for all classes of this skill')
    parser.add_argument('id', help='Internal unique identifier of this skill. Also used as the package name')
    args = parser.parse_args()
    new_event(args.cname, args.id)

