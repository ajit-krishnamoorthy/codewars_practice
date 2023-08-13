function quadrant(x, y) {
    // Poveli!
    //Given a point in a Euclidean plane (x and y), return the quadrant the point exists in: 1, 2, 3 or 4 (integer). x and y are non-zero integers, therefore the given point never lies on the axes.
    
    //Checking for first quadrant
    if (x>0 && y>0)
      {
        return 1;
      }
    //Checking for second quadrant
      if (x<0 && y>0)
      {
        return 2;
      }
    //Checking for third quadrant
      if (x<0 && y<0)
      {
        return 3;
      }
    //Checking for fourth quadrant
      if (x>0 && y<0)
      {
        return 4;
      }
  }