package com.sayz.web;

import java.io.IOException;
import java.io.PrintWriter;
import java.util.Enumeration;

import javax.servlet.ServletException;
import javax.servlet.annotation.WebServlet;
import javax.servlet.http.HttpServlet;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;

/**
 * Servlet implementation class FormData
 */
@WebServlet("/FormData")
public class FormData extends HttpServlet {
	private static final long serialVersionUID = 1L;
       
    /**
     * @see HttpServlet#HttpServlet()
     */
    public FormData() {
        super();
        // TODO Auto-generated constructor stub
    }

	/**
	 * @see HttpServlet#doGet(HttpServletRequest request, HttpServletResponse response)
	 */
    public void doGet(HttpServletRequest request,
    		HttpServletResponse response)
    		throws ServletException, IOException {
    		response.setCharacterEncoding("utf-8");
    		response.setContentType("text/html");
    		PrintWriter out = response.getWriter();
    		String docType =
    		"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0 " +
    		"Transitional//EN\">\n";
    		String title = "Reading All Request Parameters";
    		out.println(docType +
			    		"<HTML>\n" +
			    		"<HEAD><TITLE>" + title + "</TITLE></HEAD>\n" +
			    		"<BODY>\n" +
			    		"<H1 ALIGN=CENTER>" + title + "</H1>\n" +
			    		"<TABLE BORDER=1 ALIGN=CENTER>\n" +
			    		"<TR BGCOLOR=\"#FFAD00\">\n" +
			    		"<TH>Parameter Name<TH>Parameter Value(s)");
    		Enumeration<String> paramNames = request.getParameterNames();
    		while (paramNames.hasMoreElements()) {
				String paramName = (String) paramNames.nextElement();
				out.print("<TR><TD>" + paramName + "\n<TD>");
				String[] paramValues = request.getParameterValues(paramName);
				if (paramValues.length == 1) {
					String paramValue = paramValues[0];
					
					if (paramValue.length() == 0)
						out.println("<i>no value</i>");	
					else 
						out.print(paramValue);
					
				}
				else {
					out.println("<ul>");
					
					for(int i=0; i<paramValues.length; i++) {
						out.println("<li>" + paramValues[i]);
					}
					out.println("</ul>");
				}
				
			}
    
    		out.println("</table>\n</body></html>");
}
    		
    		public void doPost(HttpServletRequest request,
    				HttpServletResponse response)
    						throws ServletException, IOException {
		doGet(request, response);
	}

}
