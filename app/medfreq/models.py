#######

# This program would generate PWM on GPIO 7 Pin 26 of P1

# with 50% Dutycyle at 1kHz

#######


import json
import os
from decimal import Decimal

import RPi.GPIO as GPIO
from django.core import serializers
from django.db import models

from tools import hasStrNumbers

gpio_pin_numbers = [5, 6, 7, 13, 12, 16, 19, 20, 21, 26]

GPIO.setmode(GPIO.BCM)
GPIO.setup(gpio_pin_numbers, GPIO.OUT)

gpio_objects = []

data_path = "{}{}".format(os.getcwd(), '/medfreq/data/')

txt_path = "{}{}".format(data_path, "illnesses.txt")
xml_path = "{}{}".format(data_path, "illnesses.xml")
json_path = "{}{}".format(data_path, "illnesses.json")


class IllnessManager(models.Manager):
    def load(self):  # loads data into mysql db
        with open(txt_path) as f:
            file_content = f.readlines()
            db_index = 0
            for row in file_content:
                frequencies_decimal = []
                if len(row) > 2:  # check if row contains name of disease
                    try:
                        split = row.split(":")
                        name = split[0]
                        if hasStrNumbers(str(split)):
                            frequencies = split[1].split(",")
                            if len(frequencies) == 10:  # row contains correct number of frequencies
                                for row in frequencies:
                                    frequencies_decimal.append(str(Decimal(row)))
                                x = IllnessItem(db_index, name, frequencies_decimal, 50)  # create object
                                db_index += 1
                                x.save()  # save object to db
                    except Exception:
                        pass

    def get(self, name):
        illnesses = self.get_all()
        # get specyfied illness base on name
        return [x for x in illnesses if x.name == name][0]

    @staticmethod
    def get_all():
        all_objects = IllnessItem.objects.all()
        return all_objects

    @staticmethod
    def write_xml():
        data = serializers.serialize("xml", IllnessItem.objects.all(), sort_keys=True, indent=2)
        out = open(xml_path, "w")
        out.write(data)
        out.close()

    @staticmethod
    def read_xml():
        data = open(xml_path, 'r').read()
        return data

    @staticmethod
    def write_json():
        data = serializers.serialize("json", IllnessItem.objects.all(), sort_keys=True, indent=2)
        out = open(json_path, "w")
        out.write(data)
        out.close()

    @staticmethod
    def read_json():
        data = open(json_path, 'r').read()
        jsn = json.loads(data)
        return jsn

    def play(illness):
        # play specyfied illness frequencies
        for i, frequency in enumerate(illness.frequencies):
            gpio_obj = gpio_objects[i]
            gpio_obj.ChangeFrequency(Decimal(frequency))
            gpio_obj.start(illness.fill_time)

    @staticmethod
    def stop():
        # stop playing frequencies and release resources
        GPIO.cleanup()

    @staticmethod
    def init():
        # initialize all gpio objects
        for i, pin in enumerate(gpio_pin_numbers):
            obj = GPIO.PWM(pin, 1)
            gpio_objects.append(obj)


class IllnessItem(models.Model):
    name = models.CharField(max_length=100)
    frequencies = models.CharField(max_length=100)
    fill_time = models.IntegerField()





