from gamera.plugin import *
import _count_under_func

#class colour_image_using_ccs(PluginFunction):
#  """
#  I know this already exists but I need to try something. Colours the image a
#  given colour beneath all the connected components.
#  """
#  self_type = ImageType([RGB])
#  return_type = None
#  args = Args([ImageType([ONEBIT],"binarized_image"), \
#                Pixel("colour")])
#  doc_examples = [(RGB,)]

class count_black_under_line(PluginFunction):
  """
  Returns the number of pixels beneath a given line that are the given colour.
  The arguments 'slope' and 'y_intercept' correspond to the m and b in the
  equation of a line, y = m * x + b, respectively.
  """
  self_type = ImageType([ONEBIT])
  return_type = Int("num_black_pixels")
  args = Args([Real("slope"), Real("y_intercept")])
  doc_examples = [(ONEBIT,)]

class count_black_under_line_points(PluginFunction):
  """
  Returns the number of pixels beneath a given line that are the given colour.
  The arguments x0, y0 are the start coordinates of the line and the arguments
  x1, y1 are the end coordinates of the line.
  """
  self_type = ImageType([ONEBIT])
  return_type = Int("num_black_pixels")
  args = Args([Real("x0"), Real("y0"), Real("x1"), Real("y1")])
  doc_examples = [(ONEBIT,)]

class Count_under_funcModule(PluginModule):
  category = "Analysis"
  cpp_headers = ["count_under_func.hpp"]
#  functions = [count_black_under_line, count_black_under_line_points, \
#      colour_image_using_ccs]
  functions = [count_black_under_line, count_black_under_line_points]
  author = "Nicholas Esrerer"
  url = "nicholas.esterer@gmail.com"

module = Count_under_funcModule()
