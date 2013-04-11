package coreservlets;

import java.io.*;
import javax.servlet.*;
import javax.servlet.annotation.*;
import javax.servlet.http.*;

/** Servlet that builds the HTML form that gathers input
 *  for the search engine servlet. This servlet first
 *  displays a textfield for the search query, then looks up
 *  the search engine names known to SearchUtilities and
 *  displays a list of radio buttons, one for each search
 *  engine. 
 *  <p>
 *  From <a href="http://courses.coreservlets.com/Course-Materials/">the
 *  coreservlets.com tutorials on servlets, JSP, Struts, JSF, Ajax, GWT, and Java</a>.
 */

@WebServlet("/search-engine-form")
public class SearchEngineForm extends HttpServlet {
  @Override
  public void doGet(HttpServletRequest request,
                    HttpServletResponse response)
      throws ServletException, IOException {
    response.setContentType("text/html");
    PrintWriter out = response.getWriter();
    String title = "One-Stop Web Search!";
    String actionURL = "search-engines";
    String docType =
      "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0 " +
      "Transitional//EN\">\n";
    out.println
      (docType +
       "<HTML>\n" +
       "<HEAD><TITLE>" + title + "</TITLE></HEAD>\n" +
       "<BODY BGCOLOR=\"#FDF5E6\">\n" +
       "<CENTER>\n" +
       "<H1>" + title + "</H1>\n" +
       "<FORM ACTION=\"" + actionURL + "\">\n" +
       "  Search keywords: \n" +
       "  <INPUT TYPE=\"TEXT\" NAME=\"searchString\"><P>\n");
    SearchSpec[] specs = SearchUtilities.getCommonSpecs();
    for(int i=0; i<specs.length; i++) {
      String searchEngineName = specs[i].getName();
      out.println("<INPUT TYPE=\"RADIO\" " +
                  "NAME=\"searchEngine\" " +
                  "VALUE=\"" + searchEngineName + "\">\n");
      out.println(searchEngineName + "<BR>\n");
    }
    out.println
      ("<BR>  <INPUT TYPE=\"SUBMIT\">\n" +
       "</FORM>\n" +
       "</CENTER></BODY></HTML>");
  }
}
