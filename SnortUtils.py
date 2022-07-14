from snortparserlib.snortparser import Parser
import re

class SnortUtils:
    
    def __init__(self, filepath):
        if filepath is not None:
            self.file_path = filepath
        else:
            self.file_path = None

        self.rules = list()


    def get_rules_file(self):
        #gets lines from file path if provided upon initialization and adds them to rule list
        self.rules.clear()

        with open(self.file_path, 'r') as read_obj:
            for line in read_obj.readlines():
                parsed = Parser(line)
                self.rules.append(parsed)

    def get_rules_text(self, text):
        #parses rules from string of one or potentially more rules and adds them to the rule list
        self.rules.clear()
        parsed_text = ''

        for i in text:
            if i != r')':
                parsed_text += i
            else:
                parsed_text += ')'
                parsed = Parser(parsed_text)
                self.rules.append(parsed)
                parsed_text = ''
                parsed = None

    def get_rule_action(self, rule_dict):
        #takes parsed rule dict and returns action if present
        if rule_dict['header']['action'] is not None:
            return rule_dict['header']['action']
        else:
            return None

    def get_rule_protocol(self, rule_dict):
        #takes parsed rule dict and returns protocol if present
        if rule_dict['header']['proto'] is not None:
            return rule_dict['header']['proto']
        else:
            return None

    def get_rule_source_ip(self, rule_dict):
        #takes parsed rule dict and returns source ip if present
        if rule_dict['header']['source'] is not None:
            return rule_dict['header']['source']
        else:
            return None

    def get_rule_src_port(self, rule_dict):
        #takes parsed rule dict and returns source port if present
        if rule_dict['header']['src_port'] is not None:
            return rule_dict['header']['src_port']
        else:
            return None

    def get_rule_direction(self, rule_dict):
        #takes parsed rule dict and returns direction operator
        if rule_dict['header']['arrow'] is not None:
            return rule_dict['header']['arrow']
        else:
            return None

    def get_rule_dest_ip(self, rule_dict):
        #takes parsed rule dict and returns dest ip
        if rule_dict['header']['destination'] is not None:
            return rule_dict['header']['destination']
        else:
            return None
    
    def get_rule_dest_port(self, rule_dict):
        #takes parsed rule dict and returns dest port
        if rule_dict['header']['dst_port'] is not None:
            return rule_dict['header']['dst_port']
        else:
            return None



myclass = SnortUtils('snort-test-cases.txt')

myclass.get_rules_file()

for i in myclass.rules:
    print(myclass.get_rule_dest_(i))


