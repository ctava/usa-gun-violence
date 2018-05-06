# -*- coding: utf-8 -*-
#!/usr/bin/env python
#
# Copyright Christopher Tava
#
import webapp2
import imp

#base = imp.load_source('base', './services/base.py')
from base import BaseHandler

home = imp.load_source('home', './services/home.py')
from home import HomeHandler

data = imp.load_source('data', './services/data.py')
from data import DataHandler

yearsummaryys = imp.load_source('yearsummary', './services/yearsummary.py')
from yearsummary import YearSummaryHandler

config = {
  'webapp2_extras.auth': {
    'user_model': 'appconfig.User',
    'user_attributes': ['email_address']
  },
    'webapp2_extras.sessions': {
    'secret_key': 'GUN'
  }
}

app = webapp2.WSGIApplication([
    webapp2.Route('/',HomeHandler,name='home'),
    webapp2.Route('/data',DataHandler,name='data'),
    webapp2.Route('/yearsummary',YearSummaryHandler,name='yearsummary'),
], config=config, debug=True)

def main():
    wsgiref.handlers.CGIHandler().run(app)

if __name__ == "__main__":
    main()
