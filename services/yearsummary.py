# -*- coding: utf-8 -*-
#!/usr/bin/env python
#
# Copyright Christopher Tava
#
import webapp2
from google.appengine.ext import db
from google.appengine.api import app_identity
from google.appengine.api import mail
import logging
import sys
import json

class YearSummary(db.Model):
  year = db.StringProperty(required=True)
  month = db.StringProperty(required=True)
  n_killed = db.IntegerProperty(required=True)
  n_injured = db.IntegerProperty(required=True)
  def to_dict(self):
    return dict([(p, unicode(getattr(self, p))) for p in self.properties()])
 

class YearSummaryHandler(webapp2.RequestHandler):

    def get(self):
        try:
            self.response.headers['Content-Type'] = 'application/json'
            query = db.Query(YearSummary) 
            year=self.request.get('year')
            if (year):
                query.filter('year',year)
            month=self.request.get('month')
            if (month):
                query.filter('month',month)                                                
            response = ''
            iteration = 0
            for i in query: 
                iteration += 1
                if iteration == 1:
                  response += '['
                if iteration >= 1:
                  response += '{year":"'+str(i.year)+'","month":"'+str(i.month)+'","n_killed":"'+str(i.n_killed)+'","n_injured":"'+str(i.n_injured)+'"'
                if iteration != query.count():
                    response += '},'
                if iteration == query.count():
                    response += '}]'
            self.response.write(response)
        except:
            self.response.write("{\"error\":\"true\"}")      
            logging.error(sys.exc_info()[0])        
            logging.error(sys.exc_info()[1])
            logging.error(sys.exc_info()[2])

    def put(self):
      try:
        self.response.headers['Content-Type'] = 'application/json'      
        year = self.request.get("year")   
        if (not year):
            self.response.write('{"error":"true","comments":"year is missing"}')
            return
        month = self.request.get("month")   
        if (not month):
            self.response.write('{"error":"true","comments":"month is missing"}')
            return
        n_killed = self.request.get("n_killed")   
        if (not n_killed):
            self.response.write('{"error":"true","comments":"n_killed is missing"}')
            return
        n_injured = self.request.get("n_injured")   
        if (not n_injured):
            self.response.write('{"error":"true","comments":"n_injured is missing"}')
            return
        yearsummary = YearSummary(key_name=str(year+month),year=str(year),month=str(month),n_killed=int(n_killed),n_injured=int(n_injured))
        yearsummary.put()
        self.response.write('{"error":"false"}')
      except ValueError:
        pass        
      except:
        self.response.write("{\"error\":\"true\"}")        
        logging.error(sys.exc_info()[0])        
        logging.error(sys.exc_info()[1])
        logging.error(sys.exc_info()[2])

    def delete(self):
      try:
        self.response.headers['Content-Type'] = 'application/json'     
        query = db.Query(YearSummary)  
        year=self.request.get('year')
        if (year):
            query.filter('year',year)
        month=self.request.get('month')
        if (month):
            query.filter('month',month) 
        for i in query:
            i.delete();
        self.response.write("{\"error\":\"false\"}")
      except:
        self.response.write("{\"error\":\"true\"}")        
        logging.error(sys.exc_info()[0])        
        logging.error(sys.exc_info()[1])
        logging.error(sys.exc_info()[2])
