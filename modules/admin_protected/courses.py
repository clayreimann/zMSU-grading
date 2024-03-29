# Simple CherryPy site
# Clay Reimann 5/13/2013
# All rights reserved

# Import CherryPy global namespace
import cherrypy

from .. import db
from ..base import Base

class Courses(Base):
  """
    The courses controller
  """
  def __init__(self, tmpl_lookup):
    super(Courses, self).__init__(tmpl_lookup)
    self.page_title = "Courses"

  @cherrypy.expose
  def index(self, **params):
    """
      Displays all of the courses in the system
    """
    error = self.check_params(**params)
    if error == None and len(params) != 0:
      return self.add_course(**params)
    return self.render("admin/courses/all.html", error=error, courses=db.all_courses())

  def check_params(self, **params):
    """
      Checks the params and returns a description of the
      error, or None
    """
    if len(params) == 0:
      return ""

    if "courseNum" not in params:
      return "A course number is required."

    return None

  def add_course(self, courseNum):
    """
      Call the database function to add a course
    """
    db.add_course(courseNum)
    raise cherrypy.HTTPRedirect("/admin/courses")


  @cherrypy.expose
  def show(self, course=None):
    """
      Displays one course's listing
    """
    if course == None:
      raise cherrypy.HTTPRedirect("/admin/courses")
    else:
      c = db.get_course(courseNumber=course)
      return self.render("admin/courses/show.html", course=c)

  @cherrypy.expose
  def remove(self, course=None):
    """
      !!Not Implemented!!

      Displays a list of the courses in the system for removal
    """
    raise cherrypy.HTTPRedirect("/admin/courses")
