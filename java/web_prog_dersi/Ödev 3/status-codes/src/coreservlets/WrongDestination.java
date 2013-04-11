package coreservlets;

import java.io.*;
import javax.servlet.*;
import javax.servlet.annotation.*;
import javax.servlet.http.*;

/** Servlet that sends IE users to the Mozilla home page and
 *  Firefox (and all other) users to the Microsoft home page.
 *  <p>
 *  From <a href="http://courses.coreservlets.com/Course-Materials/">the
 *  coreservlets.com tutorials on servlets, JSP, Struts, JSF, Ajax, GWT, and Java</a>.
 */

@WebServlet("/wrong-destination")
public class WrongDestination extends HttpServlet {
  @Override
  public void doGet(HttpServletRequest request,
                    HttpServletResponse response)
      throws ServletException, IOException {
    String userAgent = request.getHeader("User-Agent");
    if ((userAgent != null) &&
        (userAgent.contains("MSIE"))) {
      response.sendRedirect("http://www.mozilla.com/");
    } else {
      response.sendRedirect("http://www.microsoft.com/");
    }
  }
}
