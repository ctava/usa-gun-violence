#!/usr/bin/env python

from google.appengine.ext.webapp import template
import webapp2

from base import BaseHandler

class HomeHandler(BaseHandler):
  def get(self):
    self.render_template('index.html')
