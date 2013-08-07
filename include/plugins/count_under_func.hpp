#ifndef COUNT_UNDER_FUNC_HPP
#define COUNT_UNDER_FUNC_HPP 

#include "gamera.hpp"
#include "plugins/draw.hpp"
#include "plugins/segmentation.hpp"
#include <vector> 

using namespace Gamera;

template<class T>
int
count_black_under_line(const T &img, double m, double b)
{
  unsigned int count = 0;
  size_t i;
  for (i = img.ul_x(); i < img.lr_x(); ++i) {
    if ( is_black( img.get( Point(i, m * i + b) ) ) )
      ++count;
  }
  return count;
}

template<class T>
int
count_black_under_line_points(const T &img, double x0, double y0, double x1, double y1)
{
  return count_black_under_line(img, (y1 - y0) / (x1 - x0), y0 - x0 * (y1 - y0) / (x1 - x0));
}

/* This doesn't work */
/*
template<class T, class U>
void
colour_image_using_ccs(T &img, U &binimg, const RGBPixel &p)
{
  ImageList* ccs = cc_analysis(binimg);
  ImageList::iterator ccs_it;
*/
  /* Create an image data object that holds pointers to connected components */
/*
  ImageData<Cc*> pointer_data = ImageData(Dim(img.width()img.height()));

  for (ccs_it = ccs->begin(); ccs_it != ccs->end(); ++ccs_it) {
    
    Cc* cc = static_cast<Cc*>(*ccs_it);


    highlight(pointer_data, *cc, cc );
  }
}
*/
  



#endif /* COUNT_UNDER_FUNC_HPP */
