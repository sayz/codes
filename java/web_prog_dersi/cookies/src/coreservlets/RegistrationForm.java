package coreservlets;

import java.io.*;
import javax.servlet.*;
import javax.servlet.annotation.*;
import javax.servlet.http.*;

/** Servlet that displays an HTML form to collect user's
 *  first name, last name, and email address. Uses cookies
 *  to determine the initial values of each of those
 *  form fields.
 *  <p>
 *  From <a href="http://courses.coreservlets.com/Course-Materials/">the
 *  coreservlets.com tutorials on servlets, JSP, Struts, JSF, Ajax, GWT, and Java</a>.
 */

@WebServlet("/registration-form")
public class RegistrationForm extends HttpServlet {
  @Override
  public void doGet(HttpServletRequest request,
                    HttpServletResponse response)
      throws ServletException, IOException {
    response.setContentType("text/html");
    PrintWriter out = response.getWriter();
    String firstName =
      CookieUtilities.getCookieValue(request, "firstName", "");
    String lastName =
      CookieUtilities.getCookieValue(request, "lastName", "");
    String emailAddress =
      CookieUtilities.getCookieValue(request, "emailAddress",
                                     "");
    String docType =
      "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0 " +
      "Transitional//EN\">\n";
    String title = "Please Register";
    out.println
      (docType +
       "<HTML>\n" +
       "<HEAD><TITLE>" + title + "</TITLE></HEAD>\n" +
       "<BODY BGCOLOR=\"#FDF5E6\">\n" +
       "<CENTER>\n" +
       "<H1>" + title + "</H1>\n" +
       "<FORM ACTION=\"registration\">\n" +
       "First Name:\n" +
       "  <INPUT TYPE=\"TEXT\" NAME=\"firstName\" " +
                 "VALUE=\"" + firstName + "\"><BR>\n" +
       "Last Name:\n" +
       "  <INPUT TYPE=\"TEXT\" NAME=\"lastName\" " +
                        "VALUE=\"" + lastName + "\"><BR>\n" +
       "Email Address: \n" +
       "  <INPUT TYPE=\"TEXT\" NAME=\"emailAddress\" " +
                 "VALUE=\"" + emailAddress + "\"><P>\n" +
       "<INPUT TYPE=\"SUBMIT\" VALUE=\"Register\">\n" +
       "</FORM></CENTER></BODY></HTML>");
  }
}
