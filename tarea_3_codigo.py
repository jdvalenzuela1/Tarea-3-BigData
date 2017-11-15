# -*- coding: utf-8 -*-
from mrjob.job import MRJob
from mrjob.step import MRStep
from mrjob.protocol import JSONValueProtocol
import re
import itertools
import csv
import string
import json
import time

# Business primero y luego Review

class EstrellasRestaurantes(MRJob):

    SORT_VALUES = True
      
    def mapper_join(self, _, line):    
        line = obj = json.loads(line)
        if len(line.keys()) == 15: # Business
          business_id = line["business_id"]
          categories = line["categories"]
          yield business_id, ['A', categories]
        elif len(line.keys()) == 9: # Review
          stars = line["stars"]
          business_id = line["business_id"]
          yield business_id, [stars]
      
    def reducer_categories(self, keys, values):
        values = [x for x in values]
        categories = []
        for value in range(len(values)-1):
            if values[value][0] == 'A':
                categories =  values[value][1]
                values.pop(value)
        if len(categories) > 0:
            for category in categories:
                yield category, values
    def reducer_stars(self, keys, values):
        line = ""
        values = [x for x in values]
        for element in values[0]:
            line += str(element[0]) +';'
        tarea_3.write(keys + ';'+line[:-1]  +"\n")
        yield keys, values

    def steps(self):
        return [MRStep(mapper=self.mapper_join, reducer=self.reducer_categories),
                MRStep(reducer=self.reducer_stars)]


if __name__ == '__main__':
    tarea_3 = open("tarea_3.csv", "w")
    start_time = time.time()
    EstrellasRestaurantes.run()
    tarea_3.close()
    print "--- %s seconds ---" % (time.time() - start_time)
    
