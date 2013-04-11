package coreservlets;

import java.io.*;
import javax.servlet.http.*;
import java.util.zip.*;

/** Three small static utilities to assist with gzip encoding.
 *  <UL>
 *    <LI>isGzipSupported: does the browser support gzip?
 *    <LI>isGzipDisabled: has the user passed in a flag
 *        saying that gzip encoding should be disabled for
 *        this request? (Useful so that you can measure
 *        results with and without gzip on the same browser).
 *    <LI>getGzipWriter: return a gzipping PrintWriter.
 *  </UL>
 *  <p>
 *  From <a href="http://courses.coreservlets.com/Course-Materials/">the
 *  coreservlets.com tutorials on servlets, JSP, Struts, JSF, Ajax, GWT, and Java</a>.
 */

public class GzipUtilities {
  
  /** Does the client support gzip? */
  
  public static boolean isGzipSupported
      (HttpServletRequest request) {
    String encodings = request.getHeader("Accept-Encoding");
    return((encodings != null) &&
           (encodings.contains("gzip")));
  }

  /** Has user disabled gzip (e.g., for benchmarking)? */
  
  public static boolean isGzipDisabled
      (HttpServletRequest request) {
    String flag = request.getParameter("disableGzip");
    return((flag != null) && (!flag.equalsIgnoreCase("false")));
  }

  /** Return gzipping PrintWriter for response. */
  
  public static PrintWriter getGzipWriter
      (HttpServletResponse response) throws IOException {
    return(new PrintWriter
            (new GZIPOutputStream
              (response.getOutputStream())));
  }
}
